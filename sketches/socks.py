#!/usr/bin/env python3.8

import socket

url = "localhost"
port = 5000
state = True
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((url, port))

while(state):
    data = sock.recv(512)
    if(data.lower() == "q"):
        sock.close()
        break
    else:

        print(f'recieved: {data}')
