import socket
import threading
import time
from tkinter import *


user_name = ""
entryMessage = ""
chat_box = ""
runApp = False

def listen_server(delay):
        global runApp
        while runApp == False:
                time.sleep(1)
                        
        
        while True:
                message = comms_socket.recv(4096).decode("UTF-8")
                print(message) 
                #chat_box.config(state = NORMAL)
                #chat_box.insert(END, message + "\n\n")
                
                time.sleep(1)
                
def login_func(name, gotUserName):
        global user_name
        user_name = name
        print (user_name)

def send_func(message):
        global entryMessage
        outbound_message = "{\"name\":\"" + user_name + "\",\"answer\": " + message + "}"
        print (outbound_message)
        comms_socket.send(bytes(outbound_message, "UTF-8"))
        entryMessage.delete(0, END)
        

        

#g = GUI()
comms_socket = socket.socket()
host = '192.168.86.11'
port = 8081
comms_socket.connect((host, port))
receive_thread = threading.Thread(target = listen_server, args=(1,))
receive_thread.start()

main_window = Tk()
main_window.title("Math Game")
main_window.withdraw()

#login
login_window = Toplevel()
login_window.title("What is your name?")
login_window.resizable(width = False, height = False)
login_window.configure(width = 400, height = 300)
labelName = Label(login_window, text = "Name: ", font = "Helvetica 12") 
labelName.place(relheight = 0.2, relx = 0.1, rely = 0.2)
entryName = Entry(login_window,  font = "Helvetica 14") 
entryName.place(relwidth = 0.4,  relheight = 0.12, relx = 0.35, rely = 0.2)  
entryName.focus()

got_user_name = BooleanVar()
login_button = Button(login_window, text = "CONTINUE",  font = "Helvetica 14 bold", command = lambda: login_func(entryName.get(), got_user_name.set(True))) 
login_button.place(relx = 0.4, rely = 0.55)
login_button.wait_variable(got_user_name)
login_window.withdraw()


#chat window
main_window.deiconify()
main_window.resizable(width = False, height = False)
main_window.configure(width = 470, height = 550)

chat_box = Text(main_window, width = 20,  height = 2, bg = "#17202A", fg = "#EAECEE", font = "Helvetica 14",  padx = 5, pady = 5)
chat_box.place(relheight = 0.745, relwidth = 1,  rely = 0.08)

labelBottom = Label(main_window, bg = "#ABB2B9", height = 80) 
labelBottom.place(relwidth = 1, rely = 0.825)

entryMessage = Entry(labelBottom,bg = "#2C3E50", fg = "#EAECEE", font = "Helvetica 13")
entryMessage.place(relwidth = 0.74, relheight = 0.06, rely = 0.008, relx = 0.011)
entryMessage.focus()

sendButton = Button(labelBottom, text = "Send", font = "Helvetica 10 bold",  width = 20, bg = "#ABB2B9", command = lambda : send_func(entryMessage.get())) 
sendButton.place(relx = 0.77, rely = 0.008, relheight = 0.06,  relwidth = 0.22) 

runApp = True

	#send_data = input("Message: ")
	#comms_socket.send(bytes(send_data, "UTF-8"))

