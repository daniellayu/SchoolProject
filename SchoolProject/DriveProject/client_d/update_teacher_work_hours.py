import tkinter
from tkinter import *
from tkinter import ttk, messagebox

class UpdateTeacherWorkTime(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x500')
        self.title('Update Teacher Work Time')

        self.check_var1 = IntVar()
        self.check_var2 = IntVar()
        self.check_var3 = IntVar()
        self.check_var4 = IntVar()
        self.check_var5 = IntVar()
        self.check_var6 = IntVar()

        self.check_var8 = IntVar()
        self.check_var9 = IntVar()
        self.check_var10 = IntVar()
        self.check_var11 = IntVar()
        self.check_var12 = IntVar()
        self.check_var13 = IntVar()
        self.check_var14 = IntVar()
        self.check_var15 = IntVar()
        self.check_var16 = IntVar()
        self.check_var17 = IntVar()
        self.check_var18 = IntVar()
        self.check_var19 = IntVar()
        self.check_var20 = IntVar()

        Label(self, text="WORK DAYS", fg="#3C00CC", font=('Microsoft YaHei UI Light', 23, 'bold')).place(x=80, y=5)

        self.c1 = Checkbutton(self, text="sunday", variable=self.check_var1, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c1.place(x=100, y=50)
        self.c2 = Checkbutton(self, text="monday", variable=self.check_var2, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c2.place(x=100, y=100)
        self.c3 = Checkbutton(self, text="tuesday", variable=self.check_var3, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c3.place(x=100, y=150)
        self.c4 = Checkbutton(self, text="wednesday", variable=self.check_var4, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c4.place(x=100, y=200)
        self.c5 = Checkbutton(self, text="thursday", variable=self.check_var5, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c5.place(x=100, y=250)
        self.c6 = Checkbutton(self, text="friday", variable=self.check_var6, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c6.place(x=100, y=300)

        self.btn_submit_days = Button(self, text="submit days", fg='#3C00CC',
                                 font=('Microsoft YaHei UI Light', 11, 'bold'), command=self.get_checked_days)
        self.btn_submit_days.place(x=125, y=400)


        Label(self, text="WORK HOURS", fg="#2583BA", font=('Microsoft YaHei UI Light', 23, 'bold')).place(x=320, y=5)


        self.c8 = Checkbutton(self, text="8:00", variable=self.check_var8, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c8.place(x=300, y=50)
        self.c9 = Checkbutton(self, text="9:00", variable=self.check_var9,
                              onvalue=1, offvalue=0, height=5, width=20)
        self.c9.place(x=300, y=100)
        self.c10 = Checkbutton(self, text="10:00", variable=self.check_var10, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c10.place(x=300, y=150)
        self.c11 = Checkbutton(self, text="11:00", variable=self.check_var11,
                              onvalue=1, offvalue=0, height=5, width=20)
        self.c11.place(x=300, y=200)
        self.c12 = Checkbutton(self, text="12:00", variable=self.check_var12, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c12.place(x=300, y=250)
        self.c13 = Checkbutton(self, text="13:00", variable=self.check_var13,
                              onvalue=1, offvalue=0, height=5, width=20)
        self.c13.place(x=300, y=300)
        self.c14 = Checkbutton(self, text="14:00", variable=self.check_var14, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c14.place(x=300, y=350)
        self.c15 = Checkbutton(self, text="15:00", variable=self.check_var15,
                              onvalue=1, offvalue=0, height=5, width=20)
        self.c15.place(x=420, y=50)
        self.c16 = Checkbutton(self, text="16:00", variable=self.check_var16, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c16.place(x=420, y=100)
        self.c17 = Checkbutton(self, text="17:00", variable=self.check_var17,
                              onvalue=1, offvalue=0, height=5, width=20)
        self.c17.place(x=420, y=150)
        self.c18 = Checkbutton(self, text="18:00", variable=self.check_var18, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c18.place(x=420, y=200)
        self.c19 = Checkbutton(self, text="19:00", variable=self.check_var19,
                              onvalue=1, offvalue=0, height=5, width=20)
        self.c19.place(x=420, y=250)
        self.c20 = Checkbutton(self, text="20:00", variable=self.check_var20,
                               onvalue=1, offvalue=0, height=5, width=20)
        self.c20.place(x=420, y=300)

        self.btn_submit_hours = Button(self, text="submit hours", fg='#2583BA',
                                      font=('Microsoft YaHei UI Light', 11, 'bold'), command=self.get_checked_hours)
        self.btn_submit_hours.place(x=400, y=400)



        self.btn_close = Button(self, text="go back", bg="red", command=self.close)
        self.btn_close.place(x=550, y=470)

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
        self.parent.parent.parent.send_msg(str_days_checked, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        if data == "succeed to update teacher's days":
            messagebox.showinfo("showinfo", "succeed to update teacher's days")
            self.close()
        elif data == "failed to update teacher's days":
            messagebox.showerror("error", "failed to update teacher's days")


    def get_checked_hours(self):
        self.hours_checked = ["update_t_work_hours", self.parent.parent.id_t]
        if self.check_var8.get() == 1:
            self.days_checked.append("8:00")
        if self.check_var9.get() == 1:
            self.days_checked.append("9:00")
        if self.check_var10.get() == 1:
            self.days_checked.append("10:00")
        if self.check_var11.get() == 1:
            self.days_checked.append("11:00")
        if self.check_var12.get() == 1:
            self.days_checked.append("12:00")
        if self.check_var13.get() == 1:
            self.days_checked.append("13:00")
        if self.check_var14.get() == 1:
            self.days_checked.append("14:00")
        if self.check_var15.get() == 1:
            self.days_checked.append("15:00")
        if self.check_var16.get() == 1:
            self.days_checked.append("16:00")
        if self.check_var17.get() == 1:
            self.days_checked.append("17:00")
        if self.check_var18.get() == 1:
            self.days_checked.append("18:00")
        if self.check_var19.get() == 1:
            self.days_checked.append("19:00")
        if self.check_var20.get() == 1:
            self.days_checked.append("20:00")
        print(self.hours_checked)
        str_hours_checked = ",".join(self.hourss_checked)
        print(str_hours_checked)
        self.parent.parent.parent.send_msg(str_hours_checked, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        if data == "succeed to update teacher's hours":
            messagebox.showinfo("showinfo", "succeed to update teacher's hours")
            self.close()
        elif data == "failed to update teacher's hours":
            messagebox.showerror("error", "failed to update teacher's hours")



    def close(self):
        self.parent.deiconify()
        self.destroy()


