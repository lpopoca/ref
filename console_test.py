#!/usr/bin/env python3

def check_reference(ref_num, file_name):
    """Check to see if the reference number is an entry in the database"""
    with open(file_name) as f:
        line = f.readline().rstrip() #Remove the newline character
        entries = line.split("\t") #Create a list of different entries from the columns
        reference_number_entry = entries[:1]
        reference_number_str = str(reference_number_entry).strip("']['")
        if ref_num is reference_number_str:
            show_details(entries)
        else:
            print("not entry")

def show_details(entry_list):
        reference_number_entry = entry_list[:1]
        reference_number_str = str(reference_number_entry).strip("']['")
        phone_number_entry = entry_list[1:2]
        phone_number_str = str(phone_number_entry).strip("']['")
        note_entry = entry_list[2:3]
        note_str = str(note_entry).strip("']['")
        print(reference_number_str)
        print("phone number: " + phone_number_str + " " + "note: " + note_str)
        

def main():
    ref_file = 'reference_list.txt'
    reference_number = input("Enter a reference number: ")
    check_reference(reference_number, ref_file)

if __name__ == "__main__":
    main()


