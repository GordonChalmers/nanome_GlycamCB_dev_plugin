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


from GlycamCB_menu import GlycamCBMenu

NAME = "Glycam Carbohydrate Builder"
DESCRIPTION = "Construct minimized oligasaccharide structure pdb from a sequence."
CATEGORY = "Carbohydrate Tools"
HAS_ADVANCED_OPTIONS = False

class GlycamCB(nanome.PluginInstance):
    def start(self):
#        print("started")
        Logs.debug("Start Glycam Carbohydrate Builder Plugin")
        self.test_menu=GlycamCBMenu(self)

    def on_run(self,button='TRUE'):
        self.menu.enabled = True
        self.update_menu(self.menu)

        
def main():
    plugin = nanome.Plugin("GlycamCB", "Input an oligasaccharide sequence and obtain a minimized pdb.", "pdb_from_sequence", False)
    plugin.set_plugin_class(GlycamCB)
    plugin.run('127.0.0.1',8888)

if __name__ == "__main__":
    main()
