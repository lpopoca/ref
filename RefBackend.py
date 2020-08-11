#!/usr/bin/env python3

import json

class RefBackend:
    """Controls the backend of Ref"""
    def __init__(self, init_ref_dict):
        self.ref_dict = init_ref_dict

    def read_entry(self, ref_dict, ref_num):
        print(ref_dict[ref_num].items())
        return ref_dict[ref_num]["note"]

        
    def create_ref(self, ref_dict, ref_num, reference_number_str, date, note):
        ref_num = {'date' : date, 'note' : note}
        ref_dict[reference_number_str] = ref_num
        return ref_dict

    def new_entry(self, reference_dictionary, ref_num, ref_note):
        reference_number = ref_num
        reference_number_str = str(reference_number)
        note = input("Enter note: ")
        create_ref(reference_dictionary,reference_number, reference_number_str, date, note)

    def load_file(self, file_name):
        """Loads a json file as a dictionary"""
        ref_dict = json.load(open(file_name))
        return ref_dict

    def save_file(self, file_name, ref_dict):
        j = json.dumps(ref_dict)
        with open(file_name, 'w') as f:
            f.write(j)
            f.close()
        return ref_dict
