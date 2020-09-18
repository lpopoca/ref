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
        self.window.resizable(False, False)

    def create_widgets(self):
        """Creates the widgets for the application"""
        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

        # Frame1
        self.frame1 = ttk.Frame(self.window)
        self.frame1.grid(row=0, column=0, sticky=tk.W)           

        # Reference Number Label
        self.reference_number_label = ttk.Label(self.frame1, text="Reference Number:")
        self.reference_number_label.grid(row=0, column=0, sticky=tk.W)

        # Reference Number Entry
        self.reference_number_entry = ttk.Entry(self.frame1)
        self.reference_number_entry.grid(row=0, column=1)

        # Find and New Buttons
        self.find_button = ttk.Button(self.frame1, text="Find")
        self.find_button.grid(row=0, column=2, padx=2)
        self.find_button["command"]=self.find
        self.new_button = ttk.Button(self.frame1, text="Enter")
        self.new_button.grid(row=0, column=3)
        self.new_button["command"]=self.new_entry

        # Date label
        self.date_var = tk.StringVar()
        self.date_label = tk.Label(self.frame1, textvariable=self.date_var)
        self.date_label.grid(row=1, column=0, sticky=tk.W)                

        # Frame2
        self.frame2 = ttk.Frame(self.window)
        self.frame2.grid(row=1, column=0, sticky=tk.W)       

        # Note text scrollbar
        self.scrollbar = ttk.Scrollbar(self.frame2)
        self.scrollbar.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E)        

        # Note text field
        self.note_text = tk.Text(self.frame2, yscrollcommand=self.scrollbar.set, undo=True)
        self.note_text.grid(row=0, column=0)

        # Configure Scroll bar so that it has a slider.
        self.scrollbar.config(command=self.note_text.yview)           

    def create_menubar(self):

        # create a toplevel menu
        self.menubar = tk.Menu(self.window)

        # create a pulldown menu, and add it to the menu bar
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Open", command=self.open)
        self.filemenu.add_command(label="Save", command=self.save)
        self.filemenu.add_command(label="Save as", command=self.save_as)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.window.quit)

        # create a pulldown menu, and add it to the menu bar
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.editmenu.add_command(label="Undo", command=self.stub)
        self.editmenu.add_command(label="Redo",command=self.stub)
        
        # display the menu
        self.window.config(menu=self.menubar)

    def open(self):
        """Load in a json file that holds reference entries"""
        ref_file = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
        filetypes = (("JSON files", "*.json*"), ("All files", "*.*")))
        self.file_name = ref_file
        self.controller.load_file(ref_file)

    def save_as(self):
        """Save the current reference dictionary into a json file"""
        ref_file = filedialog.asksaveasfilename(initialdir = "/", title = "Select a File", filetypes=(("JSON files", "*.json*"),("All files", "*.*")))
        self.file_name = ref_file
        self.controller.save_file(self.file_name)            

    def save(self):
        """Saves the reference dictionary into a json file"""
        self.controller.save_file(self.file_name)
    
    def new_entry(self):
        """Creates a new entry in the dictionary"""
        ref_num = self.reference_number_entry.get()
        ref_num_str = str(ref_num)
        date = dt.date.today()
        note = str(self.note_text.get(1.0, "end-1c"))
        self.controller.new_entry(ref_num, ref_num_str, date, note)
        self.note_text.delete(1.0, "end")
        self.reference_number_entry.delete(0, "end")
        self.date_var.set("")

    def find(self):
        """Finds an entry using the reference number"""
        ref_num = self.reference_number_entry.get()
        date, note = self.controller.read_entry(ref_num)
        self.note_text.delete(1.0, "end")
        self.date_var.set("Last Modified: " + str(date))
        self.note_text.insert(0.1, note)        

    def stub(self):
        """A stub function to test a widgets functionality."""
        pass

# Create the entire GUI program
program = RefView(app_controller)

# Start the GUI event loop
program.window.mainloop()