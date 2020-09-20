#!/usr/bin/env python3.8

from Chatter.Client import Client
from Chatter.Client import SERVER_IP
import socket
import base64

class Server():
    def __init__(self, port: int, wait_time=5):
        self.port = port
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.hostname)
        self.sock.bind(('', self.port))
        self.sock.settimeout(wait_time)
        self.sock.listen(wait_time)
        self.message = "Example text"
    def broadcast_message(self):
        while(True):
            try:
                connection, address = self.sock.accept()
                connection.send(self.message.encode())
                connection.close()
            except socket.timeout as e:
                print(e,': no connections after 5 seconds...')
                connection.close()
            except (EOFError, KeyboardInterrupt):
                quit()
            except Exception:
                print("some weird error happened")
    def change_broadcast_message(self, content: str):
        self.message = content
    def get_uniqueId(self) -> str:
        return base64.b32encode(str.encode(self.ip_address + '/' + str(self.port) + '/' + self.hostname))


# S = Server(12345)
# S.broadcast_message()
# C = Client("Jared", 12345)
# print(C.get_message())
