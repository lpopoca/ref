#!/usr/bin/env python3
import json

def read_entry(ref_dict, ref_num):
    print(str(ref_num))
    print(ref_dict[ref_num])
    
def create_ref(ref_dict, ref_num, reference_number_str, date, note):
    ref_num = {'date' : date, 'note' : note}
    ref_dict[reference_number_str] = ref_num
    return ref_dict

def new_entry(reference_dictionary):
    reference_number = input("Enter reference number: ")
    reference_number_str = str(reference_number)
    date = input("Enter date: ")
    note = input("Enter note: ")
    create_ref(reference_dictionary,reference_number, reference_number_str, date, note)

def load_file(file_name):
    ref_dict = json.load(open(file_name))
    menu(ref_dict)

def save_file(file_name, ref_dict):
    j = json.dumps(ref_dict)
    with open(file_name, 'w') as f:
        f.write(j)
        f.close()
    return ref_dict

def menu(ref_dict):
    print("Enter a choice: ", end = "")
    choice = input("""
    1: Load a dictionary file
    2: Save dictionary file
    3: Create a new entry
    4: Read a reference entry
    0: to quit.
    Enter ----> """)
    if choice == '1':
        # Load a dictionary file
        file_name = input("Enter file name: ")
        file_name = file_name + ".json"
        load_file(file_name)
        menu(ref_dict)
    elif choice == '2':
        # Save a dictionary file
        file_name = input("Enter a file name: ")
        file_name = file_name + ".json"
        save_file(file_name, ref_dict)
        menu(ref_dict)
    elif choice == '3':
        new_entry(ref_dict)
        menu(ref_dict)
    elif choice == '4':
        reference_number = input("Enter a reference number: ")
        read_entry(ref_dict, reference_number)
        menu(ref_dict)
    if choice == '0':
        exit() 

def main():
    """The main function"""
    reference_dictionary = {}
    menu(reference_dictionary)

if __name__ == "__main__":
    main()