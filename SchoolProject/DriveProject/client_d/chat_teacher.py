import tkinter
from tkinter import *
from tkinter import ttk, messagebox


class ChatTeacher(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('450x450+350+50')
        self.title('Chat Screen')
