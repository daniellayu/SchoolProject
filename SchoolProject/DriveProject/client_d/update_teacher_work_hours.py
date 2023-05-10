import tkinter
from tkinter import *
from tkinter import ttk, messagebox

class UpdateTeacherWorkTime(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x400')
        self.title('Update Teacher Work Time')

        self.check_var1 = IntVar()
        self.check_var2 = IntVar()
        self.check_var3 = IntVar()
        self.check_var4 = IntVar()
        self.check_var5 = IntVar()
        self.check_var6 = IntVar()

        self.c1 = Checkbutton(self, text="sunday", variable=self.check_var1, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c1.place(x=200, y=50)
        self.c2 = Checkbutton(self, text="monday", variable=self.check_var2, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c2.place(x=200, y=100)
        self.c3 = Checkbutton(self, text="tuesday", variable=self.check_var3, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c3.place(x=200, y=150)
        self.c4 = Checkbutton(self, text="wednesday", variable=self.check_var4, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c4.place(x=200, y=200)
        self.c5 = Checkbutton(self, text="thursday", variable=self.check_var5, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c5.place(x=200, y=250)
        self.c6 = Checkbutton(self, text="friday", variable=self.check_var6, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c6.place(x=200, y=300)

        self.btn_submit = Button(self, text="submit", command=self.get_checked_days)
        self.btn_submit.place(x=250, y=400)

        self.btn_close = Button(self, text="close", bg="red", command=self.close)
        self.btn_close.place(x=550, y=400)

    def get_checked_days(self):
        self.days_checked = ["update_t_work_days", self.parent.parent.id_t]
        if self.check_var1.get() == 1:
            self.days_checked.append("sunday")
        if self.check_var2.get() == 1:
            self.days_checked.append("monday")
        if self.check_var3.get() == 1:
            self.days_checked.append("tuesday")
        if self.check_var4.get() == 1:
            self.days_checked.append("wednesday")
        if self.check_var5.get() == 1:
            self.days_checked.append("thursday")
        if self.check_var6.get() == 1:
            self.days_checked.append("friday")
        print(self.days_checked)
        str_days_checked = ",".join(self.days_checked)
        print(str_days_checked)
        self.parent.parent.parent.client_socket.send(str_days_checked.encode())
        data = self.parent.parent.parent.client_socket.recv(1024).decode()
        if data == "succeed to update teacher's days":
            messagebox.showinfo("showinfo", "succeed to update teacher's days")
            self.close()
        elif data == "failed to update teacher's days":
            messagebox.showerror("error", "failed to update teacher's days")


    def close(self):
        self.parent.deiconify()
        self.destroy()

