import sqlite3

class LessonsDb(object):
    def __init__(self, tablename="LessonsDb", lessonId="lessonId", teacherId="teacherId", studentId="studentId", date="date", time="time", price="price"):
        self.__tablename = tablename
        self.__lessonId = lessonId
        self.__teacherId = teacherId
        self.__studentId = studentId
        self.__date = date
        self.__time = time
        self.__price = price
        self.create_table()

    def create_table(self):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            create_table_query = f"""
                    CREATE TABLE IF NOT EXISTS {self.__tablename} (
                        {self.__lessonId} INTEGER PRIMARY KEY,
                        {self.__teacherId} INTEGER NOT NULL,
                        {self.__studentId} INTEGER NOT NULL,
                        {self.__date} TEXT NOT NULL,
                        {self.__time} TEXT NOT NULL,
                        {self.__price} INTEGER NOT NULL
                    );
                            """
            cursor.execute(create_table_query)
            connection.commit()
            connection.close()
            print("succeed to create table LessonsDb")
            return True
        except:
            print("failed to create table LessonsDb")
            return False

    def insert_lesson(self, teacherId, studentId, date, time, price):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            insert_query = f"INSERT INTO {self.__tablename} ({self.__teacherId}, {self.__studentId}," \
                           f" {self.__date}, {self.__time}, {self.__price}" \
                           f" ) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(insert_query, (teacherId, studentId, date, time, price))
            connection.commit()#release db
            connection.close()
            print("succeed to insert lesson")
            return True
        except:
            print("failed to insert lesson")
            return False


    def get_all_lessons(self):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            select_query = f"SELECT * FROM {self.__tablename}"
            cursor.execute(select_query)
            teachers = cursor.fetchall()
            connection.close()
            print("succeed to get all lessons")
            return teachers
        except:
            print("failed to get all lessons")
            return False


    def get_lessons_by_teacher_id(self, teacher_id):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            select_query = f"SELECT * FROM {self.__tablename} WHERE {self.__teacherId} = {teacher_id}"
            cursor.execute(select_query)
            teachers = cursor.fetchall()
            connection.close()
            print("succeed to get all lessons")
            return teachers
        except:
            print("failed to get all lessons")
            return False


    def get_lessons_by_student_id(self, student_id):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            select_query = f"SELECT * FROM {self.__tablename} WHERE {self.__studentId} = {student_id}"
            cursor.execute(select_query)
            students = cursor.fetchall()
            connection.close()
            print("succeed to get all lessons")
            print(students)
            return students
        except:
            print("failed to get all lessons")
            return False



    def delete_lesson_by_id(self, lesson_id):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            delete_query = f"DELETE FROM {self.__tablename} WHERE {self.__lessonId} = {lesson_id}"
            cursor.execute(delete_query)
            connection.commit()
            connection.close()
            print("Succeed to delete lesson by id")
            return True
        except:
            print("Failed to delete lesson by id")
            return False

    def change_lesson_details(self, lesson_id, date, time):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            update_query = f"UPDATE {self.__tablename} SET {self.__date} = ?, {self.__time} = ? WHERE {self.__lessonId} = ?"
            cursor.execute(update_query, (date, time, lesson_id))
            connection.commit()
            connection.close()
            print("succeeded to update date")
            return True
        except:
            print("failed to update date")
            return False


    def update_time(self, lesson_id, time):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            update_query = f"UPDATE {self.__tablename} SET {self.__time} = ? WHERE {self.__lessonId} = ?"
            cursor.execute(update_query, (time, lesson_id))
            connection.commit()
            connection.close()
            print("succeeded to update time")
            return True
        except:
            print("failed to update time")
            return False




#l = LessonsDb()
#l.insert_lesson("3", "2", "13.4.2022", "10:00", "180")
#l.insert_lesson("3", "1", "4.5.2022", "15:30", "170")
#x = l.get_all_lessons()
#print(x)
#y = l.get_price()
#print(y)
#print(x[0][0])#1
#l.delete_lesson_by_id(15)
#l.update_date(3, "08.09.2022")
#l.update_time(4, "14:00")
#l.get_lessons_by_teacher_id(3)
#l.change_lesson_details(7, "6.12.2022", "12:20")
#l.get_lessons_by_student_id(2)