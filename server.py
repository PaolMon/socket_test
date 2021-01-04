import socket
import numpy as np
import cv2
import sys
from AES import AESCipher
import queue
from threading import Thread

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5005

width = 2560
height = 1440

random_key = b'G\xc3\xfd\x95A\x92\xa2%v\xbeVG\x89A2\x88'
q = queue.Queue()

def main():
    cipher = AESCipher(random_key)

    thread = Thread(target=update, daemon=True)
    thread.start()
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
                    print('WAITING FOR {} BYTES'.format(remaining_bytes))
                    while remaining_bytes > 0:
                        data = conn.recv(remaining_bytes)
                        if not data:
                            break
                        frame += data
                        remaining_bytes = frame_size - sys.getsizeof(frame)
                        print('{} bytes remaining'.format(remaining_bytes))

                    print('size of the received buffer : {}'.format(sys.getsizeof(frame)))
                    frame = cipher.decrypt(frame)
                    print('size of the received frame : {}'.format(sys.getsizeof(frame)))
                    y = np.frombuffer(frame, dtype=np.uint8, count=-1)
                    y=np.reshape(y, (height, width, 3))
                    q.put(y)



def update():
        while True:
            if not q.empty():
                img0 = q.get()
                cv2.imshow("received", img0)
                if cv2.waitKey(1) == ord('q'):  # q to quit
                    raise StopIteration

main()