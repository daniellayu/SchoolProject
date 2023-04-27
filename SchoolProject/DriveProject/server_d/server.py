import socket
import threading
from teacherdb import TeacherDb
from studentdb import StudentDb
from lessonsdb import LessonsDb



class Server(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.count = 0
        self.running = True
        self.teacherdb = TeacherDb()
        self.studentdb = StudentDb()
        self.lessonsdb = LessonsDb()

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
            server_data = client_socket.recv(1024).decode('utf-8')
            if not server_data:  # client disconnected
                break
            arr = server_data.split(",")
            print(arr)
            if arr and len(arr) == 9 and arr[0] == "sign_up_teacher":
                server_data = self.teacherdb.insert(arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8])
                print("Server data: ", server_data)
                if server_data:
                    client_socket.send("success Sign up teacher".encode())
                elif server_data:
                    client_socket.send("failed Sign up teacher".encode())

            elif arr and len(arr) == 7 and arr[0] == "sign_up_student":
                server_data = self.studentdb.insert(arr[1], arr[2], arr[3], arr[4], arr[5], arr[6])
                print("Server data: ", server_data)
                if server_data:
                    client_socket.send("success Sign up student".encode())
                elif server_data:
                    client_socket.send("failed Sign up student".encode())

            elif arr and len(arr) == 3 and arr[0] == "sign_in_teacher":
                server_data = self.teacherdb.is_exist(arr[1], arr[2])
                print("Server data: ", server_data)  # true or false
                if server_data:
                    client_socket.send("success Sign in".encode())
                elif server_data:
                    client_socket.send("failed Sign in".encode())

            elif arr and len(arr) == 3 and arr[0] == "sign_in_student":
                server_data = self.studentdb.is_exist(arr[1], arr[2])
                print("Server data: ", server_data)
                if server_data:
                    client_socket.send("success Sign in".encode())
                elif server_data:
                    client_socket.send("failed Sign in".encode())

            elif arr and len(arr) == 2 and arr[0] == "students_list":
                server_data = self.teacherdb.get_teacher_id_by_id(arr[1])
                print("Server data: ", server_data)
                server_data2 = self.studentdb.get_students_by_teacher_id(server_data)
                print("Server data2: ", server_data2)
                # Use list comprehension to join each tuple with the delimiter
                string_data2 = '-'.join([','.join(map(str, item)) for item in server_data2])
                print(string_data2)
                client_socket.send(string_data2.encode())

            elif arr and len(arr) == 2 and arr[0] == "lessons_list":
                server_data = self.teacherdb.get_teacher_id_by_id(arr[1])
                print("Server data: ", server_data)
                server_data2 = self.lessonsdb.get_lessons_by_teacher_id(server_data)
                print("Server data2: ", server_data2)
                # Use list comprehension to join each tuple with the delimiter
                string_data = '-'.join([','.join(map(str, item)) for item in server_data2])
                print(string_data)
                client_socket.send(string_data.encode())

            elif arr and len(arr) == 2 and arr[0] == "student_id_to_name":
                server_data = self.studentdb.get_student_name_by_id(arr[1])
                print("Server data: ", server_data)
                client_socket.send(server_data.encode())

            elif arr and len(arr) == 4 and arr[0] == "update_details":
                # server_data = self.teacherdb.get_teacher_id_by_name(arr[1])
                # print("Server data: ", server_data)
                server_data = self.teacherdb.update_by_id(arr[1], arr[2], arr[3]) #return false
                print("Server data: ", server_data)
                if server_data:
                    client_socket.send("success update details".encode())
                elif server_data:
                    client_socket.send("failed update details".encode())

            elif arr and len(arr) == 1 and arr[0] == "teachers_list":
                server_data = self.teacherdb.get_all_teachers()
                print("Server data: ", server_data)
                # Use list comprehension to join each tuple with the delimiter
                string_data = '-'.join([','.join(map(str, item)) for item in server_data])
                print(string_data)
                client_socket.send(string_data.encode())

            elif arr and len(arr) == 3 and arr[0] == "update_teacher_id":
                server_data = self.studentdb.update_teacher_id(arr[1], arr[2])
                print("Server data: ", server_data)
                if server_data:
                    client_socket.send("success update teacher id".encode())
                elif server_data:
                    client_socket.send("failed update teacher id".encode())

            elif arr and len(arr) == 2 and arr[0] == "student_lessons_list":
                server_data = self.studentdb.get_student_id_by_id(arr[1])
                print("Server data: ", server_data)
                server_data2 = self.lessonsdb.get_lessons_by_student_id(server_data)
                print("Server data2: ", server_data2)
                # Use list comprehension to join each tuple with the delimiter
                string_data = '-'.join([','.join(map(str, item)) for item in server_data2])
                print(string_data)
                client_socket.send(string_data.encode())

            elif arr and len(arr) == 2 and arr[0] == "teacher_id_to_name":
                server_data = self.teacherdb.get_teacher_name_by_id(arr[1])
                print("Server data: ", server_data)
                client_socket.send(server_data.encode())

            elif arr and len(arr) == 2 and arr[0] == "delete_lesson":
                server_data = self.lessonsdb.delete_lesson_by_id(arr[1])
                print(server_data)
                if server_data:
                    client_socket.send("succeed to delete lesson".encode())
                elif server_data:
                    client_socket.send("failed to delete lesson".encode())

            elif arr and len(arr) == 4 and arr[0] == "change_lesson_details":
                server_data = self.lessonsdb.change_lesson_details(arr[1], arr[2], arr[3])
                print(server_data)
                if server_data:
                    client_socket.send("succeed to change lesson details".encode())
                elif server_data:
                    client_socket.send("failed to change lesson details".encode())

            elif arr and len(arr) == 5 and arr[0] == "insert_lesson":
                # teacher_id = self.teacherdb.get_teacher_id_by_id(arr[1])
                # print(teacher_id)
                student_id = self.studentdb.get_student_id_by_id(arr[1])
                print(student_id)
                teacher_id = self.studentdb.get_teacher_id_by_student_id(student_id)
                print(teacher_id)
                server_data = self.lessonsdb.insert_lesson(teacher_id, student_id, arr[2], arr[3], arr[4])
                print(server_data)
                if server_data:
                    client_socket.send("succeed to insert lesson".encode())
                elif server_data:
                    client_socket.send("failed to insert lesson".encode())

            elif arr and len(arr) == 2 and arr[0] == "lessons_list_for_delete":
                server_data = self.teacherdb.get_teacher_id_by_id(arr[1])
                print("Server data: ", server_data)
                server_data2 = self.lessonsdb.get_lessons_by_teacher_id(server_data)
                print("Server data2: ", server_data2)
                # Use list comprehension to join each tuple with the delimiter
                string_data = '-'.join([','.join(map(str, item)) for item in server_data2])
                print(string_data)
                client_socket.send(string_data.encode())


            else:
                print(arr)
                self.send_message("error message", client_socket)

    def send_message(self, data, socket):
        print("send_message" + data)
        length = str(len(data)).zfill(4)
        msg = length + data
        print("send_message" + msg)
        socket.send(msg.encode())

    def recv_message(self, socket):
        length = socket.recv(4).decode('utf-8')
        if not length:
            return None
        print(int(length))
        data = socket.recv(int(length)).decode('utf-8')
        if not data:
            return None
        print(data)
        return data


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1802
    s = Server(ip, port)
    s.start()
