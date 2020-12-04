import socket
import tkinter

import Chatter


try:
    MathGameInstance = Chatter.Game()
except ConnectionRefusedError as error:
    Chatter.DesktopApplication.ConnectionFailed().run()
    quit()

LoginPortal = Chatter.DesktopApplication.Login()
LoginPortal.run()

try:
    client = Chatter.Client(LoginPortal.name)
    print(f'Client created with name of {client.name}')
except ValueError:
    quit()

MathGameWindow = Chatter.DesktopApplication.NumpadWindow(MathGameInstance, client)

try:
    MathGameWindow.run()
except KeyboardInterrupt:
    quit()
except Exception as error:
    print (error)
