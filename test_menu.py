import nanome
from nanome.util import Logs
from nanome.util import Color

import os

class TestMenu():
    def __init__(self, _plugin):
# import the json file of the new UI
        menu = nanome.ui.Menu.io.from_json(os.path.join(os.path.dirname(__file__), 'GlycamCB_pluginator.json'))
        self._plugin.menu = menu
        self._plugin.update_menu(menu)

        self._run_button = None

    def update_button(self, button):
        self.update_content(button)

    def make_plugin_usable(self):
        self._menu.make_plugin_usable()

    # change the args in the plugin
    def update_args(self,arg,option):
        self._plugin.update_args(arg,option)

    def make_plugin_usable(self, state = True):
        self._run_button.unusable = not state
        self._plugin.update_button(self._run_button)

    def build_menu(self):
        # create the layout node that contains select and run and refresh
        self.ln_select_run = menu.root.find_node("Refresh Run",True)

        # create the Run button
        self._run_button = menu.root.find_node("Run", True).get_content()
        self._run_button.register_pressed_callback(run_button_pressed_callback)

        # create the Clear button
        refresh_button = menu.root.find_node("Clear", True).get_content()
#        refresh_button.register_pressed_callback(clear_button_pressed_callback)


        self._menu = menu
        
