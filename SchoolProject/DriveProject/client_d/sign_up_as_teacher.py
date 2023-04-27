import tkinter
from tkinter import *
from SchoolProject.DriveProject.server_d.teacherdb import TeacherDb
from tkinter import messagebox
import threading


class SignUpTeacher(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.teacherDb = TeacherDb()
        self.geometry('500x500')
        self.title('Sign up as teacher')
        Label(self, text="SIGN Up Teacher", background="light blue").place(x=150, y=30)
        Label(self, text="first name:").place(x=50, y=60)
        self.entry_fname = Entry(self)
        self.entry_fname.place(x=50, y=80)
        Label(self, text="last name:").place(x=50, y=110)
        self.entry_lname = Entry(self)
        self.entry_lname.place(x=50, y=130)
        Label(self, text="email:").place(x=50, y=160)
        self.entry_email = Entry(self)
        self.entry_email.place(x=50, y=180)
        Label(self, text="password:").place(x=50, y=210)
        self.entry_password = Entry(self)
        self.entry_password.place(x=50, y=230)
        Label(self, text="phone number:").place(x=50, y=260)
        self.entry_phonenumber = Entry(self)
        self.entry_phonenumber.place(x=50, y=280)
        Label(self, text="ID").place(x=50, y=310)
        self.entry_id = Entry(self)
        self.entry_id.place(x=50, y=330)
        Label(self, text="price:").place(x=50, y=360)
        self.entry_price = Entry(self)
        self.entry_price.place(x=50, y=380)
        Label(self, text="experience:").place(x=50, y=410)
        self.entry_experience = Entry(self)
        self.entry_experience.place(x=50, y=430)
        self.btn_signup = Button(self, text="Sign up", background="purple", command=self.sign_up_teacher).place(x=100, y=470)
        self.btn_close = Button(self, text="close", background="red", command=self.close).place(x=150, y=470)


    def sign_up_teacher(self):
        print(self.entry_id.get())
        if (len(self.entry_id.get()) == 0) or (len(self.entry_password.get()) == 0):
            messagebox.showerror("error", "please write id and password")
            return False
        print("sign_up_teacher")
        arr = ["sign_up_teacher", self.entry_fname.get(), self.entry_lname.get(), self.entry_email.get(), self.entry_password.get(), self.entry_phonenumber.get(), self.entry_id.get(), self.entry_price.get(), self.entry_experience.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.client_socket.send(str_insert.encode())
        data = self.parent.client_socket.recv(1024).decode()
        print(data)
        if data == "success Sign up teacher":
            messagebox.showinfo("showinfo", "your details have been successfully registered as a teacher")
            self.close()

    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.sign_up_teacher, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    # def open_opening_screen(self):
    #     window = OpeningScreen(self)
    #     window.grab_set()
    #     self.withdraw()


    def close(self):
        self.parent.deiconify()
        self.destroy()
