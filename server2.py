import socket
import sys

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5006

#server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen()
    print("SERVER listening")
    while True:
        conn, addr = s.accept()
        received = b""
        conn.settimeout(5)
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(81)
                print(data)
                if not data:
                    break
                if data == b"EOF":
                    print(data)
                    break
                received += data

            print('this is what i received : %g' % int(received))
            print('this is the length of what i received : %s' % sys.getsizeof(received))


