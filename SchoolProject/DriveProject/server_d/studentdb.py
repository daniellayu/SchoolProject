import sqlite3
import hashlib

class StudentDb(object):
    def __init__(self, tablename="StudentDb", studentId="studentId", firstname="firstname", lastname="lastname",
                 email="email",password="password", phonenumber="phonenumber", Id="Id", teacherId= "teacherId"):
        self.__tablename = tablename
        self.__studentId = studentId
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__password = password
        self.__phonenumber = phonenumber
        self.__Id = Id
        self.__teacherId = teacherId
        self.create_table()

    def create_table(self):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            create_table_query = f"""
                    CREATE TABLE IF NOT EXISTS {self.__tablename} (
                        {self.__studentId} INTEGER PRIMARY KEY,
                        {self.__firstname} TEXT NOT NULL,
                        {self.__lastname} TEXT NOT NULL,
                        {self.__email} TEXT NOT NULL UNIQUE,
                        {self.__password} TEXT NOT NULL,
                        {self.__phonenumber} TEXT NOT NULL,
                        {self.__Id} INTEGER NOT NULL,
                        {self.__teacherId} INTEGER NOT NULL
                    );
                            """
            cursor.execute(create_table_query)
            connection.commit()
            connection.close()
            print("succeed to create table StudentDb")
            return True
        except:
            print("failed to create table StudentDb")
            return False


    def insert(self, firstname, lastname, email, password, phonenumber, Id):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            salt = "PYTHON"
            md5hash = hashlib.md5(salt.encode('utf-8') + password.encode()).hexdigest()
            insert_query = f"INSERT INTO {self.__tablename} ({self.__firstname}, {self.__lastname}," \
                           f" {self.__email}, {self.__password}, {self.__phonenumber}, {self.__Id}, {self.__teacherId}" \
                           f" ) VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(insert_query, (firstname, lastname, email, str(md5hash), phonenumber, Id, 0))
            connection.commit()#release db
            connection.close()
            print("succeed to insert student")
            return True
        except:
            print("failed to insert student")
            return False



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

    # def get_students_by_teacher_id1(self, teacher_id):
    #     try:
    #         connection = sqlite3.connect("database.db")
    #         cursor = connection.cursor()
    #         select_query = f"SELECT {self.__studentId}, {self.__firstname}, {self.__lastname}, {self.__email}, {self.__phonenumber}, {self.__Id} FROM {self.__tablename} WHERE {self.__teacherId} = '{teacher_id}'"
    #         cursor.execute(select_query)
    #         students = cursor.fetchall()
    #         connection.close()
    #         print("succeed to get students by teacher id")
    #         return students
    #     except:
    #         print("failed to get students by teacher id")
    #         return False

    def get_students_by_teacher_id(self, teacher_id):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            select_query = f"SELECT {self.__studentId}, {self.__firstname}, {self.__lastname}, {self.__email}, {self.__phonenumber}, {self.__Id} FROM {self.__tablename} WHERE {self.__teacherId} = {teacher_id}"
            cursor.execute(select_query)
            students = cursor.fetchall()
            connection.close()
            if students:
                print("succeed to get students by teacher id")
                return students
            else:
                return "No students found for this teacher."
        except:
            print("failed to get students by teacher id")
            return False



    def delete_by_id(self, student_id):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            delete_query = f"DELETE FROM {self.__tablename} WHERE {self.__studentId} = ?"
            cursor.execute(delete_query, (student_id,))
            connection.commit()
            connection.close()
            print("succeed to delete student by id")
            return True
        except:
            print("failed to delete student by id")
            return False

    def is_exist(self, id, password):
        conn = sqlite3.connect('database.db')
        print("Opened database successfully")
        salt = "PYTHON"
        md5hash = hashlib.md5(salt.encode('utf-8') + password.encode()).hexdigest()
        str_check = "SELECT * from " + self.__tablename + " where " + self.__Id + " = '" +id +"' and " +self.__password+" = '"+str(md5hash)+"'"
        print(str_check)
        cursor = conn.execute(str_check)
        row = cursor.fetchall()
        if row:
            print("student exist")
            return True
        else:
            print("student not exist")
            return False

    # def is_id_exist(self, id):
    #     try:
    #         conn = sqlite3.connect('database.db')
    #         print("Opened database successfully")
    #         str_check = f"SELECT * from {self.__tablename} where {self.__Id} = {id}"
    #         print(str_check)
    #         cursor = conn.execute(str_check)
    #         row = cursor.fetchall()
    #         if row:
    #             print("student already exists")
    #             return True
    #     except:
    #         print("student doesn't exists")
    #         return False

    def update_teacher_id(self, teacher_id, id):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            update_query = f"UPDATE {self.__tablename} SET {self.__teacherId} = {teacher_id} WHERE {self.__Id} = {id}"
            print(update_query)
            cursor.execute(update_query)
            connection.commit()
            connection.close()
            print("succeed to update teacher by id")
            return True
        except:
            print("failed to update teacher by id")
            return False


    def get_student_name_by_id(self, student_id):
        try:
            conn = sqlite3.connect('database.db')
            print("Opened database successfully")
            str = f"SELECT {self.__firstname}, {self.__lastname} from {self.__tablename} where {self.__studentId} = {student_id}"
            print(str)
            cursor = conn.execute(str)
            row = cursor.fetchall()
            if row:
                print(row[0][0] + " " + row[0][1])
                return row[0][0] + " " + row[0][1]
            else:
                print("student not found")
                return False
        except:
            return "failed to get student name by id"


    #student_id as PRIMARY KEY and id as ID
    def get_student_id_by_id(self, id):
        try:
            conn = sqlite3.connect('database.db')
            print("Opened database successfully")
            str = f"SELECT {self.__studentId} from {self.__tablename} where {self.__Id} = '{id}'"
            print(str)
            cursor = conn.execute(str)
            row = cursor.fetchall()
            if row:
                print(row[0][0])
                return row[0][0]
            else:
                print("student not found")
                return False
        except:
            return "failed to get student id by id"


    # teacher id and student id as PRIMARY KEY
    def get_teacher_id_by_student_id(self, student_id):
        try:
            conn = sqlite3.connect('database.db')
            print("Opened database successfully")
            str = f"SELECT {self.__teacherId} from {self.__tablename} where {self.__studentId} = '{student_id}'"
            print(str)
            cursor = conn.execute(str)
            row = cursor.fetchall()
            if row:
                print(row[0][0])
                return row[0][0]
            else:
                print("student not found")
                return False
        except:
            return "failed to get teacher id by student id"



    def get_student_id_by_name(self, student_name):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            select_query = f"SELECT {self.__studentId} FROM {self.__tablename} " \
                           f"WHERE {self.__firstname} = ?"
            print(select_query)
            cursor.execute(select_query, (student_name,))
            result = cursor.fetchone()
            connection.close()
            if result is not None:
                student_id = result[0]
                print("Succeed to get student ID by name")
                print(student_id)
                return student_id
            else:
                print("Student not found")
                return None
        except:
            print("Failed to get student ID by name")
            return None


#s = StudentDb()
#s.insert("gaya", "tamari", "gaya@", "gaya12", "05224", "12")
#x = s.get_all_students()
#x = s.get_students_by_teacher_id("dani1")
#print(x)
#s.delete_by_id(1)
#s.update_teacher_id(2, 32456)
#s.get_student_name_by_id(2)
#s.get_student_id_by_id(12)
#s.get_teacher_id_by_student_id(2)
#s.get_student_id_by_name("gaya")