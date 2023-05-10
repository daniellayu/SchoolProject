import tkinter
from tkinter import *
from tkinter import ttk, messagebox


class ChooseDays(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('500x500')
        self.title('Choose Days Screen')
