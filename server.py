import socket
import numpy as np
import cv2
import sys

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5005

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
                data = conn.recv()
                if not data:
                    break
                if data == b"EOF":
                    print(data)
                    break
                received += data

            print('size of the received buffer : %s' % sys.getsizeof(received))

            y = np.frombuffer(received, dtype=np.uint8, count=-1)
            y=np.reshape(y, (480, 640, 3))

            print('image received: %g' % sys.getsizeof(received))

            cv2.imshow('image',y)
            cv2.waitKey(0)
