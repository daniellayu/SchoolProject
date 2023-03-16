import sqlite3

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
            print("0")
            insert_query = f"INSERT INTO {self.__tablename} ({self.__firstname}, {self.__lastname}," \
                           f" {self.__email}, {self.__password}, {self.__phonenumber}, {self.__Id}, {self.__teacherId}" \
                           f" ) VALUES (?, ?, ?, ?, ?, ?, ?)"
            print("1")
            cursor.execute(insert_query, (firstname, lastname, email, password, phonenumber, Id, 0))
            print("w")
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

    def get_students_by_teacher_id1(self, teacher_id):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            select_query = f"SELECT {self.__studentId}, {self.__firstname}, {self.__lastname}, {self.__email}, {self.__phonenumber}, {self.__Id} FROM {self.__tablename} WHERE {self.__teacherId} = '{teacher_id}'"
            cursor.execute(select_query)
            students = cursor.fetchall()
            connection.close()
            print("succeed to get students by teacher id")
            return students
        except:
            print("failed to get students by teacher id")
            return False

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
        str_check = "SELECT * from " + self.__tablename + " where " + self.__Id + " = '" +id +"' and " +self.__password+" = '"+str(password)+"'"
        print(str_check)
        cursor = conn.execute(str_check)
        row = cursor.fetchall()
        if row:
            print("student exist")
            return True
        else:
            print("student not exist")
            return False

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




#s = StudentDb()
#s.insert("ana", "cohen", "anacgmail", "ana123", "05224", "32456")
#x = s.get_all_students()
#x = s.get_students_by_teacher_id("dani1")
#print(x)
#s.delete_by_id(1)
#s.update_teacher_id(2, 32456)
#s.get_student_name_by_id(12)