import socket
import threading
import time

def listen_server(delay):
        while True:
                print(comms_socket.recv(4096).decode("UTF-8")) 
                time.sleep(delay)


comms_socket = socket.socket()
host = '192.168.86.42'
port = 5000
comms_socket.connect((host, port))
receive_thread = threading.Thread(target = listen_server, args=(1,))
receive_thread.start()

while True:
        
	send_data = input("Message: ")
	comms_socket.send(bytes(send_data, "UTF-8"))

