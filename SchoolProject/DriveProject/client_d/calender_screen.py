import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar


class Calender(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        #print(self.parent.parent.parent.id_t)
        # self.date = self.parent.date
        # print(self.date)
        # self.time = self.parent.time
        # print(self.time)
        # self.lesson_id = self.parent.lesson_id
        # print(self.lesson_id)
        # self.entry_text1 = tk.StringVar()
        # self.entry_text2 = tk.StringVar()
        self.geometry('400x400')
        self.title('Calender')
        self.cal = Calendar(self, selectmode='day', data_pattern='d/m/yy')
        self.cal.place(x=50, y=50)
        # self.btn_submit = Button(self, text="choose date", command= self.grad_date)
        Button(self, text="Get Date", command=self.grad_date).pack(pady=20)
        self.date = Label(self, text="")
        self.date.pack(pady=20)
        self.btn_close = Button(self, text="Close", background="red", command=self.close)
        self.btn_close.place(x=350, y=350)


    def grad_date(self):

        self.date.config(text="Selected Date is: " + self.cal.get_date())
        print(self.cal.get_date())



    def close(self):
        self.parent.deiconify()
        self.destroy()

