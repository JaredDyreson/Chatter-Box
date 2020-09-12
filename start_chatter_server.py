#!/usr/bin/env python3.8

from Chatter.Server import Server

S = Server(12345)
S.broadcast_message()
