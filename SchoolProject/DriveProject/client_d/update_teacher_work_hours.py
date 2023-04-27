import tkinter
from tkinter import *
from tkinter import ttk, messagebox

class UpdateTeacherWorkTime(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x400')
        self.title('Update Teacher Work Time')
        Label(self, text="in which days can you work?").place(x=250, y=35)
        self.check_var1 = IntVar()
        self.check_var2 = IntVar()
        self.check_var3 = IntVar()
        self.check_var4 = IntVar()
        self.check_var5 = IntVar()
        self.check_var6 = IntVar()

        self.c1 = Checkbutton(self, text="sunday", variable=IntVar(), height=5, width=20)
        self.c2 = Checkbutton(self, text="monday", variable=self.check_var2, height=5, width=20)
        self.c3 = Checkbutton(self, text="tuesday", variable=self.check_var3, height=5, width=20)
        self.c4 = Checkbutton(self, text="wednesday", variable=self.check_var4, height=5, width=20)
        self.c5 = Checkbutton(self, text="thursday", variable=self.check_var5, height=5, width=20)
        self.c6 = Checkbutton(self, text="friday", variable=self.check_var6, height=5, width=20)

