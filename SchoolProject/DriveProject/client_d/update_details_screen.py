import tkinter
from tkinter import *
from tkinter import ttk, messagebox


class UpdateDetails(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('400x400')
        self.title('Update Details Screen')
        # Label(self, text="first name:").place(x=40, y=75)
        # self.entry_fname = Entry(self)
        # self.entry_fname.place(x=125, y=75)
        Label(self, text="price:").place(x=40, y=125)
        self.entry_price = Entry(self)
        self.entry_price.place(x=150, y=125)
        Label(self, text="years of experience:").place(x=40, y=175)
        self.entry_experience = Entry(self)
        self.entry_experience.place(x=150, y=175)
        self.btn_update = Button(self, text="update", background="pink", command=self.update).place(x=110, y=225)
        self.btn_close = Button(self, text="go back", background="red", command=self.close).place(x=110, y=275)


    def update(self):
        if (len(self.entry_price.get()) == 0) and (len(self.entry_experience.get()) == 0):
            messagebox.showerror("error", "please write your new details")
            return
        arr = ["update_details", self.parent.parent.id_t, self.entry_price.get(), self.entry_experience.get()]
        #str1 = arr[0] + "," + arr[1] + "," + arr[2] + "," + arr[3]
        #print(str1)
        str_update = ",".join(arr)
        print(str_update)
        self.parent.parent.parent.send_msg(str_update, self.parent.parent.parent.client_socket)
        data = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
        print(data)
        if data == "success update details":
            messagebox.showinfo("showinfo", "your details have been successfully updated")
        if data == "failed update details":
            messagebox.showerror("error", "try again")


    def close(self):
        self.parent.deiconify()
        self.destroy()

