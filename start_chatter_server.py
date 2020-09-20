#!/usr/bin/env python3.8

from Chatter.Server import Server

S = Server(12345)
print(S.get_uniqueId())
S.broadcast_message()