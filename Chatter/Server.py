#!/usr/bin/env python3.8

import sys, os
import asyncio
import websockets
import base64
import logging
import warnings
import random
import functools
from datetime import datetime
import time
import json

class ClientPayload(object):
    def __init__(self, name, answer):
        self.name = name
        self.answer = answer
        
class ServerPayload(object):
    def __init__(self, game_state, question, time_out, winner):
        self.game_state = game_state
        self.question = question
        self.time_out = time_out
        self.winner = winner
        self.timestamp = None

logger = logging.getLogger('websockets')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
os.environ['PYTHONASYNCIODEBUG'] = '1'
logging.basicConfig(level=logging.DEBUG)
warnings.resetwarnings()

connected = set()


def equation() -> str:
    operators = ['+', '-']
    operator = random.choice(operators)
    a = random.randint(0, 10)
    b = random.randint(0, a)
    return f'{a} {operator} {b}'

def check(answer: int, expression: str) -> bool:
    return (answer == eval(expression))

e = equation()

async def handler(websocket, path):
    # Register.
    connected.add(websocket)
    global e
    try:
        # Implement logic here.
        serverPayload = ServerPayload(game_state = False, question = e, time_out = None, winner = None)
        await websocket.send(json.dumps(serverPayload.__dict__))
        async for message in websocket:
            clientPayload = ClientPayload(**json.loads(message))
            if(clientPayload.answer == eval(e)):
                e = equation()
                serverPayload = ServerPayload(game_state = True, question = e, time_out = None, winner = clientPayload.name)
                for ws in connected:
                    await ws.send(json.dumps(serverPayload.__dict__))
            else:
                await websocket.send(json.dumps(serverPayload.__dict__))

    finally:
        connected.remove(websocket)

start_server = websockets.serve(handler, "", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


