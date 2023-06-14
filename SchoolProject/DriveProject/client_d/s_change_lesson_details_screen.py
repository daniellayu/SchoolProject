import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
#from lessons_list_screen import LessonsList


class SChangeLessonDetails(tkinter.Toplevel):
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
        self.geometry('600x400+350+50')
        self.title('Change Lesson Details')

        Label(self, text="date:").place(x=100, y=75)
        self.entry_date = Entry(self, textvariable=self.entry_text1)
        self.entry_text1.set(self.date)
        self.entry_date.place(x=175, y=75)
        #self.btn_calender = Button(self, text="calender", command=self.open_calender).place(x=270, y=75)

        Label(self, text="time:").place(x=100, y=175)
        self.entry_time = Entry(self, textvariable=self.entry_text2)
        self.entry_text2.set(self.time)
        self.entry_time.place(x=175, y=175)

        self.cal = Calendar(self, selectmode='day', data_pattern='d/mm/yy')
        self.cal.place(x=325, y=75)
        Button(self, text="Get Date", command=self.grad_date).place(x=400, y=275)
        self.date = Label(self, text="")
        self.date.place(x=450, y=275)

        self.btn_change = Button(self, text="change", bg="pink", command=self.change_lesson_details).place(x=175, y=275)
        self.btn_close = Button(self, text="go back", background="red", command=self.close)
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
        arr_date = self.cal.get_date().split("/")
        print(arr_date)
        arr_date[0] = arr_date[1]
        arr_date[1] = self.cal.get_date().split("/")[0]
        date = '/'.join([str(e) for e in arr_date])
        self.date.config(text="Selected Date is: " + date)
        print(date)
        self.entry_text1.set(date)


    # def open_teacher_lessons_screen(self):
    #     window = LessonsList(self)
    #     window.grab_set()
    #     self.withdraw()


    def close(self):
        self.parent.deiconify()
        self.destroy()
