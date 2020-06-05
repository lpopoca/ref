#!/usr/bin/env python3

def read_entry(ref_dict, ref_num,):
    print(ref_dict)
    
def create_ref(ref_dict, ref_num, reference_number_str, date, note):
    ref_num = {'date' : date, 'note' : note}
    ref_dict["reference number: " + reference_number_str] = ref_num
    return ref_dict

def new_entry(reference_dictionary):
    reference_number = input("Enter reference number: ")
    reference_number_str = str(reference_number)
    date = input("Enter date: ")
    note = input("Enter note: ")
    create_ref(reference_dictionary,reference_number, reference_number_str, date, note)

def menu(ref_dict):
    choice = input("Enter 1 to create new entry\n2 to read an entry\n0 to quit: ")
    if choice == '1':
        new_entry(ref_dict)
        menu(ref_dict)
    elif choice == '2':
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