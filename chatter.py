#!/usr/bin/env python3.8

from Chatter.Client import Client
from Chatter.Server import Server
from Chatter.Equations import Generator

C1 = Client("JARED")
C2 = Client("JOHN")

S = Server()
S.start(C1, C2)

 
