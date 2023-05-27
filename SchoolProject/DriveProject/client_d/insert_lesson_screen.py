import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from datetime import datetime




class InsertLesson(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.price = self.parent.price
        self.entry_text = tk.StringVar()
        self.geometry('700x450')
        self.title('Insert Lesson Screen')
        self.cal = Calendar(self, selectmode='day', data_pattern='d/m/yy')
        self.cal.place(x=50, y=50)

        # self.btn_submit = Button(self, text="choose date", command= self.grad_date)
        Button(self, text="Get Date", command=self.grad_date).place(x=65, y=300)
        self.date = Label(self, text="")
        self.date.place(x=150, y=300)

        Label(self, text="time:").place(x=400, y=50)
        self.entry_time = Entry(self)
        self.entry_time.place(x=470, y=50)

        Label(self, text="price:").place(x=400, y=150)
        self.entry_price = Entry(self, textvariable=self.entry_text)
        self.entry_text.set(self.price)
        self.entry_price.place(x=470, y=150)

        self.btn_insert = Button(self, text="insert", bg="pink", command=self.insert_lesson)
        self.btn_insert.place(x=500, y=300)

        self.btn_close = Button(self, text="close", bg="red", command=self.close)
        self.btn_close.place(x=600, y=370)

    def grad_date(self):
        arr_date = self.cal.get_date().split("/")
        print(arr_date)
        arr_date[0] = arr_date[1]
        arr_date[1] = self.cal.get_date().split("/")[0]
        date = '/'.join([str(e) for e in arr_date])
        print(date)
        selected_date_str = self.cal.get_date()
        selected_date_obj = datetime.strptime(selected_date_str, '%m/%d/%y')
        self.day_name = selected_date_obj.strftime('%A')
        print(self.day_name)
        self.date.config(text="Selected Date is: " + date)


    def insert_lesson(self):
        print(self.parent.parent.id_s)
        arr = ["insert_lesson", self.parent.parent.id_s, self.cal.get_date(), self.entry_time.get(), self.entry_price.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.parent.parent.send_msg(str_insert, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        if data == "succeed to insert lesson":
            messagebox.showinfo("showinfo", "succeed to insert lesson")
        elif data == "failed to insert lesson":
            messagebox.showerror("error", "failed to insert lesson")


    def close(self):
        self.parent.deiconify()
        self.destroy()