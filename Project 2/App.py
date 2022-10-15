from ast import arg
import queue
import threading
from queue import Queue
import tkinter as tk
import customtkinter
import sys, os
import time
script_dir = r"C:\Users\bmahabir\Desktop\EC601\Project 2"
sys.path.append(os.path.abspath(script_dir))
import backend_tester as be

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
class Twitter_App:
    '''INSTANTIATION'''
    def __init__(self, root):
        # initialize the application
        self.root = root
        self.root.title("Twitter Api Analysis Tool")
        self.root.geometry("620x400")


        # global variables
        self.filepath = ''
        self.window = 1

        '''LABELS'''
        # labels for the program title
        self.title_label = customtkinter.CTkLabel(root, text="Twitter Adult Content Checker", text_font=("Helvetica", 20))
        self.title_label.grid(row=0, column=0, padx=10,pady=15, sticky=tk.N)

        self.label_info = customtkinter.CTkLabel(root, text="", text_font=("Helvetica", 12), fg_color=("white", "gray38"), corner_radius=6, height=100)
        self.label_info.grid(column=0, row=3, sticky="nwe", padx=15, pady=15)

        self.progressbar = customtkinter.CTkProgressBar(root, mode='indeterminate')
        self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

        '''BUTTONS'''
        # button to get the path of the data csv file
        self.file_btn = customtkinter.CTkButton(root, text="Enter Twitter Handle", text_font=("Arial", 14), command = self.backend, borderwidth=2, relief="raised")
        self.file_btn.grid(row=2, column=0, columnspan=3, padx=20, pady=20, sticky=tk.N+tk.W)

        '''ENTRY FIELDS'''
        # entry field to display path for data csv file
        self.file_entry = customtkinter.CTkEntry(root, width=320)
        self.file_entry.grid(row=2, column=0, columnspan=3, padx=250, pady=20, sticky=tk.N+tk.W)

    def backend(self):
        self.progressbar.start()
        handle = self.file_entry.get()
        result = be.backend(handle)
        self.label_info.config(text = result)
        self.progressbar.stop()

    
root = customtkinter.CTk()
gui = Twitter_App(root)
root.mainloop()

# @Brian96203980