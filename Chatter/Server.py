#!/usr/bin/env python3.8

from Chatter.Client import Client
from Chatter.Client import SERVER_IP
import socket

class Server():
    def __init__(self, port: int, wait_time=5):
        self.port = port
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('', self.port))
        self.sock.listen(wait_time)
        self.message = "Example text"
    def broadcast_message(self):
        while(True):
            try:
                connection, address = self.sock.accept()
                connection.send(self.message.encode())
                connection.close()
            except (EOFError, KeyboardInterrupt):
                quit()
            except Exception:
                print("some weird error happened")
    def change_broadcast_message(content: str):
        self.message = content

# S = Server(12345)
# S.broadcast_message()
# C = Client("Jared", 12345)
# print(C.get_message())
