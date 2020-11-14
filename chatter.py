#!/usr/bin/env python3.8

from Chatter.Client import Client
from Chatter.Equations import Generator
from Chatter.Game import Game

C1 = Client("JARED")
C2 = Client("JOHN")

try:
    G = Game()
    G.start([C1])
except ConnectionRefusedError:
    print("[-] Server is not active, please turn it on")
