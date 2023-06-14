import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from datetime import datetime
import calendar



class InsertLesson(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.price = self.parent.price
        self.entry_text = tk.StringVar()
        self.value_inside = tk.StringVar()
        self.geometry('700x450+350+50')
        self.title('Insert Lesson Screen')
        self.cal = Calendar(self, selectmode='day', data_pattern='d/m/yy')
        self.cal.place(x=50, y=50)

        # self.btn_submit = Button(self, text="choose date", command= self.grad_date)
        Button(self, text="Get Date", command=self.grad_date).place(x=65, y=300)
        self.date = Label(self, text="")
        self.date.place(x=150, y=300)

        Label(self, text="time:").place(x=400, y=50)
        self.get_t_hours()
        # self.entry_time = Entry(self)
        # self.entry_time.place(x=470, y=50)

        Label(self, text="price:").place(x=400, y=150)
        self.entry_price = Entry(self, textvariable=self.entry_text)
        self.entry_text.set(self.price)
        self.entry_price.place(x=470, y=150)

        self.btn_insert = Button(self, text="insert", bg="pink", command=self.insert_lesson)
        self.btn_insert.place(x=500, y=300)

        self.btn_close = Button(self, text="go back", bg="red", command=self.close)
        self.btn_close.place(x=600, y=370)

        # self.arr_data = []
        # self.disable_days(self.arr_data)




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


    def disable_days(self, arr):
        arr = ["get_t_work_days", self.parent.parent.id_s]
        str1 = ",".join(arr)
        print(str1)
        self.parent.parent.parent.send_msg(str1, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        print(data)
        self.arr_data = data.split(",")
        print(self.arr_data)

        arr_date = self.cal.get_date().split("/")
        print(arr_date)
        # arr_date[0] = arr_date[1]
        arr_date[1] = self.cal.get_date().split("/")[0]
        arr_date[2] = arr_date[0]
        arr_date[0] = self.cal.get_date().split("/")[2]
        date = '/'.join([str(e) for e in arr_date])
        print(date)

        # Extract the year and month from the selected date
        year, month, _ = map(int, date.split('/'))

        # Get the first and last day of the month
        _, last_day = calendar.monthrange(year, month)

        for day in range(1, last_day + 1):
            # Get the weekday of the day
            weekday = calendar.weekday(year, month, day)

            # Check if the weekday matches any day in the given list
            if calendar.day_name[weekday].lower() in arr_date:
                # Disable the day in the calendar
                self.cal.calevent_create(f'disabled_day_{day}', f'{day}/{month}/{year}', f'Disabled Day {day}')
                self.cal.tag_config(f'disabled_day_{day}', background='gray', foreground='white')


    def get_t_hours(self):
        arr = ['get_t_work_hours', self.parent.parent.id_s]
        str_hours = ",".join(arr)
        self.parent.parent.parent.send_msg(str_hours, self.parent.parent.parent.client_socket)
        hours_options = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        arr_options = hours_options.split(",")
        print(arr_options)
        self.value_inside.set("select hour")
        self.hours_list = OptionMenu(self, self.value_inside, *arr_options)
        self.hours_list.place(x=470, y=50)


    # def print_answers(self):
    #     print("Selected Option: {}".format(self.value_inside.get()))
    #     return None





    def insert_lesson(self):
        print(self.parent.parent.id_s)
        arr = ["insert_lesson", self.parent.parent.id_s, self.cal.get_date(), self.value_inside.get(), self.entry_price.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.parent.parent.send_msg(str_insert, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        if data == "succeed to insert lesson":
            messagebox.showinfo("showinfo", "succeed to insert lesson")
            arr2 = ["send_msg_for_teacher", self.parent.parent.id_s, self.cal.get_date(),
                    "new lesson"]
            str2 = ",".join(arr2)
            self.parent.parent.parent.send_msg(str2, self.parent.parent.parent.client_socket)
            data2 = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
            print(data2)
        elif data == "failed to insert lesson":
            messagebox.showerror("error", "failed to insert lesson")


    def close(self):
        self.parent.deiconify()
        self.destroy()