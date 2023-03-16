import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar



class LastLessons(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        print(self.parent.parent.parent.id_t)
        self.geometry('700x400')
        self.title('Last Lessons Screen')
        self.cal = Calendar(self, selectmode='day', data_pattern='d/m/yy')
        self.date = self.cal.get_date()
        print(self.date)
