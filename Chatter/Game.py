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

    def start(self, C1: Client, C2: Client):
        if not(isinstance(C1, Client) and
               isinstance(C2, Client)):
               raise ValueError

        data = self.connection.recv()
        payload = json.loads(data)
        endpoints = ["game_state", "question", "time_out", "winner"]
        game_state, equation, time_out, winner = self.get_values(payload, endpoints)
        G = Generator()

        states = G.check(C1.get_answer(equation), equation), G.check(C2.get_answer(equation), equation)

        if not(any(states)):
            print("no one got the answer")
        else:
            a, b = states
            C1.is_winner, C2.is_winner = states
            declared = None
            if(C1.is_winner):
                declared = C1.name
            else:
                declared = C2.name
            print(f'Client 1: {C1.is_winner}\nClient 2: {C2.is_winner}')
        send_back = {
                    'game_state': False,
                    'question': equation,
                    'time_out': 15,
                    'winner': declared
        }
        print(send_back)
        self.connection.close()
