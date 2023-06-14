import socket
import threading
import tkinter
from tkinter import *
from sign_in_screen import SignInScreen
from sign_up_as_teacher import SignUpTeacher
from sign_up_as_student import SignupStudent
from PIL import ImageTk, Image

SIZE = 12


class OpeningScreen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x550+350+50')
        self.title('Opening Screen')
        self.config(bg="mint cream")

        self.img = Image.open('C://Users//danie//PycharmProjects//pythonProject//wheel.png')
        self.resized = self.img.resize((300, 275), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(self.resized)
        self.label_image = Label(self, image=self.image).place(x=100, y=50)

        self.handle_thread_socket()
        #self.frame1 = Frame(self, width=300, height=300, bg="blue")
        self.btn_sign_in = Button(self, text='Sign in', background="mint cream", width=13, heigh=2, command=self.open_sign_in)
        self.btn_sign_in.place(x=200, y=350)
        self.btn_sign_up_teacher = Button(self, text='Sign up as teacher', background="cornsilk3", width=13, heigh=2, command=self.open_sign_up_as_teacher)
        self.btn_sign_up_teacher.place(x=200, y=400)
        self.btn_sign_up_student = Button(self, text='Sign up as student', background="light blue", width=13, heigh=2, command=self.open_sign_up_as_student)
        self.btn_sign_up_student.place(x=200, y=450)
        self.btn_exit = Button(self, text="exit", background="red", width=5, heigh=2, command=self.exit)
        self.btn_exit.place(x=225., y=500)

    def open_sign_in(self):
        window = SignInScreen(self)
        window.grab_set()
        self.withdraw()

    def open_sign_up_as_teacher(self):
        window = SignUpTeacher(self)
        window.grab_set()
        self.withdraw()

    def open_sign_up_as_student(self):
        window = SignupStudent(self)
        window.grab_set()
        self.withdraw()

    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.create_socket, args=())
        client_handler.daemon = True
        client_handler.start()


    def create_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('10.20.4.48', 1802))
        data = self.client_socket.recv(1024).decode()
        print("data"+data)
        print("hi", self.client_socket)

    def send_msg(self, data, client_socket):
        try:
            print("message: " + str(data))
            length = str(len(data)).zfill(SIZE)
            length = length.encode('utf-8')
            print(length)
            if type(data) != bytes:
                data = data.encode()
            print(data)
            msg = length + data
            print("message with length: " + str(msg))
            client_socket.send(msg)
        except:
            print("error with sending message")

    def recv_msg(self, client_socket, ret_type="string"):
        try:
            length = client_socket.recv(SIZE).decode('utf-8')
            if not length:
                print("no length")
                return None
            print("the length: " + length)
            data = client_socket.recv(int(length))
            if not data:
                print("no data")
                return None
            print("the data: " + str(data))
            if ret_type == "string":
                data = data.decode('utf-8')
            print(data)
            return data
        except:
            print("error with receiving message")

    def exit(self):
        self.destroy()



if __name__ == "__main__":
    o = OpeningScreen()
    o.mainloop()
