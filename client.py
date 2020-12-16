import socket
import cv2
import numpy as np
import sys
from AES import AESCipher
import os

PORT=5005
HOST="127.0.0.1"
MESSAGE = b"Giovanni"

print("CLIENT")


vid_cap = cv2.VideoCapture(0) 

hasFrames,image = vid_cap.read()

#random_key = os.urandom(16)
random_key = b'G\xc3\xfd\x95A\x92\xa2%v\xbeVG\x89A2\x88'

cipher = AESCipher(random_key)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.connect((HOST, PORT))
    k = image.tobytes()
    print('size of the buffer to encrypt: %s' % sys.getsizeof(k))
    k = cipher.encrypt(k)
    print('size of the buffer to send: %s' % sys.getsizeof(k))
    s.send("{}".format(sys.getsizeof(k)).zfill(10).encode())

    while hasFrames:
        k = image.tobytes()
        k = cipher.encrypt(k)
        s.sendall(k)
        hasFrames,image = vid_cap.read()