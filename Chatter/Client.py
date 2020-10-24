#!/usr/bin/env python3.8

import sys, os
import asyncio
import websockets
import logging
import warnings

logger = logging.getLogger('websockets')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
os.environ['PYTHONASYNCIODEBUG'] = '1'
logging.basicConfig(level=logging.DEBUG)
warnings.resetwarnings()

async def handler():
    uri = "ws://localhost:5000"
    async with websockets.connect(uri) as websocket:
        await producer_handler(websocket)
        # consumer_task = asyncio.ensure_future(consumer_handler(websocket))
        # producer_task = asyncio.ensure_future(producer_handler(websocket))
        # done, pending = await asyncio.wait([consumer_task, producer_task],return_when=asyncio.FIRST_COMPLETED,)
        # for task in pending:
        #     task.cancel()




async def producer_handler(websocket):
    while True:
        # message = await producer()
        message = input()
        await websocket.send(message)

async def consumer_handler(websocket):
    async for message in websocket:
        await consumer(message)


async def producer():
    return input()

async def consumer(message: str):
    print(message)
    
    
start_client = handler()

asyncio.get_event_loop().run_until_complete(start_client)
asyncio.get_event_loop().run_forever()

