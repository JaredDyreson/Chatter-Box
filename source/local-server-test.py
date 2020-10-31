# server.py
import socket
import sys
import threading
import time
#from thread import start_new_thread

HOST = '' # all availabe interfaces
PORT = 8080 # arbitrary non privileged port 

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Could not create socket.")
    sys.exit(0)

print("[-] Socket Created")

# bind socket
try:
    s.bind((HOST, PORT))
    print("[-] Socket Bound to port " + str(PORT))
except:
    print("Bind Failed.")
    sys.exit()

s.listen(10)
print("Listening...")

# The code below is what you're looking for ############

def client_thread(conn):

    while True:

        
        #data = conn.recv(1024)
        #if not data:
        #    break
        #reply = "OK . . " + data
        #print(data)
        
        try: 
                send_message = "{\"game_state\":true,\"question\":\"2+2=?\",\"time_out\":15,\"winner\":\"\"}"
                send_message = send_message.encode()
                conn.send(send_message)
                time.sleep(15)
                
                send_message = "{\"game_state\":false,\"question\":\"2+2=?\",\"time_out\":0,\"winner\":\"JOHN\"}"
                send_message = send_message.encode()
                conn.sendall(send_message)
                time.sleep(1)
        except:
                print("Couldnt send message. Closing connection")
                break
    conn.close()

while True:
    # blocking call, waits to accept a connection
    conn, addr = s.accept()
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))
    try: 
        new_thread = threading.Thread(target = client_thread, args=(conn,))
        new_thread.start()
    except:
        print("Couldnt open thread")
    #start_new_thread(client_thread, (conn,))

s.close()
