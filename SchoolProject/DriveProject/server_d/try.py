from tkinter import *
from tkcalendar import *
from datetime import date


class MyApp(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.cal = Calendar(self, selectmode='day', data_pattern='d/m/yy',
                            disabled_dates=[date(2023, 5, 10), date(2023, 5, 15)])
        self.cal.pack()


root = Tk()
app = MyApp(root)
app.pack()
root.mainloop()