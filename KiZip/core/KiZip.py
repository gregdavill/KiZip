import os
import json
import re
import sys
from datetime import datetime
import logging
import wx

import zipfile
import shutil

import pcbnew

from .config import Config
from ..dialog import SettingsDialog
from ..errors import ParsingException
from .parser import Parser




class Logger(object):

    def __init__(self, cli=False):
        self.cli = cli
        self.logger = logging.getLogger('KiZip')
        self.logger.setLevel(logging.INFO)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter(
                "%(asctime)-15s %(levelname)s %(message)s")
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def info(self, *args):
        if self.cli:
            self.logger.info(*args)

    def error(self, msg):
        if self.cli:
            self.logger.error(msg)
        else:
            wx.MessageBox(msg)

    def warn(self, msg):
        if self.cli:
            self.logger.warn(msg)
        else:
            wx.LogWarning(msg)


log = None  # type: Logger or None


def process_substitutions(output_name_format, pcb_file_name, metadata):
    # type: (str, str, dict)->str
    name = output_name_format.replace('%f', os.path.splitext(pcb_file_name)[0])
    name = name.replace('%p', metadata['title'])
    name = name.replace('%c', metadata['company'])
    name = name.replace('%r', metadata['revision'])
    name = name.replace('%d', metadata['date'].replace(':', '-'))
    now = datetime.now()
    name = name.replace('%D', now.strftime('%Y-%m-%d'))
    name = name.replace('%T', now.strftime('%H-%M-%S'))
    # sanitize the name to avoid characters illegal in file systems
    name = name.replace('\\', '/')
    name = re.sub(r'[?%*:|"<>]', '_', name)
    return name + '.zip'

class KiZipPlugin(pcbnew.ActionPlugin, object):

    def __init__(self):
        super(KiZipPlugin, self).__init__()
        self.name = "Generate Gerber Package"
        self.category = "Read PCB"
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        icon_dir = os.path.dirname(os.path.dirname(__file__))
        self.icon_file_name = os.path.join(icon_dir, 'icon.png')
        self.description = "Generate Gerber Package"

    def defaults(self):
        pass

    def Run(self):
        from ..version import version
        from ..errors import ParsingException
        self.version = version
        board = pcbnew.GetBoard()
        pcb_file_name = board.GetFileName()
        config = Config(self.version, os.path.dirname(pcb_file_name))

        logger = Logger()
        if not pcb_file_name:
            logger.error('Please save the board file before generating gerbers')
            return

        parser = Parser(pcb_file_name, config, logger, board)
        try:
            run_with_dialog(parser, config, logger)
        except ParsingException as e:
            logger.error(str(e))


def main(parser, config, logger):
    # type: (Parser, Config, Logger) -> None
    global log
    log = logger
    pcb_file_name = os.path.basename(parser.file_name)
    pcb_file_dir = os.path.dirname(parser.file_name)

    
    pcbdata = parser.parse()

    file_list = parser.plot()


    # debug
    print(file_list)
    

    if os.path.isabs(config.output_dest_dir):
        output_file_dir = config.output_dest_dir
    else:
        output_file_dir = os.path.join(pcb_file_dir, config.output_dest_dir)

    output_file_name = process_substitutions(
            config.output_name_format, pcb_file_name, pcbdata['metadata'])
    output_file_name = os.path.join(output_file_dir, output_file_name)
    os.makedirs(output_file_dir, exist_ok=True)

    #zip up all files
    with zipfile.ZipFile(output_file_name, "w", zipfile.ZIP_DEFLATED) as zf:
        for filename in  file_list:
            zf.write(filename=os.path.abspath(filename), arcname=os.path.basename(filename))
        



def run_with_dialog(parser, config, logger):
    # type: (Parser, Config, Logger) -> None
    def save_config(dialog_panel):
        config.set_from_dialog(dialog_panel)
        config.save()

    config.load_from_ini()
    dlg = SettingsDialog(
            config_save_func=save_config,
            file_name_format_hint=config.FILE_NAME_FORMAT_HINT,
            version=config.version
    )
    try:
        config.transfer_to_dialog(dlg.panel)
        if dlg.ShowModal() == wx.ID_OK:
            config.set_from_dialog(dlg.panel)
            main(parser, config, logger)
    finally:
        dlg.Destroy()