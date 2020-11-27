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
import threading
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import time

class ClientPayload(object):
    def __init__(self, name, answer):
        self.name = name
        self.answer = answer
        
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



async def counter():
    global connected
    global timer
    global e
    global winner
    timer = timer - 1
    if timer >= 0:
        serverPayload = serverPayload = ServerPayload(game_state = False, question = e, time_out = timer, winner = winner,  score_board = scoreBoard)
        for ws in connected:
            await ws.send(json.dumps(serverPayload.__dict__))
    else:
        e = equation()
        timer = 30
        serverPayload = serverPayload = ServerPayload(game_state = False, question = e, time_out = timer, winner = winner,  score_board = scoreBoard)
        for ws in connected:
            await ws.send(json.dumps(serverPayload.__dict__))

async def handler(websocket, path):
    # Register.
    connected.add(websocket)
    global e
    global timer
    global winner
    try:
        # Implement logic here.
        serverPayload = ServerPayload(game_state = False, question = e, time_out = timer, winner = winner, score_board = scoreBoard)
        await websocket.send(json.dumps(serverPayload.__dict__))
        async for message in websocket:
            clientPayload = ClientPayload(**json.loads(message))
            if(clientPayload.answer == eval(e)):
                print("PENIS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                time.sleep(10)
                scoreBoard.update({clientPayload.name: scoreBoard.get(clientPayload.name, 0) + 1})
                winner = clientPayload.name
                e = equation()
                timer = 30
                serverPayload = ServerPayload(game_state = True, question = e, time_out = timer, winner = clientPayload.name, score_board = scoreBoard)
                for ws in connected:
                    await ws.send(json.dumps(serverPayload.__dict__))
            else:
                await websocket.send(json.dumps(serverPayload.__dict__))

    finally:
        connected.remove(websocket)
        scoreBoard.pop(websocket)




start_server = websockets.serve(handler, "", 8080)

scheduler = AsyncIOScheduler()
scheduler.add_job(counter, 'interval', seconds=1)
scheduler.start()

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



