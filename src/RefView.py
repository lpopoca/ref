#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from RefController import *
import datetime as dt

app_controller = RefController()

class RefView(tk.Frame):
    def __init__(self, app_controller, file_name = None):
        self.controller = app_controller
        self.window = tk.Tk()
        self.window.title("Reference Entry Finder")
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
        self.note_text.grid(row=1, column=0)
        # - - - - - - - - - - - - - - - - - - - - -
        # Date label
        self.date_var = tk.StringVar()
        self.date_label = tk.Label(self.frame1, textvariable=self.      date_var)
        self.date_label.grid(row=1, column=0)        

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
        """Load in a json file that holds reference entries"""
        model = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
        filetypes = (("all files", "*.*"), ("Text files", "*.txt*")))
        self.file_name = model
        self.controller.load_file(model)

    def new_entry(self):
        """Creates a new entry in the dictionary"""
        ref_num = self.reference_number_entry.get()
        ref_num_str = str(ref_num)
        date = dt.datetime.today()
        note = str(self.note_text.get(1.0, "end-1c"))
        self.controller.new_entry(ref_num, ref_num_str, date, note)
        self.note_text.delete(1.0, "end")
        self.reference_number_entry.delete(0, "end")

    def find(self):
        """Finds an entry using the reference number"""
        ref_num = self.reference_number_entry.get()
        date, note = self.controller.read_entry(ref_num)
        self.note_text.delete(1.0, "end")
        self.date_var.set("Last Modified: " + str(date))
        self.note_text.insert(0.1, note)
        self.date_label(text=date)

    def save(self):
        """Saves the reference dictionary into a json file"""
        app_controller.print_dictionary()
        app_controller.save_file(self.file_name)

# Create the entire GUI program
program = RefView(app_controller)

# Start the GUI event loop
program.window.mainloop()