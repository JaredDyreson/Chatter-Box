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
import json
import threading
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import time
import argparse

class ClientPayload(object):
    def __init__(self, name, answer):
        self.name = name
        try:
            self.answer = int(answer)
        except ValueError:
            raise ValueError(f'{self.answer} is not convertible to integer, stop.')

class ServerPayload(object):
    def __init__(self, game_state, question, time_out, winner, score_board: {}):
        self.game_state = game_state
        self.question = question
        self.time_out = time_out
        self.winner = winner
        self.score_board = score_board

logger = logging.getLogger('websockets')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
os.environ['PYTHONASYNCIODEBUG'] = '1'
logging.basicConfig(level=logging.DEBUG)
warnings.resetwarnings()

def equation() -> str:
    operators = ['+', '-']
    operator = random.choice(operators)
    a = random.randint(0, 10)
    b = random.randint(0, a)
    return f'{a} {operator} {b}'

def check(answer: int, expression: str) -> bool:
    return (answer == eval(expression))


connected = set()
e = equation()
timer = 30
scoreBoard = {}
winner = None
scheduler = AsyncIOScheduler()


async def counter():
    global connected
    global timer
    global e
    global winner
    timer = timer - 1
    if timer >= 0:
        serverPayload = ServerPayload(game_state = False, question = e, time_out = timer, winner = winner, score_board = scoreBoard)
        for ws in connected:
            await ws.send(json.dumps(serverPayload.__dict__))
    else:
        e = equation()
        timer = 30
        serverPayload = ServerPayload(game_state = False, question = e, time_out = timer, winner = winner, score_board = scoreBoard)
        for ws in connected:
            await ws.send(json.dumps(serverPayload.__dict__))

async def handler(websocket, path):
    # Register.
    if len(connected) == 0:
        scheduler.add_job(counter, 'interval', seconds=1)
        scheduler.start()
    connected.add(websocket)
    global e
    global timer
    global winner
    try:
        # Implement logic here.
        e = equation()
        timer = 30
        serverPayload = ServerPayload(game_state = False, question = e, time_out = timer, winner = winner, score_board = scoreBoard)
        await websocket.send(json.dumps(serverPayload.__dict__))
        async for message in websocket:
            try:
                clientPayload = ClientPayload(**json.loads(message))
                if(clientPayload.answer == eval(e)):
                    scoreBoard.update({clientPayload.name: scoreBoard.get(clientPayload.name, 0) + 1})
                    winner = clientPayload.name
                    e = equation()
                    timer = 30
                    serverPayload = ServerPayload(game_state = True, question = e, time_out = timer, winner = clientPayload.name, score_board = scoreBoard)
                    for ws in connected:
                        await ws.send(json.dumps(serverPayload.__dict__))
                else:
                    serverPayload = ServerPayload(game_state = True, question = e, time_out = timer, winner = clientPayload.name, score_board = scoreBoard)
                    await websocket.send(json.dumps(serverPayload.__dict__))
            except json.decoder.JSONDecodeError:
                print("you sent the wrong JSON")


    finally:
        connected.remove(websocket)
        if len(connected) == 0:
            scheduler.shutdown()


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", type=int,
                    help="specify the port to be set")

parser.add_argument("-n", "--name", type=str,
                    help="specify the IP address to be set")

args = parser.parse_args()
port, ip_address = args.port if args.port else 8080, args.name if args.name else ""

start_server = websockets.serve(handler, ip_address, port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

