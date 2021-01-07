import socket
import numpy as np
import sys
from AES import AESCipher
import queue
from threading import Thread

_client_connected_ = False

defm

def main(key):

    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = 5005

    cipher = AESCipher(key)

    #server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((SERVER_HOST, SERVER_PORT))
        s.listen()
        print("SERVER listening")
        if True:  #to replace while True: in test
            conn, addr = s.accept()
            conn.settimeout(5)
            with conn:


if __name__ == "__main__":

    shared_key = b'G\xc3\xfd\x95A\x92\xa2%v\xbeVG\x89A2\x88'

    main(shared_key)