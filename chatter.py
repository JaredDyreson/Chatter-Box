#!/usr/bin/env python3.8

from Chatter.Client import Client
from Chatter.Equations import Generator
from Chatter.Game import Game

C1 = Client("JARED")
C2 = Client("JOHN")

G = Game()
G.start(C1, C2)
