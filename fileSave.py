from tkinter import filedialog
from tkinter import *
import tkinter as tk
__name__ = "Griff Wood"
__version__ = "2.5"
"""Gets the selected Path from user"""
def get_dir():
    ''' Asks user to choose a location
    :return: Selected File Path as String
    '''
    root = tk.Tk()
    root.withdraw()
    dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    return dirname

