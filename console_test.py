#!/usr/bin/env python3

def search_ref_list(user_num, file_name):
    """Checks the reference list to see if the user's reference number is in
    the text file."""
    with open(file_name) as f:
        # The for-else loop reads each line and checks if the reference number
        # is in the list
        for line in f:
            new_line = line.rstrip() # Strips the newline char
            entries = new_line.split("\t") # Separates the entries
            reference_number_entry = entries[:1] # The first column is the reference number
            reference_number_str = str(reference_number_entry).strip("']['")
            if is_ref_num(user_num, reference_number_str):
                show_details(entries)
                break
        # If there is no more data to read then the end of file has been reached
        # and the reference number was not located.
        else: 
            print("Reference number not located in the file.")

def is_ref_num(user_num, ref_num):
    """Check to see if the reference number is an entry in the database"""
    if user_num == ref_num:
        return True
    else:
        return False

def show_details(entry_list):
    """Shows the details related to the reference number?"""
    reference_number_entry = entry_list[:1] # The first slice is the reference number
    reference_number_str = str(reference_number_entry).strip("']['") # a string is easier for us to use.
    phone_number_entry = entry_list[1:2]
    phone_number_str = str(phone_number_entry).strip("']['")
    note_entry = entry_list[2:3]
    note_str = str(note_entry).strip("']['")
    print(reference_number_str)
    print("phone number: " + phone_number_str + " " + "note: " + note_str)
    

def main():
    """The main function"""
    ref_file = 'reference_list.txt'
    reference_number = input("Enter a reference number: ")
    search_ref_list(reference_number, ref_file)

if __name__ == "__main__":
    main()