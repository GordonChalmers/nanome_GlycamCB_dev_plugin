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

DIR = os.path.dirname(__file__)

class test(nanome.PluginInstance):
    def start(self):
        print("started")
        Logs.debug("Start Glycam Carbohydrate Builder Plugin")
        self.menu = nanome.ui.Menu.io.from_json(os.path.join(DIR, 'GlycamCB_pluginator.json'))
#        self.settings = SettingsMenu(self, self.open_menu)

#        self.menu.enabled = True
#        self.update_menu(self.menu)

#        self.on_run_button()
#        self.update_menu(self.menu)


    def on_run(self,button='TRUE'):
        self.menu.enabled = True
        self.update_menu(self.menu)

#    def open_menu(self, menu=None):
#        self.menu = self._menu
#        self.menu.enabled = True
#        self.update_menu(self.menu)

        
def main():
    plugin = nanome.Plugin("GlycamCB", "Input an oligasaccharide sequence and obtain a minimized pdb.", "pdb_from_sequence", False)
    plugin.set_plugin_class(test)
    plugin.run('127.0.0.1',8888)

if __name__ == "__main__":
    main()
