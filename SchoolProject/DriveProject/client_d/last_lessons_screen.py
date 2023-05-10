import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from datetime import date as d



class LastLessons(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('800x450')
        self.title('Last Lessons Screen')
        self.table = ttk.Treeview(self, columns=("c1", "c2", "c3", "c4", "c5"), show="headings", heigh="7")
        self.table.column("#1", anchor=CENTER, width=120)
        self.table.column("#2", anchor=CENTER, width=120)
        self.table.column("#3", anchor=CENTER, width=120)
        self.table.column("#4", anchor=CENTER, width=120)
        self.table.column("#5", anchor=CENTER, width=120)
        self.table.heading("#1", text="lessonId")
        self.table.heading("#2", text="student name")
        self.table.heading("#3", text="date")
        self.table.heading("#4", text="time")
        self.table.heading("#5", text="price")
        self.table.place(x=150, y=100)
        self.listbox()
        self.btn_close = Button(self, text="Close", background="red", command=self.close)
        self.btn_close.place(x=650, y=370)

    def listbox(self):
        arr = ["lessons_list", self.parent.parent.id_t]
        str1 = arr[0] + "," + (arr[1])
        print(str1)
        self.parent.parent.parent.client_socket.send(str1.encode())
        data = self.parent.parent.parent.client_socket.recv(1024).decode()
        print(data)
        arr_data = data.split("-")
        print(arr_data)
        for item in arr_data:
            line1 = item.split(",")
            print(line1)
            student_id = line1[2]
            print(student_id)
            arr2 = ["student_id_to_name", student_id]
            str2 = arr2[0] + "," + arr2[1]
            self.parent.parent.parent.client_socket.send(str2.encode())
            student_name = self.parent.parent.parent.client_socket.recv(1024).decode()
            print("student name: " + student_name)

            date = line1[3].split("/")
            print(date) #['10', '7', '22']
            month = int(date[0])
            day = int(date[1])
            year = date[2]
            today_date = str(d.today())
            print(today_date)
            arr_today_date = today_date.split("-")
            print(arr_today_date) #['2023', '04', '07']
            if month <= int(arr_today_date[1]):
                if (month == int(arr_today_date[1]) and day <= int(arr_today_date[2])) or (month < int(arr_today_date[1])):
                    self.table.insert("", 'end', text="1", values=(line1[0], student_name, line1[3], line1[4], line1[5]))


    def close(self):
        self.parent.deiconify()
        self.destroy()
