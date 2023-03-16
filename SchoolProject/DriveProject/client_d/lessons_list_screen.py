import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from last_lessons_screen import LastLessons
from change_lesson_details_screen import ChangeLessonDetails


class LessonsList(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        print(self.parent.parent.id_t)
        self.geometry('700x400')
        self.title('Lessons List Screen')
        self.table = ttk.Treeview(self, columns=("c1", "c2", "c3", "c4", "c5"), show="headings", heigh="7")
        self.table.column("#1", anchor=CENTER, width=120)
        self.table.column("#2", anchor=CENTER, width=120)
        self.table.column("#3", anchor=CENTER, width=120)
        self.table.column("#4", anchor=CENTER, width=120)
        self.table.column("#5", anchor=CENTER, width=120)
        self.table.heading("#1", text="lessonId")
        self.table.heading("#2", text="student name")
        self.table.heading("#3", text="date")
        self.table.heading("#4", text="time")
        self.table.heading("#5", text="price")
        self.table.place(x=45, y=100)
        self.listbox()
        self.table.bind('<Button-1>', self.select_line)
        self.btn_last = Button(self, text="last lessons", command=self.open_last_lessons)
        self.btn_last.place(x=75, y=45)
        self.btn_refresh = Button(self, text="refresh", command=self.listbox)
        self.btn_refresh.place(x=175, y=45)
        self.btn_cancel = Button(self, text="cancel lesson", command=self.delete_lesson)
        self.btn_cancel.place(x=115, y=375)
        self.btn_change = Button(self, text="change lesson details", command=self.change_lesson_details)
        self.btn_change.place(x=315, y=375)
        # self.btn_change = Button(self, text="change time", command=self.change_lesson_time)
        # self.btn_change.place(x=315, y=275)
        self.btn_close = Button(self, text="Close", background="red", command=self.close)
        self.btn_close.place(x=650, y=370)


    def listbox(self):
        arr = ["lessons_list", self.parent.parent.id_t]
        str1 = arr[0] + "," + (arr[1])
        print(str1)
        self.parent.parent.parent.client_socket.send(str1.encode())
        data = self.parent.parent.parent.client_socket.recv(1024).decode()
        print(data)
        arr_data = data.split("-")
        print(arr_data)
        line1 = arr_data[0].split(",")
        print(line1)
        for item in arr_data:
            student_id = line1[2]
            print(student_id)
            arr2 = ["student_id_to_name", student_id]
            str2 = arr2[0] + "," + arr2[1]
            self.parent.parent.parent.client_socket.send(str2.encode())
            student_name = self.parent.parent.parent.client_socket.recv(1024).decode()
            print("student name: " + student_name)
            line1 = item.split(",")
            self.table.insert("", 'end', text="1", values=(line1[0], student_name, line1[3], line1[4], line1[5]))


    def select_line(self, event):
        curItem = self.table.focus()
        print(curItem)
        print(self.table.item(curItem)['values'])
        self.x = self.table.item(curItem)['values']
        self.lesson_id = self.x[0]
        print(self.lesson_id)
        self.date = self.x[2]
        print(self.date)
        self.time = self.x[3]
        print(self.time)



    def open_last_lessons(self):
        window = LastLessons(self)
        window.grab_set()
        self.withdraw()


    def delete_lesson(self):
        arr = ["delete_lesson_t", self.x[0]]
        print(arr)
        str1 = arr[0] + "," + str(arr[1])
        print(str1)
        self.parent.parent.parent.client_socket.send(str1.encode())
        data = self.parent.parent.parent.client_socket.recv(1024).decode()  # recived success or failed
        print(data)
        if data == "succeed to delete lesson":
            messagebox.showinfo("showinfo", "you deleted lesson successfully")
            self.close()
        if data == "failed to delete lesson":
            messagebox.showerror("error", "error")


    def change_lesson_details(self):
        window = ChangeLessonDetails(self)
        window.grab_set()
        self.withdraw()





    def close(self):
        self.parent.deiconify()
        self.destroy()