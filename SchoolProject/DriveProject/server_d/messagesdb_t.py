import sqlite3

class MessagesDb(object):
    def __init__(self, tablename="MessagesDb", messageId="messageId", from_id="from_id", to_id="to_id",
                 date="date", text="text"):
        self.__tablename = tablename
        self.__messageId = messageId
        self.__from_id = from_id
        self.__to_id = to_id
        self.__date = date
        self.__text = text
        self.create_table()

    def create_table(self):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            create_table_query = f"""
                    CREATE TABLE IF NOT EXISTS {self.__tablename} (
                        {self.__messageId} INTEGER PRIMARY KEY,
                        {self.__from_id} INTEGER NOT NULL,
                        {self.__to_id} INTEGER NOT NULL,
                        {self.__date} TEXT NOT NULL,
                        {self.__text} TEXT NOT NULL
                    );
                            """
            cursor.execute(create_table_query)
            connection.commit()
            connection.close()
            print("succeed to create table MessagesDb")
            return True
        except:
            print("failed to create table MessagesDb")
            return False


    def insert(self, from_id, to_id, date, text):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            insert_query = f"INSERT INTO {self.__tablename} ({self.__from_id}, {self.__to_id}," \
                           f" {self.__date}, {self.__text}" \
                           f" ) VALUES (?, ?, ?, ?)"
            cursor.execute(insert_query, (from_id, to_id, date, text))
            connection.commit()#release db
            connection.close()
            print("succeed to insert message")
            return True
        except:
            print("failed to insert message")
            return False


    def delete_message(self, message_id):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            delete_query = f"DELETE FROM {self.__tablename} WHERE {self.__messageId} = ?"
            cursor.execute(delete_query, (message_id,))
            connection.commit()
            connection.close()
            print("succeed to delete message by id")
            return True
        except:
            print("failed to delete message by id")
            return False


    def get_all_messages_for_teacher(self, to_id):
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            select_query = f"SELECT * FROM {self.__tablename} WHERE {self.__to_id} = {to_id}"
            cursor.execute(select_query)
            teachers = cursor.fetchall()
            connection.close()
            print("succeed to get messages")
            return teachers
        except:
            print("failed to get messages")
            return False


#m = MessagesDb()
#m.insert(1, 2, "1/6/2023", "hello")
#m.delete_message(3)