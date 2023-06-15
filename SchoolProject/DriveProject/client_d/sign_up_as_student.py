import tkinter
from tkinter import *
from tkinter import messagebox
from choose_teacher_screen import ChooseTeacher
import threading


class SignupStudent(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('500x500+350+50')
        self.title('Sign up as student')

        Label(self, text="SIGN UP STUDENT", fg="#57a1f8", font=('Microsoft YaHei UI Light', 23, 'bold')).place(x=125, y=30)

        Label(self, text="first name:", fg="black", font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=75, y=100)
        self.entry_fname = Entry(self, width=25, fg='black', font=('Microsoft YaHei UI Light', 11))
        self.entry_fname.place(x=200, y=100)

        Label(self, text="last name:", fg="black", font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=75, y=150)
        self.entry_lname = Entry(self, width=25, fg='black', font=('Microsoft YaHei UI Light', 11))
        self.entry_lname.place(x=200, y=150)

        Label(self, text="email:", fg="black", font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=75, y=200)
        self.entry_email = Entry(self, width=25, fg="black", font=('Microsoft YaHei UI Light', 11))
        self.entry_email.place(x=200, y=200)

        Label(self, text="password:", fg="black", font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=75, y=250)
        self.entry_password = Entry(self, width=25, fg="black", font=('Microsoft YaHei UI Light', 11))
        self.entry_password.place(x=200, y=250)

        Label(self, text="phone number:", fg="black", font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=75, y=300)
        self.entry_phonenumber = Entry(self, width=25, fg="black", font=('Microsoft YaHei UI Light', 11))
        self.entry_phonenumber.place(x=200, y=300)

        Label(self, text="ID:", fg="black", font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=75, y=350)
        self.entry_id = Entry(self, width=25, fg="black", font=('Microsoft YaHei UI Light', 11))
        self.entry_id.place(x=200, y=350)

        self.btn_signup = Button(self, text="Sign up", fg='white', bg='#57a1f8',
                                 font=('Microsoft YaHei UI Light', 11, 'bold'), command=self.sign_up_student).place(x=185, y=400)

        self.btn_close = Button(self, text="go back", background="red", command=self.close).place(x=370, y=470)

    def sign_up_student(self):
        print(self.entry_id.get())
        if (len(self.entry_id.get()) == 0) or (len(self.entry_password.get()) == 0):
            messagebox.showerror("error", "please write id and password")
            return False
        # arr1 = ["check_id", self.entry_id.get()]
        # str_check = ",".join(arr1)
        # self.parent.send_msg(str_check, self.parent.client_socket)
        # data1 = self.parent.recv_msg(self.parent.client_socket)
        # if data1:
        #     messagebox.showerror("error", "student already exists")
        print("sign_up_student")
        arr = ["sign_up_student", self.entry_fname.get(), self.entry_lname.get(), self.entry_email.get(),
               self.entry_password.get(), self.entry_phonenumber.get(), self.entry_id.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.send_msg(str_insert, self.parent.client_socket)
        data = self.parent.recv_msg(self.parent.client_socket)
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

