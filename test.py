import nanome
from nanome.util import Logs

import sys
import time
import numpy as np
import re
import os
from os import path

import json
import requests
import tempfile
import traceback


# specific to GlycamCB menu test

from test_menu import TestMenu

NAME = "Glycam Carbohydrate Builder"
DESCRIPTION = "Construct oligasaccharide structure pdb from a sequence."
CATEGORY = "Carbohydrate Tools"
HAS_ADVANCED_OPTIONS = False

MENU_PATH = path.join(path.dirname(path.realpath(__file__)), "GlycamCB_pluginator.json")

class test(nanome.PluginInstance):
    def start(self):
        Logs.debug("Start Glycam Carbohydrate Builder Plugin")
        self._menu = nanome.ui.Menu.io.from_json(os.path.join(os.path.dirname(__file__), 'GlycamCB_pluginator.json'))
        self._menu.enabled=True

    def on_run(self):
        menu = self.menu
        menu.enabled = True
        
def main():
    plugin = nanome.Plugin("GlycamCB", "Input an oligasaccharide sequence and obtain a minimized pdb.", "pdb_from_sequence", False)
    plugin.set_plugin_class(test)
    plugin.run('127.0.0.1',8888)

if __name__ == "__main__":
    main()
