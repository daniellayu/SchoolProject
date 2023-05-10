import sqlite3

class MessagesDb(object):
    def __init__(self, tablename="MessagesDb", messageId="messageId", from_id="from_id", to_id="to_id", date="date",
                 text="text"):
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
            insert_query = f"""
                    INSERT INTO {self.__tablename} 
                    ({self.__from_id}, {self.__to_id}, {self.__date}, {self.__text}) 
                    VALUES (?, ?, ?, ?)
                """
            cursor.execute(insert_query, (from_id, to_id, date, text))
            connection.commit()
            connection.close()
            print("Message inserted successfully")
            return True
        except:
            print("Failed to insert message")
            return False




m = MessagesDb
m.insert(1, 2, "3/4/2023", "delete", "r")