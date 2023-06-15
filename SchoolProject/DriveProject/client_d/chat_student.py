import tkinter
from tkinter import *
from tkinter import ttk, messagebox


class ChatStudent(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('800x500+350+50')
        self.title('Chat Screen')
        Label(self, text="CHAT", fg="#57a1f8", font=('Microsoft YaHei UI Light', 23, 'bold')).place(x=150, y=40)
        self.table = ttk.Treeview(self, columns=("c1", "c2", "c3"), show="headings", heigh="7")
        self.table.column("#1", anchor=CENTER, width=160)
        self.table.column("#2", anchor=CENTER, width=160)
        self.table.column("#3", anchor=CENTER, width=160)

        self.table.heading("#1", text="from")
        self.table.heading("#2", text="date")
        self.table.heading("#3", text="message")

        self.table.place(x=170, y=100)
        self.table.bind('<Button-1>', self.select_line)
        self.btn_close = Button(self, text="go back", background="red", command=self.close).place(x=400, y=300)


        self.listbox()


    def listbox(self):
        arr = ["s_messages", self.parent.parent.id_s]
        str1 = ",".join(arr)
        print(str1)
        self.parent.parent.parent.send_msg(str1, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        print(data)
        arr_data = data.split("-")
        print(arr_data)
        for item in arr_data:
            line1 = item.split(",")
            print(line1)
            teacher_id = line1[2]
            print(teacher_id)
            arr2 = ["teacher_id_to_name", teacher_id]
            str2 = arr2[0] + "," + arr2[1]
            self.parent.parent.parent.send_msg(str2, self.parent.parent.client_socket)
            teacher_name = self.parent.parent.parent.recv_msg(self.parent.parent.client_socket)
            print("teacher name: " + teacher_name)
            self.table.insert("", 'end', text="1", values=(line1[1], teacher_name, line1[2]))

            # date = line1[3].split("/")
            # print(date)  # ['10', '7', '22']
            # month = int(date[0])
            # day = int(date[1])
            # # year = date[2]
            # today_date = str(d.today())
            # print(today_date)
            # arr_today_date = today_date.split("-")
            # print(arr_today_date)  # ['2023', '04', '07']

            # if month >= int(arr_today_date[1]):
            #     if (month == int(arr_today_date[1]) and day >= int(arr_today_date[2])) or (
            #             month > int(arr_today_date[1])):
            #         self.table.insert("", 'end', text="1",
            #                           values=(line1[0], student_name, line1[3], line1[4], line1[5]))

    def select_line(self, event):
        curItem = self.table.focus()
        print(curItem)
        print(self.table.item(curItem)['values'])
        self.x = self.table.item(curItem)['values']
        # self.lesson_id = self.x[0]
        # print(self.lesson_id)
        # self.student_name = self.x[1]
        # print(self.student_name)
        # self.date = self.x[2]
        # print(self.date)
        # self.time = self.x[3]
        # print(self.time)

    def close(self):
        self.parent.deiconify()
        self.destroy()
        