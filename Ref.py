#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from RefBackend import *

reference_dictionary = {}
back = RefBackend(reference_dictionary)

class Ref(tk.Frame):
    def __init__(self, reference_dictionary, file_name = None):
        self.window = tk.Tk()
        self.window.title("Reference Entry Finder")
        self.dictionary = reference_dictionary
        self.file_name = file_name
        self.create_widgets()
        self.create_menubar()

    def create_widgets(self):
        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5
        # - - - - - - - - - - - - - - - - - - - - -
        # Frame1
        self.frame1 = ttk.Frame(self.window)
        self.frame1.grid(row=0, column=0, sticky=tk.W)              
        # - - - - - - - - - - - - - - - - - - - - -
        # Reference Number Label
        self.reference_number_label = ttk.Label(self.frame1, text="Reference Number:")
        self.reference_number_label.grid(row=0, column=0, padx=10)
        # - - - - - - - - - - - - - - - - - - - - -
        # Reference Number Entry
        self.reference_number_entry = ttk.Entry(self.frame1, textvariable="Enter A Reference Number")
        self.reference_number_entry.grid(row=0, column=1)
        # - - - - - - - - - - - - - - - - - - - - -
        # Find and New Buttons
        self.find_button = ttk.Button(self.frame1, text="Find")
        self.find_button.grid(row=0, column=2, padx=2)
        self.find_button["command"]=self.find
        # - - - - - - - - - - - - - - - - - - - - -
        self.new_button = ttk.Button(self.frame1, text="New")
        self.new_button.grid(row=0, column=3)
        self.new_button["command"]=self.new_entry
        # - - - - - - - - - - - - - - - - - - - - -
        # Frame2
        self.frame2 = ttk.Frame(self.window)
        self.frame2.grid(row=1, column=0, sticky=tk.W)
        # - - - - - - - - - - - - - - - - - - - - -
        # Note text field
        self.note_text = tk.Text(self.frame2)
        self.note_text.grid(row=1, column=1)

    def create_menubar(self):
        # - - - - - - - - - - - - - - - - - - - - -
        # create a toplevel menu
        self.menubar = tk.Menu(self.window)
        # - - - - - - - - - - - - - - - - - - - - -
        # create a pulldown menu, and add it to the menu bar
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Open", command=self.open)
        self.filemenu.add_command(label="Save", command=self.save)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.window.quit)
        # - - - - - - - - - - - - - - - - - - - - -
        # display the menu
        self.window.config(menu=self.menubar)

    def open(self):
        jsonfile = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
        filetypes = (("all files", "*.*"), ("Text files", "*.txt*")))
        self.file_name = jsonfile
        self.dictionary = back.load_file(jsonfile)


    def new_entry(self):
        ref_num = self.reference_number_entry.get()
        note = self.note_text.get(1.0, "end-1c")
        RefBackend.new_entry(self, self.dictionary, ref_num, note)
        self.note_text.insert(1.0, note)

    def find(self):
        ref_num = self.reference_number_entry.get()
        note = RefBackend.read_entry(self, self.dictionary, ref_num)
        self.note_text.delete(1.0, "end")
        self.note_text.insert(0.1, note)

    def save(self):
        print("stub")
        #back.save_file(self.dictionary)

# Create the entire GUI program
program = Ref(reference_dictionary)

# Start the GUI event loop
program.window.mainloop()

""" empty_dict = {}
back = RefBackend(empty_dict)

def display_note(ref_num):
    self.ref_num = ref_num
    note = back.read_entry(back.ref_dict, ref_num)

def open():
    jsonfile = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
    filetypes = (("all files", "*.*"), ("Text files", "*.txt*")))
    back.load_file(jsonfile) """

