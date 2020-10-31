#!/usr/bin/env python3.8

from Chatter.Client import Client
from Chatter.Equations import Generator

import socket
import json

SERVER_IP = "144.202.127.25"
SERVER_PORT = 8080

class Server():
    def __init__(self, url=SERVER_IP, port=SERVER_PORT, wait_time=15):
        if not(isinstance(url, str) and
               isinstance(port, int) and
               isinstance(wait_time, int)):
               raise ValueError

        self.port = port
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect((url, port))

    def get_values(self, payload: dict, keys: list) -> tuple:
        if not(isinstance(payload, dict) and
               isinstance(keys, list)):
               raise ValueError

        return (payload[key] for key in keys)

    def start(self, C1: Client, C2: Client):
        if not(isinstance(C1, Client) and
               isinstance(C2, Client)):
               raise ValueError

        G = Generator()
        data = self.sock.recv(512)
        payload = json.loads(data.decode("utf-8").replace("'",'"'))
        endpoints = ["game_state", "question", "time_out", "winner"]
        game_state, equation, time_out, winner = self.get_values(payload, endpoints)

        states = G.check(C1.get_answer(equation), equation), G.check(C2.get_answer(equation), equation)

        if not(any(states)):
            print("no one got the answer")
        else:
            a, b = states
            C1.is_winner, C2.is_winner = states
            print(f'Client 1: {C1.is_winner}\nClient 2: {C2.is_winner}')
        send_back = {
                    'game_state': False,
                    'question': '2+2',
                    'time_out': 15,
                    'winner': C1.name if C1.is_winner else C2.name
        }
        print(send_back)
        self.sock.close()

