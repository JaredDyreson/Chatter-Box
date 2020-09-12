#!/usr/bin/env python3.8

import socket

s = socket.socket()

PORT = 12345

s.connect(('127.0.0.1', PORT))

print(s.recv(1024))
s.close()
