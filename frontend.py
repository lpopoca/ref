import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import backend

def my_command():
    print("hello")

def load():
    jsonfile = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
    filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    backend.load_file(jsonfile)
    
application_window = tk.Tk()

application_window.title("Reference Entry Finder")

#Menubar
menubar = Menu(application_window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=my_command)
filemenu.add_command(label="Open", command=load)
filemenu.add_command(label="Save", command=my_command)
filemenu.add_command(label="Save as...", command=my_command)
filemenu.add_command(label="Close", command=my_command)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=application_window.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=my_command)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=my_command)
editmenu.add_command(label="Copy", command=my_command)
editmenu.add_command(label="Paste", command=my_command)
editmenu.add_command(label="Delete", command=my_command)
editmenu.add_command(label="Select All", command=my_command)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=my_command)
helpmenu.add_command(label="About...", command=my_command)
menubar.add_cascade(label="Help", menu=helpmenu)
application_window.config(menu=menubar)

#Application
reference_entry_label = ttk.Label(application_window, text="Reference Number:")
reference_entry_label.grid(row=0, column=0)

reference_entry = ttk.Entry(application_window)
reference_entry.grid(row=0, column=1, columnspan=3, sticky=tk.W + tk.E)

reference_button = ttk.Button(application_window, text="Find")
reference_button.grid(row=0, column=4)
reference_button['command'] = my_command

note_label = ttk.Label(application_window, text="Note:")
note_label.grid(row=1, column=0, sticky=tk.N + tk.W)

note_text_field = tk.Text(application_window)
note_text_field.grid(row=1, column=1, columnspan=3)

application_window.mainloop()