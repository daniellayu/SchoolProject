import tkinter
from tkinter import *
from tkinter import messagebox
from SchoolProject.DriveProject.server_d.studentdb import StudentDb
from choose_teacher_screen import ChooseTeacher
import threading


class SignupStudent(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.studentDb = StudentDb()
        self.geometry('500x500')
        self.title('Sign up as student')
        Label(self, text="SIGN UP STUDENT", background="light blue").place(x=150, y=55)
        Label(self, text="first name").place(x=75, y=100)
        self.entry_fname = Entry(self)
        self.entry_fname.place(x=175, y=100)
        Label(self, text="last name").place(x=75, y=125)
        self.entry_lname = Entry(self)
        self.entry_lname.place(x=175, y=125)
        Label(self, text="email").place(x=75, y=150)
        self.entry_email = Entry(self)
        self.entry_email.place(x=175, y=150)
        Label(self, text="password").place(x=75, y=175)
        self.entry_password = Entry(self)
        self.entry_password.place(x=175, y=175)
        Label(self, text="phone number").place(x=75, y=200)
        self.entry_phonenumber = Entry(self)
        self.entry_phonenumber.place(x=175, y=200)
        Label(self, text="ID").place(x=75, y=225)
        self.entry_id = Entry(self)
        self.entry_id.place(x=175, y=225)
        self.btn_signup = Button(self, text="Sign up", background="purple", command=self.sign_up_student).place(x=150, y=300)
        self.btn_close = Button(self, text="close", background="red", command=self.close).place(x=150, y=350)

    def sign_up_student(self):
        print(self.entry_id.get())
        if (len(self.entry_id.get()) == 0) or (len(self.entry_password.get()) == 0):
            messagebox.showerror("error", "please write id and password")
            return False
        print("sign_up_student")
        arr = ["sign_up_student", self.entry_fname.get(), self.entry_lname.get(), self.entry_email.get(),
               self.entry_password.get(), self.entry_phonenumber.get(), self.entry_id.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.client_socket.send(str_insert.encode())
        data = self.parent.client_socket.recv(1024).decode()
        print(data)
        if data == "success Sign up student":
            messagebox.showinfo("showinfo", "your details have been successfully registered as a student")
            self.close()

    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.sign_up_student, args=())
        self.client_handler.daemon = True
        self.client_handler.start()


    def open_choose_teacher(self):
        window = ChooseTeacher(self)
        window.grab_set()
        self.withdraw()


    def close(self):
        self.parent.deiconify() #show parent
        self.destroy()# close and destroy this screen

