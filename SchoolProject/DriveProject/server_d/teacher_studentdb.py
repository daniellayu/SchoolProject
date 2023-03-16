import sqlite3
from studentdb import StudentDb
from teacherdb import TeacherDb

class TeacherStudentDb(object):
    def __init__(self, tablename="TeacherStudentDb"):#, teacherStudentId="teacherStudentId", teacherId="teacherId", studentId="studentId"):
        self.__tablename = tablename
        self.studentdb = StudentDb()
        self.teacherdb = TeacherDb()
        # self.__teacherStudentId = teacherStudentId
        # self.__teacherId = teacherId
        # self.__studentId = studentId
        # self.create_table()

    # def create_table(self):
    #     try:
    #         connection = sqlite3.connect("database.db")
    #         cursor = connection.cursor()
    #         create_table_query = f"""
    #                 CREATE TABLE IF NOT EXISTS {self.__tablename} (
    #                     {self.__teacherStudentId} INTEGER PRIMARY KEY,
    #                     {self.__teacherId} INTEGER NOT NULL,
    #                     {self.__studentId} INTEGER NOT NULL
    #                 );
    #                         """
    #         cursor.execute(create_table_query)
    #         connection.commit()
    #         connection.close()
    #         print("succeed to create table TeacherStudentDb")
    #         return True
    #     except:
    #         print("failed to create table TeacherStudentDb")
    #         return False


    def get_teacher_id_by_name(self, teacher_name):
        try:
            conn = sqlite3.connect('database.db')
            print("Opened database successfully")
            str = f"SELECT {self.__teacherId} from {self.__tablename} where {self.__firstname} = '{teacher_name}'"
            print(str)
            cursor = conn.execute(str)
            row = cursor.fetchall()
            if row:
                print(row[0][0])
                return row[0][0]
            else:
                print("teacher not found")
                return False
        except:
            return "failed to get teacher id by name"


    def get_all_students(self):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            select_query = f"SELECT {self.__studentId}, {self.__firstname}, {self.__lastname}, {self.__email}, {self.__phonenumber}, {self.__Id} FROM {self.__tablename}"
            cursor.execute(select_query)
            students = cursor.fetchall()
            connection.close()
            print("succeed to get all students")
            return students
        except:
            print("failed to get all students")
            return False