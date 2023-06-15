import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from s_change_lesson_details_screen import SChangeLessonDetails
from choose_teacher_screen import ChooseTeacher
from insert_lesson_screen import InsertLesson
from student_last_lessons_screen import StudentLastLessons
from chat_student import ChatStudent
from PIL import ImageTk, Image



class StudentLessonsList(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('800x400+350+50')
        self.title('Student Lessons List Screen')
        Label(self, text="MY LESSONS", fg="#98B4D4", font=('Microsoft YaHei UI Light', 23, 'bold')).place(x=370, y=40)

        self.table = ttk.Treeview(self, columns=("c1", "c2", "c3", "c4", "c5"), show="headings", heigh="7")
        self.table.column("#1", anchor=CENTER, width=120)
        self.table.column("#2", anchor=CENTER, width=120)
        self.table.column("#3", anchor=CENTER, width=120)
        self.table.column("#4", anchor=CENTER, width=120)
        self.table.column("#5", anchor=CENTER, width=120)
        self.table.heading("#1", text="lessonId")
        self.table.heading("#2", text="teacher name")
        self.table.heading("#3", text="date")
        self.table.heading("#4", text="time")
        self.table.heading("#5", text="price")
        self.table.place(x=170, y=100)
        self.table.bind('<Button-1>', self.select_line)

        self.btn_last = Button(self, text="last lessons", fg='white', bg='#f6b26b',
                               font=('Microsoft YaHei UI Light', 11, 'bold'), command=self.open_last_lessons)
        self.btn_last.place(x=20, y=100)

        self.btn_choose_t = Button(self, text="choose teacher", fg='white', bg='#93c47d',
                               font=('Microsoft YaHei UI Light', 11, 'bold'), command=self.open_choose_teacher)
        self.btn_choose_t.place(x=20, y=150)

        self.btn_insert_lesson = Button(self, text="insert lesson", fg='white', bg='#CC9999',
                               font=('Microsoft YaHei UI Light', 11, 'bold'), command=self.open_insert_lesson)
        self.btn_insert_lesson.place(x=20, y=200)

        self.img = Image.open('C://Users//danie//OneDrive//שולחן העבודה//python img//refresh btn.png')
        self.resized = self.img.resize((35, 35), Image.Resampling.LANCZOS)
        self.img_refresh = ImageTk.PhotoImage(self.resized)
        self.btn_refresh = Button(self, text="refresh", command=self.refresh, fg='white',
                               font=('Microsoft YaHei UI Light', 11, 'bold'),
                                  image=self.img_refresh)
        self.btn_refresh.place(x=700, y=45)

        self.img2 = Image.open('C://Users//danie//OneDrive//שולחן העבודה//python img//chat.png')
        self.resized2 = self.img2.resize((40, 40), Image.Resampling.LANCZOS)
        self.img_chat = ImageTk.PhotoImage(self.resized2)
        self.btn_chat = Button(self, text="chat", command=self.open_chat_student, fg='white',
                               font=('Microsoft YaHei UI Light', 11, 'bold'),
                               image=self.img_chat)
        self.btn_chat.place(x=50, y=320)

        self.btn_cancel = Button(self, text="cancel lesson", fg='white', bg='#e06666',
                               font=('Microsoft YaHei UI Light', 11, 'bold'), command=self.delete_lesson)
        self.btn_cancel.place(x=250, y=320)

        self.btn_change = Button(self, text="change lesson details", fg='white', bg='#ffe599',
                               font=('Microsoft YaHei UI Light', 11, 'bold'), command=self.change_lesson_details)
        self.btn_change.place(x=400, y=320)

        self.btn_close = Button(self, text="go back", background="red", command=self.close)
        self.btn_close.place(x=650, y=320)

        self.listbox()



    def listbox(self):
        arr = ["student_lessons_list", self.parent.id_s]
        str1 = arr[0] + "," + (arr[1])
        print(str1)
        self.parent.parent.send_msg(str1, self.parent.parent.client_socket)
        data = self.parent.parent.recv_msg(self.parent.parent.client_socket)
        print(data)
        arr_data = data.split("-")
        print(arr_data)
        line1 = arr_data[0].split(",")
        print(line1)
        for item in arr_data:
            teacher_id = line1[1]
            print(teacher_id)
            arr2 = ["teacher_id_to_name", teacher_id]
            str2 = arr2[0] + "," + arr2[1]
            self.parent.parent.send_msg(str2, self.parent.parent.client_socket)
            teacher_name = self.parent.parent.recv_msg(self.parent.parent.client_socket)
            print("teacher name: " + teacher_name)
            line1 = item.split(",")
            self.table.insert("", 'end', text="1", values=(line1[0], teacher_name, line1[3], line1[4], line1[5]))
            self.price = line1[5]


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
        window = StudentLastLessons(self)
        window.grab_set()
        self.withdraw()


    def open_choose_teacher(self):
        window = ChooseTeacher(self)
        window.grab_set()
        self.withdraw()


    def open_insert_lesson(self):
        window = InsertLesson(self)
        window.grab_set()
        self.withdraw()

    def open_chat_student(self):
        window = ChatStudent(self)
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
            arr2 = ["send_msg_for_teacher", self.parent.parent.id_s, self.cal.get_date(),
                    "lesson's details have changed"]
            str2 = ",".join(arr2)
            self.parent.parent.parent.send_msg(str2, self.parent.parent.parent.client_socket)
            data2 = self.parent.parent.parent.recv_msg(self.parent.parent.parent.client_socket)
            print(data2)
        if data == "failed to delete lesson":
            messagebox.showerror("error", "error")


    def change_lesson_details(self):
        window = SChangeLessonDetails(self)
        window.grab_set()
        self.withdraw()


    def close(self):
        self.parent.deiconify()
        self.destroy()