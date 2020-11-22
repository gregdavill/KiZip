#!/usr/bin/python3
from __future__ import absolute_import

import argparse
import os
import sys

import pcbnew

# python 2 and 3 compatibility hack
def to_utf(s):
    if isinstance(s, bytes):
        return s.decode('utf-8')
    else:
        return s


if __name__ == "__main__":
    # Add ../ to the path
    # Works if this script is executed without installing the module
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(script_dir))
    os.environ['KIZIP_CLI_MODE'] = 'True'
    

    from KiZip.core import KiZip
    from KiZip.core.config import Config
    from KiZip.core.parser import Parser
    
    #from KiZip.ecad import get_parser_by_extension
    from KiZip.version import version
    from KiZip.errors import (ExitCodes, ParsingException,
                                          exit_error)

    create_wx_app = 'KIZIP_NO_DISPLAY' not in os.environ
    if create_wx_app:
        import wx
        app = wx.App()

    parser = argparse.ArgumentParser(
            description='KiCad KiZip plugin CLI.',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('file',
                        type=lambda s: to_utf(s),
                        help="KiCad PCB file")
    config = Config(version) 
    config.add_options(parser, config.FILE_NAME_FORMAT_HINT)
    args = parser.parse_args()
    logger = KiZip.Logger(cli=True)
    if not os.path.isfile(args.file):
        exit_error(logger, ExitCodes.ERROR_FILE_NOT_FOUND,
                   "File %s does not exist." % args.file)
    print("Loading %s" % args.file)
    
    config.rel_directory = os.path.dirname(args.file)
    board  = pcbnew.LoadBoard(args.file)

    parser = Parser(args.file, config, logger, board)
    if args.show_dialog:
        if not create_wx_app:
            exit_error(logger, ExitCodes.ERROR_NO_DISPLAY, "Can not show dialog when "
                       "KIZIP_NO_DISPLAY is set.")
        try:
            KiZip.run_with_dialog(parser, config, logger)
        except ParsingException as e:
            exit_error(logger, ExitCodes.ERROR_PARSE, e)
    else:
        config.set_from_args(args)
        try:
            KiZip.main(parser, config, logger)
        except ParsingException as e:
            exit_error(logger, ExitCodes.ERROR_PARSE, str(e))
