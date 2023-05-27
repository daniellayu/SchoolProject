import tkinter
from tkinter import *
from tkinter import ttk, messagebox

class UpdateDetails(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.title('Update Details Screen')
        # Label(self, text="first name:").place(x=40, y=75)
        # self.entry_fname = Entry(self)
        # self.entry_fname.place(x=125, y=75)
        Label(self, text="Update my details", fg="blue", font=15).place(x=125, y=50)
        Label(self, text="price:").place(x=40, y=125)
        self.entry_price = Entry(self)
        self.entry_price.place(x=125, y=125)
        Label(self, text="years of experience:").place(x=40, y=175)
        self.entry_experience = Entry(self)
        self.entry_experience.place(x=125, y=175)
        self.btn_update = Button(self, text="update", background="pink", command=self.update).place(x=110, y=225)
        #self.btn_close = Button(self, text="close", background="red", command=self.close).place(x=110, y=275)






if __name__ == "__main__":
    o = UpdateDetails()
    o.mainloop()
