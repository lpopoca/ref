#!/usr/bin/env python3

import json

class RefController:
    """Controls the backend of Ref"""
    def __init__(self, ref_dict={}):
        self.ref_dict = ref_dict

    def read_entry(self, ref_num):
        """Reads an entry in the dictionary"""
        print(self.ref_dict[ref_num].items())
        return self.ref_dict[ref_num]["date"], self.ref_dict[ref_num]["note"]
        
    def new_entry(self, ref_num, ref_num_str, date, note):
        """Creates a new dictionary entry"""
        reference_number = ref_num
        reference_number_str = str(reference_number)
        reference_number = {'date' : date, 'note' : note}
        self.ref_dict[reference_number_str] = reference_number

    def load_file(self, file_name):
        """Loads a json file as a dictionary"""
        self.ref_dict = json.load(open(file_name))

    def save_file(self, file_name):
        """Saves the dictionary to the json file that is currently open"""
        j = json.dumps(self.ref_dict)
        with open(file_name, 'w') as f:
            f.write(j)
            f.close()

