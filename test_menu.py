import nanome
from nanome.util import Logs
from nanome.util import Color

import copy
import re
import math
import numpy as np
import os

class TestMenu():
    def __init__(self, plugin):
# import the json file of the new UI
        menu = nanome.ui.Menu.io.from_json(os.path.join(os.path.dirname(__file__), 'GlycamCB_pluginator.json'))
        self.plugin=plugin
        self.plugin.menu = menu
        self.plugin.update_menu(self.plugin.menu)
#        self.build_menu(menu)

# layout node setup (run)
        ln_btn_run = self.plugin.menu.root.find_node('Run Button')
        btn_run = ln_btn_run.get_content()
        btn_run.register_pressed_callback(test_print)
        
# layout node setup (clear)
        ln_btn_clear = self.plugin.menu.root.find_node('Clear Button')
        btn_clear = ln_btn_clear.get_content()
        btn_clear.register_pressed_callback(test_print)

    def test_print():
        print("test button")
        
    def _on_run(self):
        print("test button")

 
    def _request_refresh(self):
        self._plugin.request_refresh()

    def update_button(self, button):
        self.update_content(button)

    def make_plugin_usable(self):
        self.menu.make_plugin_usable()

    def build_menu(self):

    # refresh the lists
        def refresh_button_pressed_callback(button):
            self._request_refresh()
            
    # press the run button and run the algorithm
        def run_button_pressed_callback(button):
            self.sequence = self.menu.root.find_node('sequence').get_content()
            print("test")
        
        # create the layout node that contains select and run and refresh
        self.ln_select_run = menu.root.find_node("Refresh Run",True)

        # create the Run button
        self.run_button = menu.root.find_node("Run", True).get_content()
        self.run_button.register_pressed_callback(run_button_pressed_callback)

        # create the Clear button
        refresh_button = menu.root.find_node("Clear", True).get_content()
        refresh_button.register_pressed_callback(clear_button_pressed_callback)

#        self._menu = menu
        
