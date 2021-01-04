import socket
import sys
from AES import AESCipher
import numpy as np
from matplotlib import pyplot as plt
import ffmpeg


PORT=5005
HOST="127.0.0.1"

print("CLIENT")


width = 2560
height = 1440

dim = width * height * 3

process1 = (
    ffmpeg
    .input('rtsp://192.168.1.17/11')
    .output('-', format='rawvideo')
    .run_async(pipe_stdout=True)
)

#random_key = os.urandom(16)
random_key = b'G\xc3\xfd\x95A\x92\xa2%v\xbeVG\x89A2\x88'

cipher = AESCipher(random_key)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.connect((HOST, PORT))
    k = process1.stdout.read(dim)
    print('size of the buffer to encrypt: %s' % sys.getsizeof(k))
    k = cipher.encrypt(k)
    print('size of the buffer to send: %s' % sys.getsizeof(k))
    s.send("{}".format(sys.getsizeof(k)).zfill(10).encode())

    while process1.poll() is None:
        k = process1.stdout.read(dim)
        k = cipher.encrypt(k)
        s.sendall(k)

process1.wait()