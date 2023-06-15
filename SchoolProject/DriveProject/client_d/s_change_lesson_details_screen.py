import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from datetime import datetime

#from lessons_list_screen import LessonsList


class SChangeLessonDetails(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        Label(self, text="LESSON'S DETAILS", fg="#ffe599", font=('Microsoft YaHei UI Light', 23, 'bold')).place(x=100, y=10)

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
        self.value_inside = tk.StringVar()

        self.geometry('600x400+350+50')
        self.title('Change Lesson Details')
        self.disable_days()

        Label(self, text="date:").place(x=100, y=100)
        self.entry_date = Entry(self, textvariable=self.entry_text1)
        self.entry_text1.set(self.date)
        self.entry_date.place(x=175, y=100)
        #self.btn_calender = Button(self, text="calender", command=self.open_calender).place(x=270, y=75)

        Label(self, text="time:").place(x=100, y=200)
        self.entry_time = Entry(self, textvariable=self.entry_text2)
        self.get_t_hours()

        # self.entry_text2.set(self.time)
        # self.entry_time.place(x=175, y=175)

        self.cal = Calendar(self, selectmode='day', data_pattern='d/mm/yy')
        self.cal.place(x=325, y=100)
        Button(self, text="Get Date", command=self.grad_date).place(x=400, y=300)
        # self.date = Label(self, text="")
        # self.date.place(x=450, y=275)

        self.btn_change = Button(self, text="change", bg="pink", command=self.change_lesson_details).place(x=175, y=275)
        self.btn_close = Button(self, text="go back", background="red", command=self.close)
        self.btn_close.place(x=300, y=350)



    def change_lesson_details(self):
        if (len(self.entry_date.get()) == 0) and (len(self.entry_time.get()) == 0):
            messagebox.showerror("error", "please write your new details")
            return

        arr = ["change_lesson_details",  str(self.lesson_id) ,self.entry_date.get(), self.value_inside.get()]
        # str1 = arr[0] + "," + arr[1] + "," + arr[2] + "," + arr[3]
        # print(str1)

        str_change = ",".join(arr)
        print(str_change)
        self.parent.parent.parent.send_msg(str_change, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)  # recived success or failed
        print(data)
        if data == "succeed to change lesson details":
            messagebox.showinfo("showinfo", "your details have been successfully updated")
            arr2 = ["send_msg_for_teacher", self.parent.parent.id_s, self.cal.get_date(), "lesson's details have changed"]
            str2 = ",".join(arr2)
            self.parent.parent.parent.send_msg(str2, self.parent.parent.parent.client_socket)
            data2 = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
            print(data2)
        if data == "failed to change lesson details":
            messagebox.showerror("error", "try again")

    def grad_date(self):
        # arr_date = self.cal.get_date().split("/")
        # print(arr_date)
        # arr_date[0] = arr_date[1]
        # arr_date[1] = self.cal.get_date().split("/")[0]
        # date = '/'.join([str(e) for e in arr_date])
        # self.date.config(text="Selected Date is: " + date)
        # print(date)
        # self.entry_text1.set(date)

        arr_date = self.cal.get_date().split("/")
        print(arr_date)
        arr_date[0] = arr_date[1]
        arr_date[1] = self.cal.get_date().split("/")[0]
        self.date1 = '/'.join([str(e) for e in arr_date])
        print(self.date1)
        self.entry_text1.set(self.date1)

        selected_date_str = self.cal.get_date()
        selected_date_obj = datetime.strptime(selected_date_str, '%m/%d/%y')
        self.day_name = selected_date_obj.strftime('%A')
        print(self.day_name)
        # self.date.config(text="Selected Date is: " + self.date1)
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

    def get_t_hours(self):
        arr = ['get_t_work_hours', self.parent.parent.id_s]
        str_hours = ",".join(arr)
        self.parent.parent.parent.send_msg(str_hours, self.parent.parent.parent.client_socket)
        hours_options = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        arr_options = hours_options.split(",")
        print(arr_options)
        self.value_inside.set("select hour")
        self.hours_list = OptionMenu(self, self.value_inside, *arr_options)
        self.hours_list.place(x=175, y=200)

    def disable_days(self):
        arr = ["get_t_work_days", self.parent.parent.id_s]
        str1 = ",".join(arr)
        print(str1)
        self.parent.parent.parent.send_msg(str1, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        print(data)
        Label(self, text=f"your teacher's days off are:{data}", fg="#B30000", font=('Microsoft YaHei UI Light', 11, 'bold')).place(x=70, y=60)



    # def open_teacher_lessons_screen(self):
    #     window = LessonsList(self)
    #     window.grab_set()
    #     self.withdraw()


    def close(self):
        self.parent.deiconify()
        self.destroy()
