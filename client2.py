import socket

PORT=5006
HOST="127.0.0.1"
MESSAGE = b"Giovanni"

size = 480*640*3

print("CLIENT")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.connect((HOST, PORT))
    s.send(b'%g'.zfill(15) % size)