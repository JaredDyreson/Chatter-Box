#!/usr/bin/env python3.8

from Chatter.Client import Client
from Chatter.Server import Server
from Chatter.Equations import Generator

C1 = Client("JARED")
C2 = Client("JOHN")

S = Server()
S.start(C1, C2)

<<<<<<< HEAD
# G = Generator()
# for x in range(0, 100):
    # print(G.equation())
=======
 
>>>>>>> 3f08103412acf91e278c5a8fb77c4f3c6f75416f
