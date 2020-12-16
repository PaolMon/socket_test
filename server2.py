import socket
import numpy as np
import cv2
import sys
from AES import AESCipher

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5006

random_key = b'G\xc3\xfd\x95A\x92\xa2%v\xbeVG\x89A2\x88'

cipher = AESCipher(random_key)

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
                frame = cipher.decrypt(frame)
                print('size of the received frame : %s' % sys.getsizeof(frame))
                print('received frame : %s' % frame)