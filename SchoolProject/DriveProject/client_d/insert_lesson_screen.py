import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

import parso.parser
from tkcalendar import Calendar
from datetime import datetime
import calendar



class InsertLesson(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.price = 0
        self.entry_text = tk.StringVar()
        self.value_inside = tk.StringVar()
        self.geometry('700x450+350+50')
        self.title('Insert Lesson Screen')
        Label(self, text="INSERT LESSON", fg="#CC9999", font=('Microsoft YaHei UI Light', 20, 'bold')).place(x=250, y=15)
        self.disable_days()


        self.cal = Calendar(self, selectmode='day', data_pattern='d/m/yy')
        self.cal.place(x=50, y=100)

        # self.btn_submit = Button(self, text="choose date", command= self.grad_date)
        Button(self, text="Get Date", command=self.grad_date).place(x=65, y=325)
        self.date = Label(self, text="")
        self.date.place(x=150, y=325)

        Label(self, text="time:").place(x=400, y=100)
        self.get_t_hours()
        # self.entry_time = Entry(self)
        # self.entry_time.place(x=470, y=50)

        Label(self, text="price:").place(x=400, y=200)
        self.entry_price = Entry(self, textvariable=self.entry_text)
        self.get_t_price()


        self.btn_insert = Button(self, text="insert", fg='black', bg='#CC9999',
                                 font=('Microsoft YaHei UI Light', 11, 'bold'), command=self.insert_lesson)
        self.btn_insert.place(x=250, y=400)

        self.btn_close = Button(self, text="go back", bg="red", command=self.close)
        self.btn_close.place(x=600, y=370)

        # self.arr_data = []
        # self.disable_days(self.arr_data)




    def grad_date(self):
        arr_date = self.cal.get_date().split("/")
        print(arr_date)
        arr_date[0] = arr_date[1]
        arr_date[1] = self.cal.get_date().split("/")[0]
        self.date1 = '/'.join([str(e) for e in arr_date])
        print(self.date1)
        selected_date_str = self.cal.get_date()
        selected_date_obj = datetime.strptime(selected_date_str, '%m/%d/%y')
        self.day_name = selected_date_obj.strftime('%A')
        print(self.day_name)
        self.date.config(text="Selected Date is: " + self.date1)
        arr = ["get_t_work_days", self.parent.parent.id_s]
        str1 = ",".join(arr)
        print(str1)
        self.parent.parent.parent.send_msg(str1, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        print(data)
        self.arr_data = data.split(",")
        print(self.arr_data)
        arr_date1 = self.cal.get_date().split("/")
        print(arr_date1)
        for i in self.arr_data:
            if i == str(self.day_name).lower():
                messagebox.showinfo("showinfo", "your teacher is not working on this day")



    def disable_days(self):
        arr = ["get_t_work_days", self.parent.parent.id_s]
        str1 = ",".join(arr)
        print(str1)
        self.parent.parent.parent.send_msg(str1, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        print(data)
        Label(self, text=f"your teacher's days off are:{data}", fg="#B30000", font=('Microsoft YaHei UI Light', 14, 'bold')).place(x=50, y=50)


    def get_t_price(self):
        arr = ["get_t_price", self.parent.parent.id_s]
        str1 = ",".join(arr)
        self.parent.parent.parent.send_msg(str1, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        self.entry_text.set(data)
        self.entry_price.place(x=470, y=200)





    def get_t_hours(self):
        arr = ['get_t_work_hours', self.parent.parent.id_s]
        str_hours = ",".join(arr)
        self.parent.parent.parent.send_msg(str_hours, self.parent.parent.parent.client_socket)
        hours_options = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        arr_options = hours_options.split(",")
        print(arr_options)
        self.value_inside.set("select hour")
        self.hours_list = OptionMenu(self, self.value_inside, *arr_options)
        self.hours_list.place(x=470, y=100)


    # def print_answers(self):
    #     print("Selected Option: {}".format(self.value_inside.get()))
    #     return None





    def check_lesson(self):
        print(self.parent.parent.id_s)
        arr = ["check_lesson", self.parent.parent.id_s, self.date1, self.value_inside.get(), self.entry_price.get()]
        str_check = ",".join(arr)
        print(str_check)
        self.parent.parent.parent.send_msg(str_check, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        if data == "lesson is not exist":
            self.insert_lesson()
        if data == "lesson is exist":
            messagebox.showinfo("showinfo", "your teacher is already in a lesson this time, please chose differnt time or date")


    def insert_lesson(self):
        arr1 = ["insert_lesson", self.parent.parent.id_s, self.date1, self.value_inside.get(), self.entry_price.get()]
        str_insert = ",".join(arr1)
        print(str_insert)
        self.parent.parent.parent.send_msg(str_insert, self.parent.parent.parent.client_socket)
        data1 = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        if data1 == "succeed to insert lesson":
            messagebox.showinfo("showinfo", "succeed to insert lesson")
            arr2 = ["send_msg_for_teacher", self.parent.parent.id_s, self.cal.get_date(),
                    "new lesson"]
            str2 = ",".join(arr2)
            self.parent.parent.parent.send_msg(str2, self.parent.parent.parent.client_socket)
            data2 = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
            print(data2)
            self.close()
        elif data1 == "failed to insert lesson":
            messagebox.showerror("error", "failed to insert lesson")


    def close(self):
        self.parent.deiconify()
        self.destroy()