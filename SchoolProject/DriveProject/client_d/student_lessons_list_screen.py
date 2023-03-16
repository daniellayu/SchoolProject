import tkinter
from tkinter import *
from tkinter import ttk, messagebox


class StudentLessonsList(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        print(self.parent.parent.client_socket)
        self.geometry('400x400')
        self.title('Student Lessons List Screen')
