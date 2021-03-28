import nanome
from nanome.util import Logs
from nanome.util import Color

import copy
import re
import math
import numpy as np
import os
import json


class GlycamCBMenu():
    def __init__(self, plugin):
# import the json file of the new UI
        menu = nanome.ui.Menu.io.from_json(os.path.join(os.path.dirname(__file__), 'GlycamCB_pluginator.json'))
        self.plugin=plugin
        self.plugin.menu = menu

# layout node setup r(un)
        ln_btn_run = self.plugin.menu.root.find_node('RunButton')
        btn_run = ln_btn_run.get_content()
        btn_run.register_pressed_callback(self.test_run_print)
        
# layout node setup (clear) - doesn't do anything 
        ln_btn_clear = self.plugin.menu.root.find_node('ClearButton')
        btn_clear = ln_btn_clear.get_content()
        btn_clear.register_pressed_callback(self.test_clear_print)

        self.plugin.update_menu(self.plugin.menu)

    def test_run_print(self,button):
#        print("running - button")
        # get sequence from menu
        ln_text_sequence = self.plugin.menu.root.find_node('sequence')
        self.text_sequence = ln_text_sequence.get_content().input_text
#        print(self.text_sequence)
        # get user specified molecule name from menu - didnt remove spaces
        ln_text_molecule_name = self.plugin.menu.root.find_node('molecule_name')
        self.molecule_name = ln_text_molecule_name.get_content().input_text
#        print(self.molecule_name)

# check GlycamCB json script
# api json file with sequence
#        self.plugin.json_request=nanome.api.ui.io.layout_node_io.from_json(os.path.join(os.path.dirname(__file__))+'/build_sequence.txt')
#        self.json_request = json.loads(open(os.path.join(os.path.dirname(__file__),'build_sequence.txt')).read())
#        for (k, v) in self.json_request.items():
#           print("Key: " + k)
#           print("Value: " + str(v))

#  little odd - parse json scripts instead
# change input script build_no_sequence for glycam.org
        self.file1 = open(os.path.join(os.path.dirname(__file__),'build_no_sequence.txt'))
        self.seq_file=self.file1.read()
        self.file1.close()

# new input script with molecular sequence
        self.new_seq_file=self.seq_file.replace("no_sequence",self.text_sequence)
        self.file2=open(os.path.join(os.path.dirname(__file__),'build_'+self.text_sequence)+'.txt','w')
        self.file2.write(self.new_seq_file)
        self.file2.close()
#        print(self.new_seq_file)

# send to glycam via bash

        self.command='bash api-https.bash test.glycam.org build_'+self.text_sequence+'.txt'
#        print(self.command)
        os.system(self.command)

# parse .Response.json file 'build_'+text_sequence+'.txt.Response.json
#  for URL of pdb file - starts at url_loc+15 and ends at next "
# url is self.url

# check parse - use this and comment out 4 lines below
#        self.file3=open(os.path.join(os.path.dirname(__file__),'test.json.Response.json'))

# real parse
        self.file3 = open(os.path.join(os.path.dirname(__file__),'build_'+self.text_sequence+'.txt.Response.json'))
        self.rcvd_file=self.file3.read()
        self.url_loc=self.rcvd_file.find("downloadUrl")
        self.url_end_loc=self.rcvd_file.find("\"",self.url_loc+15)
#        print(self.url_loc+15)
#        print(self.url_end_loc)
        self.url=self.rcvd_file[self.url_loc+15:self.url_end_loc]
#        print(self.url)
        self.file3.close()

# download the pdb file at url with usr name
#  curl -L -o self.molecule_name self.url
#  pdb file is stored in molecule_name.pdb file

#        if self.url_loc>0 and self.url_end_loc>0:
            self.command='curl -L -o '+self.molecule_name+'.pdb '+self.url
            print(self.command)
            os.system(self.command)
#        else:
#            print("rcvd_file is empty")

### add to Nanome entry list - molecule_name.pdb

#        self.add_to_workspace('molecule.pdb')


### now quit plugin

###      quit plugin with message to user in menu on completion status
   
    def test_clear_print(self,button):
        print("test clear button")
        


# not used
    
    def _on_run(self,button):
        print("test button")

    def _request_refresh(self):
        self._plugin.request_refresh()

    def update_button(self, button):
        self.update_content(button)

    def make_plugin_usable(self):
        self.menu.make_plugin_usable()
  
