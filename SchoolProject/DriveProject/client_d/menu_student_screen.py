import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from choose_teacher_screen import ChooseTeacher
from student_lessons_list_screen import StudentLessonsList
from insert_lesson_screen import InsertLesson


class MenuStudent(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        print(self.parent.parent.client_socket)
        self.geometry('400x400')
        self.title('Menu Student Screen')
        Label(self, text="Welcome student", bg="light gray").place(x=175, y=75)
        self.btn_c = Button(self, text="choose teacher", bg="light green", width=13, heigh=2,
                            command=self.open_choose_teacher).place(x=100, y=125)
        self.btn_l = Button(self, text="lessons", bg="light green", width=13, heigh=2,
                            command=self.open_student_lessons_list).place(x=250, y=125)
        self.btn_i = Button(self, text="insert lesson", bg="light green", width=13, heigh=2,
                             command=self.open_insert_lesson).place(x=150, y=225)
        self.btn_d = Button(self, text="delete lesson", bg="light green", width=13, heigh=2).place(x=150, y=225)
        self.btn_close = Button(self, text="Close", background="red", command=self.close).place(x=200, y=350)

    def open_choose_teacher(self):
        window = ChooseTeacher(self)
        window.grab_set()
        self.withdraw()

    def open_student_lessons_list(self):
        window = StudentLessonsList(self)
        window.grab_set()
        self.withdraw()

    def open_insert_lesson(self):
        window = InsertLesson(self)
        window.grab_set()
        self.withdraw()

    def close(self):
        self.parent.deiconify()
        self.destroy()

