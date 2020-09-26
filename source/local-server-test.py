import socket
import sys
import threading
import time

def listen_clients(delay):
        while True:
            print(address[0] + ": " +connection.recv(4096).decode("UTF-8"))
            time.sleep(delay)

comms_socket = socket.socket()
host = ''
port = 5000
comms_socket.bind((host, port))
comms_socket.listen(10)
connection, address = comms_socket.accept()

receive_thread = threading.Thread(target = listen_clients, args=(1,))
receive_thread.start()

while True:
        time.sleep(1)
