import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from SchoolProject.DriveProject.server_d.teacherdb import TeacherDb
from SchoolProject.DriveProject.server_d.studentdb import StudentDb
import threading
#from menu_teacher_screen import MenuTeacher
#from menu_student_screen import MenuStudent
from lessons_list_screen import LessonsList
from student_lessons_list_screen import StudentLessonsList


class SignInScreen(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.id_s = "0"
        self.id_t = "0"
        self.teacherdb = TeacherDb()
        self.studentdb = StudentDb()
        self.geometry('500x500+350+50')
        self.title('Signin')
        #self.config(bg="#57a1f8")

        Label(self, text="SIGN IN", fg="#57a1f8", font=('Microsoft YaHei UI Light', 23, 'bold')).place(x=185, y=75)

        Label(self, text="ID:", fg="black", font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=150, y=150)
        self.entry_id = Entry(self, width=25, fg='black', bg='#57a1f8', border=0, font=('Microsoft YaHei UI Light', 11))
        self.entry_id.place(x=150, y=175)

        Label(self, text="Password:", fg="black", font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=150, y=235)
        self.entry_password = Entry(self, show='*', width=25, fg='black', bg='#57a1f8', border=0, font=('Microsoft YaHei UI Light', 11))
        self.entry_password.place(x=150, y=260)

        self.radio = IntVar()
        self.trb = Radiobutton(self, text="teacher", fg='#57a1f8', font=('Microsoft YaHei UI Light', 11, 'bold'),
                               value=1, variable=self.radio).place(x=150, y=310)
        self.srb = Radiobutton(self, text="student", fg='#57a1f8', font=('Microsoft YaHei UI Light', 11, 'bold'),
                               value=2, variable=self.radio).place(x=250, y=310)

        self.btn_signin = Button(self, text="Sign in", fg='white', bg='#57a1f8',
                                 font=('Microsoft YaHei UI Light', 11, 'bold'), command=self.sign_in).place(x=185, y=400)

        self.btn_close = Button(self, text="Close", background="red", command=self.close)
        self.btn_close.place(x=185, y=450)


    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.sign_in, args=())
        self.client_handler.daemon = True
        self.client_handler.start()


    def sign_in(self):
        if (len(self.entry_id.get()) == 0) and (len(self.entry_password.get()) == 0):
            messagebox.showerror("error", "please write id and password")
            return
        print("sign in", self.radio.get())
        if self.radio.get() == 0:
            messagebox.showerror("error", "please choose if you tea")
        if self.radio.get() == 1:
            arr = ["sign_in_teacher", self.entry_id.get(), self.entry_password.get()]
            str_insert = ",".join(arr)
            print(str_insert)
            self.parent.send_msg(str_insert, self.parent.client_socket)
            data = self.parent.recv_msg(self.parent.client_socket)
            #self.parent.client_socket.send(str_insert.encode())#sending line 41
            #data = self.parent.client_socket.recv(1024).decode()#recived success or failed
            print(data)
            self.id_t = self.entry_id.get()
            if data == "success Sign in":
                self.open_teacher_lessons_screen()
            if data == "failed Sign in":
                messagebox.showerror("error", "teacher not exist, please sign up")
        if self.radio.get() == 2:
            arr = ["sign_in_student", self.entry_id.get(), self.entry_password.get()]
            str_insert = ",".join(arr)
            print(str_insert)
            self.parent.send_msg(str_insert, self.parent.client_socket)
            data = self.parent.recv_msg(self.parent.client_socket)#recived success or failed
            print(data)
            self.id_s = self.entry_id.get()
            if data == "success Sign in":
                self.open_student_lessons_screen()
            if data == "failed Sign in":
                messagebox.showerror("error", "student not exist, please sign up")


    def open_teacher_lessons_screen(self):
        window = LessonsList(self)
        window.grab_set()
        self.withdraw()


    def open_student_lessons_screen(self):
        window = StudentLessonsList(self)
        window.grab_set()
        self.withdraw()


    def close(self):
        self.parent.deiconify()
        self.destroy()
