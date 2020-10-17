#!/usr/bin/env python3.8

import socket
import ast
import json

class Client():
    def __init__(self, name: str):
        if not(isinstance(name, str)):
            raise ValueError

        self.name = name
        self.answer = None
        self.is_winner = False

    def get_answer(self):
       self.answer = input("what is 2 + 2 ?: ")
       return self.answer


    def get_values(self, payload: dict, keys: list) -> tuple:
        return (payload[key] for key in keys)


class Server():
    def __init__(self, url: str, port: int, wait_time=15):
        if not(isinstance(url, str) and
               isinstance(port, int) and
               isinstance(wait_time, int)):
               raise ValueError

        self.port = port
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect((url, port))
        # self.sock.bind(('', self.port))
        # self.sock.listen(wait_time)

    def start(self, C1: Client, C2: Client):
        if not(isinstance(C1, Client) and
               isinstance(C2, Client)):
               raise ValueError

        answer_one, answer_two = C1.get_answer(), C2.get_answer()

        while(True):
            data = self.sock.recv(512)
            pay = json.loads(data.decode("utf-8").replace("'",'"'))
            # game_state, question, time_out, winner = get_values(pay, ["game_state", "question", "time_out", "winner"])

            if not(eval("2+2") == 4):
                sock.close()
                break
            else:
                print(data)
                # print(state, question, time_out, winner)


url = "remote.belownitrogen.com"
port = 8081

C1 = Client("JOHN")
C2 = Client("JARED")

S = Server(url, port)
S.start(C1, C2)

# sock.connect((url, port))

