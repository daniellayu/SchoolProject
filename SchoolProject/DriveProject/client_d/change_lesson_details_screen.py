import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox


class ChangeLessonDetails(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        #print(self.parent.parent.parent.id_t)
        self.date = self.parent.date
        print(self.date)
        self.time = self.parent.time
        print(self.time)
        self.lesson_id = self.parent.lesson_id
        print(self.lesson_id)
        self.entry_text1 = tk.StringVar()
        self.entry_text2 = tk.StringVar()
        self.geometry('400x400')
        self.title('Change Lesson Details')
        Label(self, text="date:").place(x=100, y=75)
        self.entry_date = Entry(self, textvariable=self.entry_text1)
        self.entry_text1.set(self.date)
        self.entry_date.place(x=175, y=75)
        Label(self, text="time:").place(x=100, y=175)
        self.entry_time = Entry(self, textvariable=self.entry_text2)
        self.entry_text2.set(self.time)
        self.entry_time.place(x=175, y=175)
        self.btn_change = Button(self, text="change", bg="pink", command=self.change_lesson_details).place(x=175, y=275)
        self.btn_close = Button(self, text="Close", background="red", command=self.close)
        self.btn_close.place(x=300, y=350)



    def change_lesson_details(self):
        if (len(self.entry_date.get()) == 0) and (len(self.entry_time.get()) == 0):
            messagebox.showerror("error", "please write your new details")
            return
        arr = ["change_lesson_details",  str(self.lesson_id) ,self.entry_date.get(), self.entry_time.get()]
        # str1 = arr[0] + "," + arr[1] + "," + arr[2] + "," + arr[3]
        # print(str1)

        str_change = ",".join(arr)
        print(str_change)
        self.parent.parent.parent.parent.client_socket.send(str_change.encode())
        data = self.parent.parent.parent.parent.client_socket.recv(1024).decode()  # recived success or failed
        print(data)
        if data == "succeed to change lesson details":
            messagebox.showinfo("showinfo", "your details have been successfully updated")
        if data == "failed to change lesson details":
            messagebox.showerror("error", "try again")



    def close(self):
        self.parent.deiconify()
        self.destroy()
