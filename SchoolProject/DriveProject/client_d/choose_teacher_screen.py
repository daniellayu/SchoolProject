import tkinter
from tkinter import *
from tkinter import ttk, messagebox


class ChooseTeacher(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        print(self.parent.parent.id_s)
        print(self.parent.parent.parent.client_socket)
        self.geometry('800x400+350+50')
        self.title('Choose Teacher Screen')
        #Label(self, text="choose your teacher").place(x=100, y=35)
        self.table = ttk.Treeview(self, columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show="headings", heigh="7")
        self.table.column("#1", anchor=CENTER, width=70)
        self.table.column("#2", anchor=CENTER, width=100)
        self.table.column("#3", anchor=CENTER, width=100)
        self.table.column("#4", anchor=CENTER, width=100)
        self.table.column("#5", anchor=CENTER, width=100)
        self.table.column("#6", anchor=CENTER, width=70)
        self.table.column("#7", anchor=CENTER, width=70)
        #self.table.column("#8", anchor=CENTER, width=70)
        self.table.heading("#1", text="teacher id")
        self.table.heading("#2", text="first name")
        self.table.heading("#3", text="last name")
        self.table.heading("#4", text="email")
        self.table.heading("#5", text="phone number")
        self.table.heading("#6", text="experience")
        self.table.heading("#7", text="price")
        #self.table.heading("#8", text="select")
        self.table.bind('<Button-1>', self.selectItem)
        self.table.place(x=45, y=100)
        self.listbox()
        self.btn_close = Button(self, text="go back", background="red", command=self.close)
        self.btn_close.place(x=750, y=370)

    def selectItem(self, event):
        curItem = self.table.focus()
        print(curItem)
        print(self.table.item(curItem)['values'])
        x = self.table.item(curItem)['values']
        print(x[0])
        arr = ["update_teacher_id", x[0], self.parent.parent.id_s]
        print(arr)
        str1 = arr[0]+","+str(arr[1])+","+arr[2]
        print(str1)
        self.parent.parent.parent.send_msg(str1, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)  # recived success or failed
        print(data)
        if data == "success update teacher id":
            messagebox.showinfo("showinfo", "you signed to " + self.table.item(curItem)['values'][1] + self.table.item(curItem)['values'][2])
            self.close()
        if data == "failed update teacher id":
            messagebox.showerror("error", "error")


    def listbox(self):
        arr = ["teachers_list"]
        str = ",".join(arr)
        print(str)
        self.parent.parent.parent.send_msg(str, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        print(data)
        arr_data = data.split("-")
        print(arr_data)
        line1 = arr_data[0].split(",")
        print(line1)
        for item in arr_data:
            line1 = item.split(",")
            self.table.insert("", 'end', text="1", values=(line1[0], line1[1], line1[2], line1[3], line1[4], line1[5], line1[6]))


    def close(self):
        self.parent.deiconify()
        self.destroy()

