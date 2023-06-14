import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from last_lessons_screen import LastLessons
from t_change_lesson_details_screen import TChangeLessonDetails
from students_list_screen import StudentsList
from update_details_screen import UpdateDetails
from chat_teacher import ChatTeacher
from update_teacher_work_hours import UpdateTeacherWorkTime
from datetime import date as d
from PIL import ImageTk, Image




class LessonsList(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        print(self.parent.id_t)
        self.geometry('800x450+350+50')
        self.title('Lessons List Screen')
        Label(self, text="MY LESSONS", fg="#98B4D4", font=('Microsoft YaHei UI Light', 23, 'bold')).place(x=400, y=40)
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
        self.table.place(x=150, y=100)
        self.listbox()
        self.table.bind('<Button-1>', self.select_line)

        #self.config(bg="#ff00b7")

        self.btn_last = Button(self, text="last lessons", command=self.open_last_lessons)
        self.btn_last.place(x=50, y=50)

        self.img3 = Image.open('C://Users//danie//OneDrive//שולחן העבודה//python img//students list btn.png')
        self.resized = self.img3.resize((100, 50), Image.Resampling.LANCZOS)
        self.img_s_list = ImageTk.PhotoImage(self.resized)
        self.btn_s_list = Button(self, text="students list", command=self.open_student_list, image=self.img_s_list)
        self.btn_s_list.place(x=30, y=100)

        self.btn_update_t_details = Button(self, text="update details", command=self.open_update_t_details)
        self.btn_update_t_details.place(x=40, y=200)

        self.img4 = Image.open('C://Users//danie//OneDrive//שולחן העבודה//python img//work days btn.png')
        self.resized = self.img4.resize((100, 50), Image.Resampling.LANCZOS)
        self.img_choose_days = ImageTk.PhotoImage(self.resized)
        self.btn_choose_days = Button(self, text="my days", command=self.open_update_t_work_hours, image=self.img_choose_days)
        self.btn_choose_days.place(x=30, y=250)

        self.img = Image.open('C://Users//danie//OneDrive//שולחן העבודה//python img//refresh btn.png')
        self.resized = self.img.resize((35, 35), Image.Resampling.LANCZOS)
        self.img_refresh = ImageTk.PhotoImage(self.resized)
        self.btn_refresh = Button(self, text="refresh", command=self.refresh, font=('Helvetica bold', 12), image=self.img_refresh)
        self.btn_refresh.place(x=700, y=45)

        self.img2 = Image.open('C://Users//danie//OneDrive//שולחן העבודה//python img//chat.png')
        self.resized2 = self.img2.resize((40, 40), Image.Resampling.LANCZOS)
        self.img_chat = ImageTk.PhotoImage(self.resized2)
        self.btn_chat = Button(self, text="chat", command=self.open_chat_teacher, font=('Helvetica bold', 12),
                                  image=self.img_chat)
        self.btn_chat.place(x=50, y=350)

        self.btn_cancel = Button(self, text="cancel lesson", command=self.delete_lesson)
        self.btn_cancel.place(x=250, y=300)

        self.btn_change = Button(self, text="change lesson details", command=self.change_lesson_details)
        self.btn_change.place(x=400, y=300)

        self.btn_close = Button(self, text="go back", background="red", command=self.close)
        self.btn_close.place(x=650, y=370)


    def listbox(self):
        arr = ["lessons_list", self.parent.id_t]
        str1 = arr[0] + "," + (arr[1])
        print(str1)
        self.parent.parent.send_msg(str1, self.parent.parent.client_socket)
        data = self.parent.parent.recv_msg(self.parent.parent.client_socket)
        print(data)
        arr_data = data.split("-")
        print(arr_data)
        for item in arr_data:
            line1 = item.split(",")
            print(line1)
            student_id = line1[2]
            print(student_id)
            arr2 = ["student_id_to_name", student_id]
            str2 = arr2[0] + "," + arr2[1]
            self.parent.parent.send_msg(str2, self.parent.parent.client_socket)
            student_name = self.parent.parent.recv_msg(self.parent.parent.client_socket)
            print("student name: " + student_name)

            date = line1[3].split("/")
            print(date) #['10', '7', '22']
            month = int(date[0])
            day = int(date[1])
            #year = date[2]
            today_date = str(d.today())
            print(today_date)
            arr_today_date = today_date.split("-")
            print(arr_today_date) #['2023', '04', '07']
            if month >= int(arr_today_date[1]):
                if (month == int(arr_today_date[1]) and day >= int(arr_today_date[2])) or (month > int(arr_today_date[1])):
                    self.table.insert("", 'end', text="1", values=(line1[0], student_name, line1[3], line1[4], line1[5]))


    def select_line(self, event):
        curItem = self.table.focus()
        print(curItem)
        print(self.table.item(curItem)['values'])
        self.x = self.table.item(curItem)['values']
        self.lesson_id = self.x[0]
        print(self.lesson_id)
        self.student_name = self.x[1]
        print(self.student_name)
        self.date = self.x[2]
        print(self.date)
        self.time = self.x[3]
        print(self.time)




    def open_last_lessons(self):
        window = LastLessons(self)
        window.grab_set()
        self.withdraw()


    def open_student_list(self):
        window = StudentsList(self)
        window.grab_set()
        self.withdraw()


    def open_update_t_details(self):
        window = UpdateDetails(self)
        window.grab_set()
        self.withdraw()

    def open_chat_teacher(self):
        window = ChatTeacher(self)
        window.grab_set()
        self.withdraw()

    def open_update_t_work_hours(self):
        window = UpdateTeacherWorkTime(self)
        window.grab_set()
        self.withdraw()

    def refresh(self):
        for item in self.table.get_children():
            self.table.delete(item)
        self.listbox()



    def delete_lesson(self):
        arr = ["delete_lesson", self.x[0]]
        print(arr)
        str1 = arr[0] + "," + str(arr[1])
        print(str1)
        self.parent.parent.send_msg(str1, self.parent.parent.client_socket)
        data = self.parent.parent.recv_msg(self.parent.parent.client_socket)  # recived success or failed
        print(data)
        if data == "succeed to delete lesson":
            messagebox.showinfo("showinfo", "you deleted lesson successfully")
            student_fname = self.parent.student_name.spilt()[0]
            print(student_fname)
            arr2 = ["send_msg_for_student", self.parent.parent.id_t, student_fname, self.cal.get_date(),
                    "lesson's details have changed"]
            str2 = ",".join(arr2)
            self.parent.parent.parent.send_msg(str2, self.parent.parent.parent.client_socket)
            data2 = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
            print(data2)
        if data == "failed to delete lesson":
            messagebox.showerror("error", "error")


    def change_lesson_details(self):
        window = TChangeLessonDetails(self)
        window.grab_set()
        self.withdraw()



    def close(self):
        self.parent.deiconify()
        self.destroy()