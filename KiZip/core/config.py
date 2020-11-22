"""Config object"""

import argparse
import os
import re

from wx import FileConfig
import wx

from .. import dialog
from .kicad import layer_names, layers_default


class Config:
    FILE_NAME_FORMAT_HINT = (
        'Output file name format supports substitutions:\n'
        '\n'
        '    %f : original pcb file name without extension.\n'
        '    %p : pcb/project title from pcb metadata.\n'
        '    %c : company from pcb metadata.\n'
        '    %r : revision from pcb metadata.\n'
        '    %d : pcb date from metadata if available, '
        'file modification date otherwise.\n'
        '    %D : gerber generation date.\n'
        '    %T : gerber generation time.\n'
        '\n'
        'Extension will be added automatically.'
    )  # type: str

    LAYER_NAMES = layer_names # type: list

    # Helper constants
    config_file = os.path.join(os.path.dirname(__file__), '..', 'config.ini')

    # Defaults
    
    # General 
    output_dest_dir = 'Production/'  # This is relative to pcb file directory
    output_name_format = '%f_gerber_%D_%T'

    # Layers
    layers = [{'layer':l, 'ext':'', 'enabled': (l in layers_default)} for l in LAYER_NAMES]
    

    @staticmethod
    def _split(s):
        """Splits string by ',' and drops empty strings from resulting array."""
        return [a.replace('\\,', ',') for a in re.split(r'(?<!\\),', s) if a]

    @staticmethod
    def _join(lst):
        return ','.join([s.replace(',', '\\,') for s in lst])

    def __init__(self, version, rel_directory=None):
        self.version = version
        self.rel_directory = rel_directory

    def load_from_ini(self):
        """Init from config file if it exists."""
        if not os.path.isfile(self.config_file):
            return
        f = FileConfig(localFilename=self.config_file)
        f.SetPath('/general')
        self.output_dest_dir = f.Read('output_dest_dir', self.output_dest_dir)
        self.output_name_format = f.Read('output_name_format', self.output_name_format)


        f.SetPath("/layers")
        for index in range(len(self.layers)):
            d = self.layers[index]
            d['enabled'] = f.ReadBool(f'{d["layer"]}_enabled', d['enabled'])
        


    def save(self):
        f = FileConfig(localFilename=self.config_file)

        f.SetPath('/general')
        output_dest_dir = self.output_dest_dir
        if output_dest_dir.startswith(self.rel_directory):
            output_dest_dir = os.path.relpath(
                    output_dest_dir, self.rel_directory)
        f.Write('output_dest_dir', output_dest_dir)
        f.Write('output_name_format', self.output_name_format)

        f.SetPath("/layers")
        for index in range(len(self.layers)):
            d = self.layers[index]
            f.WriteBool(f'{d["layer"]}_enabled',d['enabled'])
        
        f.Flush()

    def set_from_dialog(self, dlg):
        # type: (dialog.settings_dialog.SettingsDialogPanel) -> None
        
        # General
        self.output_dest_dir = dlg.general.outputDirPicker.Path
        self.output_name_format = dlg.general.fileNameFormatTextControl.Value

        # Layers
        for index in range(len(self.layers)):
            layer = self.layers[index]

            #item.SetText(layer['layer'])
            #dlg.layers.LayerList.InsertItem(item)
            #dlg.layers.LayerList.SetItem(index,0,layer['layer'])
            #dlg.layers.LayerList.SetItem(index,1,layer['ext'])

            if index in dlg.layers.selected:
                layer['enabled'] = True
            else:
                layer['enabled'] = False

    def transfer_to_dialog(self, dlg):
        # type: (dialog.settings_dialog.SettingsDialogPanel) -> None

        # General
        import os.path
        if os.path.isabs(self.output_dest_dir):
            dlg.general.outputDirPicker.Path = self.output_dest_dir
        else:
            dlg.general.outputDirPicker.Path = os.path.join(
                    self.rel_directory, self.output_dest_dir)
        dlg.general.fileNameFormatTextControl.Value = self.output_name_format

        # Layers
        for index in range(len(self.layers)):
            layer = self.layers[index]

            item = wx.ListItem()
            item.SetId(index)

            item.SetText(layer['layer'])
            dlg.layers.LayerList.InsertItem(item)
            dlg.layers.LayerList.SetItem(index,0,layer['layer'])
            dlg.layers.LayerList.SetItem(index,1,layer['ext'])

            if layer['enabled']:
                dlg.layers.selected.append(index)

        dlg.layers.UpdateListSelections()


    # noinspection PyTypeChecker
    def add_options(self, parser, file_name_format_hint):
        # type: (argparse.ArgumentParser, str) -> None
        parser.add_argument('--show-dialog', action='store_true',
                            help='Shows config dialog. All other flags '
                                 'will be ignored.')

        # General
        parser.add_argument('--dest-dir', default=self.output_dest_dir,
                            help='Destination directory for output file '
                                 'relative to pcb file directory.')
        parser.add_argument('--name-format', default=self.output_name_format,
                            help=file_name_format_hint.replace('%', '%%'))

    def set_from_args(self, args):
        # type: (argparse.Namespace) -> None
        import math

        # General
        self.output_dest_dir = args.dest_dir
        self.output_name_format = args.name_format

