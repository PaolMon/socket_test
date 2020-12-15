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
        conn.settimeout(5)
        with conn:
            frame = b''
            print('Connected by', addr)
            frame_size = conn.recv(80)
            frame_size = int(frame_size)
            remaining_bytes = frame_size - sys.getsizeof(frame)
            while remaining_bytes:
                data = conn.recv(remaining_bytes)
                if not data:
                    break
                frame += data
                remaining_bytes = frame_size - sys.getsizeof(frame)

            print('size of the received buffer : %s' % sys.getsizeof(frame))

            y = np.frombuffer(frame, dtype=np.uint8, count=-1)
            y=np.reshape(y, (480, 640, 3))

            cv2.imshow('image',y)
            cv2.waitKey(0)
