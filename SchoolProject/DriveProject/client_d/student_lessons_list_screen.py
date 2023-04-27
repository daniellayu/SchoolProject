import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from last_lessons_screen import LastLessons
from change_lesson_details_screen import ChangeLessonDetails
from choose_teacher_screen import ChooseTeacher
from insert_lesson_screen import InsertLesson
from chat_student import ChatStudent
from PIL import ImageTk, Image



class StudentLessonsList(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('800x450')
        self.title('Student Lessons List Screen')
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
        self.table.place(x=150, y=100)
        self.listbox()
        self.table.bind('<Button-1>', self.select_line)

        self.btn_last = Button(self, text="last lessons", command=self.open_last_lessons)
        self.btn_last.place(x=50, y=120)

        self.btn_choose_t = Button(self, text="choose teacher", command=self.open_choose_teacher)
        self.btn_choose_t.place(x=50, y=170)

        self.btn_insert_lesson = Button(self, text="insert lesson", command=self.open_insert_lesson)
        self.btn_insert_lesson.place(x=50, y=220)

        self.img = Image.open('C://Users//danie//OneDrive//שולחן העבודה//python img//refresh btn.png')
        self.resized = self.img.resize((35, 35), Image.Resampling.LANCZOS)
        self.img_refresh = ImageTk.PhotoImage(self.resized)
        self.btn_refresh = Button(self, text="refresh", command=self.refresh, font=('Helvetica bold', 12),
                                  image=self.img_refresh)
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

        self.btn_close = Button(self, text="Close", background="red", command=self.close)
        self.btn_close.place(x=650, y=370)


    def listbox(self):
        arr = ["student_lessons_list", self.parent.id_s]
        str1 = arr[0] + "," + (arr[1])
        print(str1)
        self.parent.parent.client_socket.send(str1.encode())
        data = self.parent.parent.client_socket.recv(1024).decode()
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
            self.parent.parent.client_socket.send(str2.encode())
            teacher_name = self.parent.parent.client_socket.recv(1024).decode()
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
        window = LastLessons(self)
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

    def open_chat_teacher(self):
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
        self.parent.parent.client_socket.send(str1.encode())
        data = self.parent.parent.client_socket.recv(1024).decode()  # recived success or failed
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