#!/usr/bin/env
from tkinter import filedialog
from tkinter import *
import tkinter as tk  # neede for window




def prompt_and_get_file_name():
    """prompt the user to open a file and return the file path of the file"""

    # TO DO: add other file types!!!!!!!!!!!!!!!!!!
    try:
        img_file_name =  filedialog.askopenfilename(
            initialdir = "/",
            title = "Select file",
            filetypes =
            (
                ("jpeg files","*.jpg"),  # still need jpEg!!!
                ("gif files", "*.gif"),
                ("png files", "*.png"),
                ("all", "*.*")
            ) # add more types: using tuple: ("description", "*.type")
        )
    except:
        print("Image file not able to be opened")
    # return name of selected file as string:
    return img_file_name
