import socket
import threading
from teacherdb import TeacherDb
from studentdb import StudentDb
from lessonsdb import LessonsDb
from messagesdb_s import MessagesDb_Students
from messagesdb_t import MessagesDb


SIZE = 12


class Server(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.count = 0
        self.running = True
        self.teacherdb = TeacherDb()
        self.studentdb = StudentDb()
        self.lessonsdb = LessonsDb()
        self.messagesdb_s = MessagesDb_Students()
        self.messagesdb_t = MessagesDb()




    def start(self):
        try:
            print('server starting up on ip %s port %s' % (self.ip, self.port))
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((self.ip, self.port))
            sock.listen()
            while True:
                print('waiting for a new client')
                clientSocket, client_address = sock.accept()
                print('new client entered')
                clientSocket.send('Hello this is server'.encode())
                self.count += 1
                print(self.count)
                # implement here your main logic
                self.handleClient(clientSocket, self.count)
        except socket.error as e:
            print(e)





    def handleClient(self, clientSock, current):
        client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, current,))
        client_handler.start()

    def handle_client_connection(self, client_socket, current):
        while self.running:
            server_data = self.recv_msg(client_socket)
            if not server_data:  # client disconnected
                break
            arr = server_data.split(",")
            print(arr)
            if arr and len(arr) == 9 and arr[0] == "sign_up_teacher":
                server_data = self.teacherdb.insert(arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8])
                print("Server data: ", server_data)
                if server_data:
                    self.send_msg("success Sign up teacher", client_socket)
                elif server_data:
                    self.send_msg("failed Sign up teacher", client_socket)

            elif arr and len(arr) == 7 and arr[0] == "sign_up_student":
                server_data = self.studentdb.insert(arr[1], arr[2], arr[3], arr[4], arr[5], arr[6])
                print("Server data: ", server_data)
                if server_data:
                    self.send_msg("success Sign up student", client_socket)
                elif server_data:
                    self.send_msg("failed Sign up student", client_socket)

            elif arr and len(arr) == 3 and arr[0] == "sign_in_teacher":
                server_data = self.teacherdb.is_exist(arr[1], arr[2])
                print("Server data: ", server_data)  # true or false
                if server_data:
                    self.send_msg("success Sign in", client_socket)
                elif server_data:
                    self.send_msg("failed Sign in", client_socket)

            elif arr and len(arr) == 3 and arr[0] == "sign_in_student":
                server_data = self.studentdb.is_exist(arr[1], arr[2])
                print("Server data: ", server_data)
                if server_data == True:
                    self.send_msg("success Sign in", client_socket)
                if server_data == False:
                    self.send_msg("failed Sign in", client_socket)

            elif arr and len(arr) == 2 and arr[0] == "students_list":
                server_data = self.teacherdb.get_teacher_id_by_id(arr[1])
                print("Server data: ", server_data)
                server_data2 = self.studentdb.get_students_by_teacher_id(server_data)
                print("Server data2: ", server_data2)
                # Use list comprehension to join each tuple with the delimiter
                string_data2 = '-'.join([','.join(map(str, item)) for item in server_data2])
                print(string_data2)
                self.send_msg(string_data2, client_socket)

            elif arr and len(arr) == 2 and arr[0] == "lessons_list":
                server_data = self.teacherdb.get_teacher_id_by_id(arr[1])
                print("Server data: ", server_data)
                server_data2 = self.lessonsdb.get_lessons_by_teacher_id(server_data)
                print("Server data2: ", server_data2)
                # Use list comprehension to join each tuple with the delimiter
                string_data = '-'.join([','.join(map(str, item)) for item in server_data2])
                print(string_data)
                self.send_msg(string_data, client_socket)

            elif arr and len(arr) == 2 and arr[0] == "student_id_to_name":
                server_data = self.studentdb.get_student_name_by_id(arr[1])
                print("Server data: ", server_data)
                self.send_msg(server_data, client_socket)

            elif arr and len(arr) == 4 and arr[0] == "update_details":
                # server_data = self.teacherdb.get_teacher_id_by_name(arr[1])
                # print("Server data: ", server_data)
                server_data = self.teacherdb.update_by_id(arr[1], arr[2], arr[3]) #return false
                print("Server data: ", server_data)
                if server_data:
                    self.send_msg("success update details", client_socket)
                elif server_data:
                    self.send_msg("failed update details", client_socket)

            elif arr and len(arr) == 1 and arr[0] == "teachers_list":
                server_data = self.teacherdb.get_all_teachers()
                print("Server data: ", server_data)
                # Use list comprehension to join each tuple with the delimiter
                string_data = '-'.join([','.join(map(str, item)) for item in server_data])
                print(string_data)
                self.send_msg(string_data, client_socket)

            elif arr and len(arr) == 3 and arr[0] == "update_teacher_id":
                server_data = self.studentdb.update_teacher_id(arr[1], arr[2])
                print("Server data: ", server_data)
                if server_data:
                    self.send_msg("success update teacher id", client_socket)
                elif server_data:
                    self.send_msg("failed update teacher id", client_socket)

            elif arr and len(arr) == 2 and arr[0] == "student_lessons_list":
                server_data = self.studentdb.get_student_id_by_id(arr[1])
                print("Server data: ", server_data)
                server_data2 = self.lessonsdb.get_lessons_by_student_id(server_data)
                print("Server data2: ", server_data2)
                # Use list comprehension to join each tuple with the delimiter
                string_data = '-'.join([','.join(map(str, item)) for item in server_data2])
                print(string_data)
                self.send_msg(string_data, client_socket)

            elif arr and len(arr) == 2 and arr[0] == "teacher_id_to_name":
                server_data = self.teacherdb.get_teacher_name_by_id(arr[1])
                print("Server data: ", server_data)
                self.send_msg(server_data, client_socket)

            elif arr and len(arr) == 2 and arr[0] == "delete_lesson":
                server_data = self.lessonsdb.delete_lesson_by_id(arr[1])
                print(server_data)
                if server_data:
                    self.send_msg("succeed to delete lesson", client_socket)
                elif server_data:
                    self.send_msg("failed to delete lesson", client_socket)

            elif arr and len(arr) == 4 and arr[0] == "change_lesson_details":
                server_data = self.lessonsdb.change_lesson_details(arr[1], arr[2], arr[3])
                print(server_data)
                if server_data:
                    self.send_msg("succeed to change lesson details", client_socket)
                elif server_data:
                    self.send_msg("failed to change lesson details", client_socket)

            elif arr and len(arr) == 5 and arr[0] == "check_lesson":
                # teacher_id = self.teacherdb.get_teacher_id_by_id(arr[1])
                # print(teacher_id)
                student_id = self.studentdb.get_student_id_by_id(arr[1])
                print(student_id)
                teacher_id = self.studentdb.get_teacher_id_by_student_id(student_id)
                print(teacher_id)
                is_exist = self.lessonsdb.is_lesson_exist(teacher_id, student_id, arr[2], arr[3])
                if is_exist == True:
                    self.send_msg("lesson is exist", client_socket)
                elif is_exist == False:
                    self.send_msg("lesson is not exist", client_socket)


            elif arr and len(arr) == 5 and arr[0] == "insert_lesson":
                student_id = self.studentdb.get_student_id_by_id(arr[1])
                print(student_id)
                teacher_id = self.studentdb.get_teacher_id_by_student_id(student_id)
                print(teacher_id)
                server_data = self.lessonsdb.insert_lesson(teacher_id, student_id, arr[2], arr[3], arr[4])
                print(server_data)
                if server_data:
                    self.send_msg("succeed to insert lesson", client_socket)
                elif server_data:
                    self.send_msg("failed to insert lesson", client_socket)

            elif arr and arr[0] == "update_t_work_days":
                teacher_id = self.teacherdb.get_teacher_id_by_id(arr[1])
                print(teacher_id)
                days = ",".join(arr[2:])
                print(days)
                server_data = self.teacherdb.update_days(teacher_id, days)
                print(server_data)
                if server_data:
                    self.send_msg("succeed to update teacher's days", client_socket)
                elif server_data:
                    self.send_msg("failed to update teacher's days", client_socket)

            elif arr and len(arr) == 2 and arr[0] == "get_t_work_days":
                student_id = self.studentdb.get_student_id_by_id(arr[1])
                print(student_id)
                teacher_id = self.studentdb.get_teacher_id_by_student_id(student_id)
                print(teacher_id)
                server_data = self.teacherdb.get_teacher_days_by_Id(teacher_id)
                print("server date" + server_data)
                self.send_msg(server_data, client_socket)

            elif arr and arr[0] == "update_t_work_hours":
                teacher_id = self.teacherdb.get_teacher_id_by_id(arr[1])
                print(teacher_id)
                hours = ",".join(arr[2:])
                print(hours)
                server_data = self.teacherdb.update_hours(teacher_id, hours)
                print(server_data)
                if server_data:
                    self.send_msg("succeed to update teacher's hours", client_socket)
                elif server_data:
                    self.send_msg("failed to update teacher's hours", client_socket)

            elif arr and len(arr) == 2 and arr[0] == "get_t_work_hours":
                student_id = self.studentdb.get_student_id_by_id(arr[1])
                print(student_id)
                teacher_id = self.studentdb.get_teacher_id_by_student_id(student_id)
                print(teacher_id)
                server_data = self.teacherdb.get_teacher_hours_by_Id(teacher_id)
                print(server_data)
                self.send_msg(server_data, client_socket)

            elif arr and len(arr) == 2 and arr[0] == "get_t_work_hours2":
                teacher_id = self.teacherdb.get_teacher_id_by_id(arr[1])
                print(teacher_id)
                server_data = self.teacherdb.get_teacher_hours_by_Id(teacher_id)
                print(server_data)
                self.send_msg(server_data, client_socket)

            elif arr and len(arr) == 4 and arr[0] == "send_msg_for_teacher":
                student_id = self.studentdb.get_student_id_by_id(arr[1])
                print(student_id)
                teacher_id = self.studentdb.get_teacher_id_by_student_id(student_id)
                print(teacher_id)
                server_data = self.messagesdb_t.insert(student_id, teacher_id, arr[2], arr[3])
                print(server_data)
                self.send_msg("message successfully sent", client_socket)

            elif arr and len(arr) == 5 and arr[0] == "send_msg_for_student":
                student_id = self.studentdb.get_student_id_by_name(arr[2])
                print(student_id)
                teacher_id = self.teacherdb.get_teacher_id_by_id(arr[1])
                print(teacher_id)
                server_data = self.messagesdb_s.insert(teacher_id, student_id, arr[3], arr[4])
                print(server_data)
                self.send_msg("message successfully sent", client_socket)

            elif arr and len(arr) == 2 and arr[0] == "get_t_price":
                student_id = self.studentdb.get_student_id_by_id(arr[1])
                print(student_id)
                teacher_id = self.studentdb.get_teacher_id_by_student_id(student_id)
                print(teacher_id)
                price = self.teacherdb.get_teacher_price_by_id(teacher_id)
                print(price)
                str_price = str(price)
                self.send_msg(str_price, client_socket)

            # elif arr and len(arr) == 2 and arr[0] == "check_id":
            #     server_data = self.teacherdb.is_id_exist(arr[1])
            #     print(server_data)
            #     if server_data == True:
            #         self.send_msg("true", client_socket)
            #     if server_data == False:
            #         self.send_msg("false", client_socket)
            #     if server_data == None:
            #         self.send_msg("false", client_socket)




            # elif arr and len(arr) == 2 and arr[0] == "lessons_list_for_delete":
            #     server_data = self.teacherdb.get_teacher_id_by_id(arr[1])
            #     print("Server data: ", server_data)
            #     server_data2 = self.lessonsdb.get_lessons_by_teacher_id(server_data)
            #     print("Server data2: ", server_data2)
            #     # Use list comprehension to join each tuple with the delimiter
            #     string_data = '-'.join([','.join(map(str, item)) for item in server_data2])
            #     print(string_data)
            #     client_socket.send(string_data.encode())

            elif arr and len(arr) == 2 and arr[0] == "s_messages":
                student_id = self.studentdb.get_student_id_by_id(arr[1])
                print(student_id)
                server_data = self.messagesdb_s.get_all_messages_for_student(student_id)
                print(server_data)
                # Use list comprehension to join each tuple with the delimiter
                string_data = '-'.join([','.join(map(str, item)) for item in server_data])
                print(string_data)
                self.send_msg(string_data, client_socket)


            elif arr and len(arr) == 2 and arr[0] == "t_messages":
                print(1)
                teacher_id = self.teacherdb.get_teacher_id_by_id(arr[1])
                print(teacher_id)
                server_data = self.messagesdb_t.get_all_messages_for_teacher(teacher_id)
                print(server_data)
                # Use list comprehension to join each tuple with the delimiter
                string_data = '-'.join([','.join(map(str, item)) for item in server_data])
                print(string_data)
                self.send_msg(string_data, client_socket)

            else:
                print(arr)
                self.send_msg("error message", client_socket)

    def send_msg(self, data, client_socket):
        try:
            print("message: " + str(data))
            length = str(len(data)).zfill(SIZE) #the size of the msg
            length = length.encode('utf-8')
            print(length)
            if type(data) != bytes:
                data = data.encode()# if not byte send as str
            print(data)
            msg = length + data
            print("message with length: " + str(msg))
            client_socket.send(msg)
        except:
            print("error with sending message")



    def recv_msg(self, client_socket, ret_type="string"):
        try:
            length = client_socket.recv(SIZE).decode('utf-8')# recv size of msg
            if not length:
                print("no length")
                return None
            print("the length: " + length)
            data = client_socket.recv(int(length)) # the text of tne msg
            if not data:
                print("no data")
                return None
            print("the data: " + str(data))
            if ret_type == "string":
                data = data.decode('utf-8') #recv
            print(data)
            return data
        except:
            print("error with receiving message")




if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1802
    s = Server(ip, port)
    s.start()
