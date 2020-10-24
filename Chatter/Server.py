#!/usr/bin/env python3.8

import sys, os
import asyncio
import websockets
import base64
import logging
import warnings

logger = logging.getLogger('websockets')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
os.environ['PYTHONASYNCIODEBUG'] = '1'
logging.basicConfig(level=logging.DEBUG)
warnings.resetwarnings()

connected = set()

async def handler(websocket, path):
    # Register.
    connected.add(websocket)
    try:
        # Implement logic here.
        await asyncio.wait([ws.send("Hello! You are connected to websocket!") for ws in connected])
        consumer_task = asyncio.ensure_future(consumer_handler(websocket, path))
        producer_task = asyncio.ensure_future(producer_handler(websocket, path))
        done, pending = await asyncio.wait([consumer_task, producer_task], return_when=asyncio.FIRST_COMPLETED,)
        for task in pending:
            task.cancel()
    finally:
        # Unregister.
        connected.remove(websocket)


async def producer_handler(websocket, path):
    while True:
        message = await producer()
        await websocket.send(message)

async def consumer_handler(websocket, path):
    async for message in websocket:
        await consumer(message)


async def producer():
    return "server produced message!"

async def consumer(message: str):
    print(message)


start_server = websockets.serve(handler, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
