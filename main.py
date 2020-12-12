#!/usr/bin/env python3.8

import socket
import tkinter

import MathGames


try:
    MathGameInstance = MathGames.Game(url="localhost", port=8080)
except ConnectionRefusedError as error:
    MathGames.DesktopApplication.ConnectionFailed().run()
    quit()

LoginPortal = MathGames.DesktopApplication.Login()
LoginPortal.run()

try:
    client = MathGames.Client(LoginPortal.name)
    print(f'Client created with name of {client.name}')
except ValueError:
    quit()

MathGameWindow = MathGames.DesktopApplication.NumpadWindow(MathGameInstance, client)

try:
    MathGameWindow.run()
except KeyboardInterrupt:
    quit()
