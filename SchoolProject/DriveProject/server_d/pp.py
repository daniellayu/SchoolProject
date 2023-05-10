import tkinter
from tkinter import *
from tkinter import ttk, messagebox

class UpdateTeacherWorkTime(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x500')
        self.title('Update Teacher Work Time')

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()


        self.c1 = Checkbutton(self, text="sunday", variable=self.var1, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c1.place(x=200, y=50)
        self.c2 = Checkbutton(self, text="monday", variable=self.var2, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c2.place(x=200, y=100)
        self.c3 = Checkbutton(self, text="tuesday", variable=self.var3, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c3.place(x=200, y=150)
        self.c4 = Checkbutton(self, text="wednesday", variable=self.var4, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c4.place(x=200, y=200)
        self.c5 = Checkbutton(self, text="thursday", variable=self.var5, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c5.place(x=200, y=250)
        self.c6 = Checkbutton(self, text="friday", variable=self.var6, onvalue=1, offvalue=0,
                              height=5, width=20)
        self.c6.place(x=200, y=300)

        self.btn_submit = Button(self, text="submit", command=self.get_checked_days)
        self.btn_submit.place(x=250, y=400)


    def get_checked_days(self):
        self.days_checked = ["update_t_work_days"]
        if self.var1.get() == 1:
            self.days_checked.append("sunday")
        if self.var2.get() == 1:
            self.days_checked.append("monday")
        if self.var3.get() == 1:
            self.days_checked.append("tuesday")
        if self.var4.get() == 1:
            self.days_checked.append("wednesday")
        if self.var5.get() == 1:
            self.days_checked.append("thursday")
        if self.var6.get() == 1:
            self.days_checked.append("friday")
        print(self.days_checked)
        str_days_checked = ",".join(self.days_checked)
        print(str_days_checked)





if __name__ == "__main__":
    o = UpdateTeacherWorkTime()
    o.mainloop()
