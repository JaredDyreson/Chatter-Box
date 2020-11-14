from Chatter.Client import Client
from Chatter.Equations import Generator

import websocket
import json

SERVER_IP = "144.202.127.25"
SERVER_PORT = 8080

class Game():
    def __init__(self, url=SERVER_IP, port=SERVER_PORT, wait_time=15):
        if not(isinstance(url, str) and
               isinstance(port, int) and
               isinstance(wait_time, int)):
               raise ValueError

        self.port = port
        self.url = url
        self.connection = websocket.create_connection(f'ws://{self.url}:{self.port}')

    def get_values(self, payload: dict, keys: list) -> tuple:
        if not(isinstance(payload, dict) and
               isinstance(keys, list)):
               raise ValueError

        return (payload[key] for key in keys)

    def start(self, manifest: list):
        if not(isinstance(manifest, list)):
               raise ValueError

        data = self.connection.recv()
        payload = json.loads(data)
        endpoints = ["game_state", "question", "time_out", "winner", "timestamp"]
        game_state, equation, time_out, winner, timestamp = self.get_values(payload, endpoints)
        G = Generator()
        time, answer = element.get_answer(equation)
        payload = {

        }
        self.connection.send()



        #  this code should be run server side, not client side
        states = []


        for element in manifest:
            time, answer = element.get_answer(equation)
            if(G.check(answer, equation)):
                element.timestamp = time
                states.append(element)

        states.sort(key=lambda x: x.timestamp)

        send_back = {
            'game_state': False,
            'question': equation,
            'time_out': 15,
            'winner': None if not(states) else states[0].name
        }

        print(send_back)
        self.connection.close()
