import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from students_list_screen import StudentsList
from lessons_list_screen import LessonsList
from update_details_screen import UpdateDetails
import threading


class MenuTeacher(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        print(self.parent.parent.client_socket)
        self.geometry('400x400')
        self.title('Menu Teacher Screen')
        Label(self, text="Welcome teacher", bg="light gray").place(x=175, y=75)
        self.btn_s = Button(self, text="student's list", bg="light green", width=13, heigh=2, command=self.open_students_list).place(x=100, y=125)
        self.btn_l = Button(self, text="lessons", bg="light green", width=13, heigh=2, command=self.open_lessons_list).place(x=250, y=125)
        self.btn_ud = Button(self, text="update details", bg="light green", width=13, heigh=2, command=self.open_update_details).place(x=150, y=225)
        self.btn_close = Button(self, text="Close", background="red", command=self.close).place(x=200, y=350)

    def open_students_list(self):
        window = StudentsList(self)
        window.grab_set()
        self.withdraw()

    def open_lessons_list(self):
        window = LessonsList(self)
        window.grab_set()
        self.withdraw()

    def open_update_details(self):
        window = UpdateDetails(self)
        window.grab_set()
        self.withdraw()

    def close(self):
        self.parent.deiconify()
        self.destroy()