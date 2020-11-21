"""Config object"""

import argparse
import os
import re

from wx import FileConfig

from .. import dialog


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
        '    %D : bom generation date.\n'
        '    %T : bom generation time.\n'
        '\n'
        'Extension will be added automatically.'
    )  # type: str

    # Helper constants
    config_file = os.path.join(os.path.dirname(__file__), '..', 'config.ini')

    # Defaults


    @staticmethod
    def _split(s):
        """Splits string by ',' and drops empty strings from resulting array."""
        return [a.replace('\\,', ',') for a in re.split(r'(?<!\\),', s) if a]

    @staticmethod
    def _join(lst):
        return ','.join([s.replace(',', '\\,') for s in lst])

    def __init__(self, version):
        self.version = version

    def load_from_ini(self):
        """Init from config file if it exists."""
        if not os.path.isfile(self.config_file):
            return
        f = FileConfig(localFilename=self.config_file)


    def save(self):
        f = FileConfig(localFilename=self.config_file)

        
        f.Flush()

    def set_from_dialog(self, dlg):
        # type: (dialog.settings_dialog.SettingsDialogPanel) -> None
        ...

    def transfer_to_dialog(self, dlg):
        # type: (dialog.settings_dialog.SettingsDialogPanel) -> None
        ...

    # noinspection PyTypeChecker
    def add_options(self, parser, file_name_format_hint):
        ...

    def set_from_args(self, args):
        # type: (argparse.Namespace) -> None
        import math


    def get_html_config(self):
        import json
        d = {f: getattr(self, f) for f in self.html_config_fields}
        return json.dumps(d)
