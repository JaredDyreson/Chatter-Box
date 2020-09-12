#!/usr/bin/env python3.8

import socket

s = socket.socket()
PORT = 12345

s.bind(('', PORT))

s.listen(5)

while(True):
    connection, address = s.accept()
    connection.send('Thank you for connecting'.encode())
    connection.close()

