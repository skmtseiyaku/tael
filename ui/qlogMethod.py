import tkinter as tk
import tkcalendar
from tkinter import ttk
from ctypes import windll

def qlogTest():
    return "interface.qlog is called"

class qlog:
    def __init__(self, root):
        self.root = root
        self.root.title("Quick Log")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        windll.shcore.SetProcessDpiAwareness(1)
        #scaleFactor = windll.shcore.GetScaleFactorForDevice(0) / 100
        #root.tk.call('tk', 'scaling', scaleFactor)

    
    def submit(self, text_input, date_input):

    def submit(self):

    def show(self):

    def start(self):
