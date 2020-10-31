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

logger = logging.getLogger('websockets')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
os.environ['PYTHONASYNCIODEBUG'] = '1'
logging.basicConfig(level=logging.DEBUG)
warnings.resetwarnings()

connected = set()


def equation() -> str:
    operators = ['+', '-']
    random.seed(datetime.now())
    operator = random.choice(operators)
    a = random.randint(0, 10)
    b = random.randint(0, a)
    return f'{a} {operator} {b}'

e = equation()

def check(answer: int, expression: str) -> bool:
    return (answer == eval(expression))

async def handler(websocket, path):
    # Register.
    connected.add(websocket)
    global e
    try:
        # Implement logic here.
        await websocket.send("Hello! You are connected to websocket!")
        await websocket.send(f"Equation: {e}")
        async for message in websocket:
            if(int(message) == eval(e)):
                e = equation()
                for ws in connected:
                    if(ws == websocket):
                        await ws.send("You got the right Answer!")
                    else:
                        await ws.send("Someone got the right Answer!")
                        
                    await ws.send(f"New equation: {e}")
            else:
                await websocket.send("Incorrect Answer. Try again!")

    finally:
        connected.remove(websocket)

start_server = websockets.serve(handler, "", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
