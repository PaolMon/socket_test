import socket
import sys

PORT=5006
HOST="127.0.0.1"
MESSAGE = b"Giovanni"

size = 480*640*3
msg = b'%g'.zfill(10) % size

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.connect((HOST, PORT))
    msg_size = sys.getsizeof(msg)
    print('sending %g bytes, wrapped in TCP expected %g' % (msg_size, msg_size+33))
    s.send(msg)