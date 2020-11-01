#!/usr/bin/env python3.8

from websocket import create_connection
import json

ws = create_connection("ws://144.202.127.25:8080")
print("got connection to my server")
ws.send(4)

result =  ws.recv()
print(result)
ws.close()
