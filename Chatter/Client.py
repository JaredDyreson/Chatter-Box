#!/usr/bin/env python3.8

import socket

"""
Author: Jared Dyreson
Function: Client class that can communicate with another
"""

SERVER_IP = '127.0.0.1'

class Client():
    def __init__(self, name: str, port: int):
        self.name = name
        self.port = port
        self.sock = socket.socket()
        self.connection = self.sock.connect((SERVER_IP, self.port))
    def get_message(self) -> str:
        return self.sock.recv(1024).decode()

