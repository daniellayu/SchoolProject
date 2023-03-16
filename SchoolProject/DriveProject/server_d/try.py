import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk


# conn = sqlite3.connect('database.db')
# c = conn.cursor()
#
# c.execute("SELECT * FROM StudentDb")
# data = c.fetchall()
# conn.close()
#
# print(str(data))

class View(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.entry_text = tk.StringVar()
        self.entry1 = Entry(self, textvariable=self.entry_text)
        self.entry_text.set(10)
        self.entry1.place(x=100, y=100)


if __name__ == "__main__":
    v = View()
    v.mainloop()

