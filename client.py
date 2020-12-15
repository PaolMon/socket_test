import socket
import cv2
import numpy as np
import sys

PORT=5005
HOST="127.0.0.1"
MESSAGE = b"Giovanni"

print("CLIENT")


vid_cap = cv2.VideoCapture(0) 

hasFrames,image = vid_cap.read()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.connect((HOST, PORT))

    while hasFrames:
        k = image.tobytes()
        print('size of the buffer to send: %s' % sys.getsizeof(k))
        s.sendall(k)
        s.send(b"EOF")
        hasFrames,image = vid_cap.read()