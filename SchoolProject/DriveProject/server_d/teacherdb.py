import sqlite3

class TeacherDb(object):
    def __init__(self, tablename="teacherDb", teacherId="teacherId", firstname="firstname", lastname="lastname", email="email", phonenumber="phonenumber", Id="Id", password="password", price="price", experience="experience", days="days", hours="hours"):
        self.__tablename = tablename
        self.__teacherId = teacherId #auto increment
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__password = password
        self.__phonenumber = phonenumber
        self.__Id = Id
        self.__price = price
        self.__experience = experience
        self.__days = days
        self.__hours = hours
        self.create_table()


    def create_table(self):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            create_table_query = f"""
                    CREATE TABLE IF NOT EXISTS {self.__tablename} (
                        {self.__teacherId} INTEGER PRIMARY KEY,
                        {self.__firstname} TEXT NOT NULL,
                        {self.__lastname} TEXT NOT NULL,
                        {self.__email} TEXT NOT NULL UNIQUE,
                        {self.__password} TEXT NOT NULL,
                        {self.__phonenumber} TEXT NOT NULL,
                        {self.__Id} INTEGER NOT NULL,
                        {self.__price} INTEGER NOT NULL,
                        {self.__experience} INTEGER NOT NULL,
                        {self.__days} TEXT NOT NULL,
                        {self.__hours} TEXT NOT NULL
                    );
                            """
            cursor.execute(create_table_query)
            connection.commit()
            connection.close()
            print("succeed to create table TeacherDb")
            return True
        except:
            print("failed to create table TeacherDb")
            return False

    def insert(self, firstname, lastname, email, password, phonenumber, Id, price, experience):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            insert_query = f"INSERT INTO {self.__tablename} ({self.__firstname}, {self.__lastname}," \
                           f" {self.__email}, {self.__password}, {self.__phonenumber}, {self.__Id}, {self.__price}," \
                       f" {self.__experience}, {self.__days}) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(insert_query, (firstname, lastname, email, password, phonenumber, Id, price, experience, ""))
            connection.commit()#release db
            connection.close()
            print("succeed to insert teacher")
            return True
        except:
            print("failed to insert teacher")
            return False

    def get_all_teachers(self):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            select_query = f"SELECT * FROM {self.__tablename}"
            cursor.execute(select_query)
            teachers = cursor.fetchall()
            connection.close()
            print("succeed to get all teachers")
            return teachers
        except:
            print("failed to get all teachers")
            return False

    def delete_by_id(self, teacher_id):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            delete_query = f"DELETE FROM {self.__tablename} WHERE {self.__teacherId} = ?"
            cursor.execute(delete_query, (teacher_id,))
            connection.commit()
            connection.close()
            print("succeed to delete teacher by id")
            return True
        except:
            print("failed to delete teacher by id")
            return False

    def update_by_id(self, id, price, experience):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            update_query = f"UPDATE {self.__tablename} SET {self.__price} = {price}, {self.__experience} = {experience} WHERE {self.__Id} = {id}"
            cursor.execute(update_query)
            connection.commit()
            connection.close()
            print("succeed to update teacher by id")
            return True
        except:
            print("failed to update teacher by id")
            return False

    def is_exist(self, id, password):
        try:
            conn = sqlite3.connect('database.db')
            print("Opened database successfully")
            str_check = "SELECT * from " + self.__tablename + " where " + self.__Id + " = '" +id +"' and " +self.__password+" = '"+str(password)+"'"
            print(str_check)
            cursor = conn.execute(str_check)
            row = cursor.fetchall()
            if row:
                print("teacher exist")
                return True
        except:
            print("teacher not exist")
            return False


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


    #teacher_id as PRIMARY KEY and id as ID
    def get_teacher_id_by_id(self, id):
        try:
            conn = sqlite3.connect('database.db')
            print("Opened database successfully")
            str = f"SELECT {self.__teacherId} from {self.__tablename} where {self.__Id} = '{id}'"
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
            return "failed to get teacher id by id"



    def get_teacher_name_by_id(self, teacher_id):
        try:
            conn = sqlite3.connect('database.db')
            print("Opened database successfully")
            str = f"SELECT {self.__firstname}, {self.__lastname} from {self.__tablename} where {self.__teacherId} = {teacher_id}"
            print(str)
            cursor = conn.execute(str)
            row = cursor.fetchall()
            if row:
                print(row[0][0] + " " + row[0][1])
                return row[0][0] + " " + row[0][1]
            else:
                print("teacher not found")
                return False
        except:
            return "failed to get teacher name by id"


    def update_days(self, teacher_id, days):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            update_query = f"UPDATE {self.__tablename} SET {self.__days} = ? WHERE {self.__teacherId} = ?"
            print(update_query)
            cursor.execute(update_query, (days, teacher_id))
            connection.commit()
            connection.close()
            print("succeed to update teacher's days")
            return True
        except:
            print("failed to update teacher's days")
            return False


    def get_teacher_days_by_Id(self, teacher_id):
        try:
            conn = sqlite3.connect('database.db')
            print("Opened database successfully")
            str = f"SELECT {self.__days} from {self.__tablename} where {self.__teacherId} = '{teacher_id}'"
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
            return "failed to get teacher's days"


    def update_hours(self, teacher_id, hours):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            update_query = f"UPDATE {self.__tablename} SET {self.__hours} = ? WHERE {self.__teacherId} = ?"
            print(update_query)
            cursor.execute(update_query, (hours, teacher_id))
            connection.commit()
            connection.close()
            print("succeed to update teacher's hours")
            return True
        except:
            print("failed to update teacher's hours")
            return False

    def get_teacher_hours_by_Id(self, teacher_id):
        try:
            conn = sqlite3.connect('database.db')
            print("Opened database successfully")
            str = f"SELECT {self.__hours} from {self.__tablename} where {self.__teacherId} = '{teacher_id}'"
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
            return "failed to get teacher's hours"


#t = TeacherDb()
#t.insert("dani1", "yusu1", "danngi23", "p1", "34551", "1231", "1501", "31")
#x = t.get_all_teachers()
#print(x)
#print(x[0][0])#1
#t.delete_by_id(1)
#t.update_by_id(1, 160, 11)
#t.get_teacher_id_by_name("q") #2
#t.get_teacher_name_by_id(3)
#t.get_teacher_id_by_id(144)
#t.update_days(1, "sunday")
#t.get_teacher_days_by_Id(144)

