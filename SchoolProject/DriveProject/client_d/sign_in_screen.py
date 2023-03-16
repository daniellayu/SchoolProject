import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from DriveProject.server_d.teacherdb import TeacherDb
from DriveProject.server_d.studentdb import StudentDb
import threading
from menu_teacher_screen import MenuTeacher
from menu_student_screen import MenuStudent


class SignInScreen(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.id_s = "0"
        self.id_t = "0"
        self.teacherdb = TeacherDb()
        self.studentdb = StudentDb()
        self.geometry('400x400')
        self.title('Signin')
        Label(self, text="SIGN IN", background="light blue").place(x=170, y=75)
        Label(self, text="ID", background="light blue").place(x=75, y=150)
        self.entry_id = Entry(self)
        self.entry_id.place(x=150, y=150)
        Label(self, text="Password", background="light blue").place(x=75, y=200)
        self.entry_password = Entry(self, show='*')
        self.entry_password.place(x=150, y=200)
        self.radio = IntVar()
        self.trb = Radiobutton(self, text="teacher", value=1, variable=self.radio).place(x=100, y=250)
        self.srb = Radiobutton(self, text="student", value=2, variable=self.radio).place(x=200, y=250)
        self.btn_signin = Button(self, text="Sign in", background="light pink", command=self.sign_in).place(x=170, y=275)
        self.btn_close = Button(self, text="Close", background="red", command=self.close)
        self.btn_close.place(x=170, y=325)


    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.sign_in, args=())
        self.client_handler.daemon = True
        self.client_handler.start()


    def sign_in(self):
        if (len(self.entry_id.get()) == 0) and (len(self.entry_password.get()) == 0):
            messagebox.showerror("error", "please write id and password")
            return
        print("sign in", self.radio.get())
        if self.radio.get() == 1:
            arr = ["sign_in_teacher", self.entry_id.get(), self.entry_password.get()]
            str_insert = ",".join(arr)
            print(str_insert)
            self.parent.client_socket.send(str_insert.encode())#sending line 41
            data = self.parent.client_socket.recv(1024).decode()#recived success or failed
            print(data)
            self.id_t = self.entry_id.get()
            if data == "success Sign in":
                self.open_menu_teacher_screen()
            if data == "failed Sign in":
                messagebox.showerror("error", "teacher not exist, please sign up")
        if self.radio.get() == 2:
            arr = ["sign_in_student", self.entry_id.get(), self.entry_password.get()]
            str_insert = ",".join(arr)
            print(str_insert)
            self.parent.client_socket.send(str_insert.encode())
            data = self.parent.client_socket.recv(1024).decode()#recived success or failed
            print(data)
            self.id_s = self.entry_id.get()
            if data == "success Sign in":
                self.open_menu_student_screen()
            if data == "failed Sign in":
                messagebox.showerror("error", "student not exist, please sign up")


    def open_menu_teacher_screen(self):
        window = MenuTeacher(self)
        window.grab_set()
        self.withdraw()


    def open_menu_student_screen(self):
        window = MenuStudent(self)
        window.grab_set()
        self.withdraw()


    def close(self):
        self.parent.deiconify()
        self.destroy()
