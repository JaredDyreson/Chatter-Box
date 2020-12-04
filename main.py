import socket
import threading
import time
import json
import select

import tkinter

# import Chatter.DesktopApplication
import Chatter

# GLOBAL VARIABLES

try:
    G = Chatter.Game()
except ConnectionRefusedError as error:
    Chatter.DesktopApplication.ConnectionFailed().run()
    quit()

L = Chatter.DesktopApplication.Login()
L.run()

client = Chatter.Client(L.name)
print(f'Client created with name of {client.name}')

N = Chatter.DesktopApplication.NumpadWindow(G, client)

try:
    N.run()
except Exception as error:
    print(error)
