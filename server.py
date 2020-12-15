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
    if True:  #to replace while True: in test
        conn, addr = s.accept()
        conn.settimeout(5)
        with conn:
            print('Connected by', addr)
            frame_size = conn.recv(80)
            frame_size = int(frame_size)
            while True:
                frame = b''
                remaining_bytes = frame_size
                print('WAITING FOR %g BYTES' % remaining_bytes)
                while remaining_bytes > 0:
                    data = conn.recv(remaining_bytes)
                    if not data:
                        break
                    frame += data
                    remaining_bytes = frame_size - sys.getsizeof(frame)
                    print('%g bytes remaining' % remaining_bytes)

                print('size of the received buffer : %s' % sys.getsizeof(frame))

                y = np.frombuffer(frame, dtype=np.uint8, count=-1)
                y=np.reshape(y, (480, 640, 3))
