import tkinter
from tkinter import *
from tkinter import ttk


class StudentsList(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('700x400')
        self.title('Students List Screen')
        self.table = ttk.Treeview(self, columns=("c1", "c2", "c3", "c4", "c5", "c6"), show="headings", heigh="7")
        self.table.column("#1", anchor=CENTER, width=100)
        self.table.column("#2", anchor=CENTER, width=100)
        self.table.column("#3", anchor=CENTER, width=100)
        self.table.column("#4", anchor=CENTER, width=100)
        self.table.column("#5", anchor=CENTER, width=100)
        self.table.column("#6", anchor=CENTER, width=100)
        self.table.heading("#1", text="studentId")
        self.table.heading("#2", text="first name")
        self.table.heading("#3", text="last name")
        self.table.heading("#4", text="email")
        self.table.heading("#5", text="phone number")
        self.table.heading("#6", text="id")
        self.table.place(x=45, y=100)
        self.listbox()
        self.btn_close = Button(self, text="Close", background="red", command=self.close)
        self.btn_close.place(x=650, y=370)



    def listbox(self):
        arr = ["students_list", self.parent.parent.id_t]
        str1 = arr[0]+","+(arr[1])
        print(str1)
        self.parent.parent.parent.send_msg(str1, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        print(data)
        arr_data = data.split("-")
        print(arr_data)
        line1 = arr_data[0].split(",")
        print(line1)
        for item in arr_data:
            line1 = item.split(",")
            self.table.insert("", 'end', text="1", values=(line1[0], line1[1], line1[2], line1[3], line1[4], line1[5]))



    def close(self):
        self.parent.deiconify()
        self.destroy()