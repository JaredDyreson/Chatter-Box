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

def check(answer: int, expression: str) -> bool:
    return (answer == eval(expression))

async def handler(websocket, path, e):
    # Register.
    connected.add(websocket)
    try:
        # Implement logic here.
        await asyncio.wait([ws.send("Hello! You are connected to websocket!") for ws in connected])
        await asyncio.wait([ws.send(f"Equation: {e}") for ws in connected])
        consumer_task = asyncio.ensure_future(consumer_handler(websocket, path, e))
        producer_task = asyncio.ensure_future(producer_handler(websocket, path, e))
        done, pending = await asyncio.wait([consumer_task, producer_task], return_when=asyncio.ALL_COMPLETED,)
        # for task in pending:
        #     task.cancel()
    finally:
        # Unregister.
        connected.remove(websocket)


async def producer_handler(websocket, path, e):
    message = await producer(e)
    await websocket.send(message)

async def consumer_handler(websocket, path, e):
    async for message in websocket:
        await consumer(message, e)


async def producer(e):
    return f"Answer is {eval(e)}"

async def consumer(message: str, e):
    print(message)
    await asyncio.wait([ws.send(f"{int(message) == eval(e)}") for ws in connected])


def equation() -> str:
    operators = ['+', '-']
    random.seed(datetime.now())
    operator = random.choice(operators)
    a = random.randint(0, 10)
    b = random.randint(0, a)
    return f'{a} {operator} {b}'


bound_handler = functools.partial(handler, e = equation())
start_server = websockets.serve(bound_handler, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
