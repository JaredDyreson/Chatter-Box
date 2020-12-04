from Chatter.Client import Client
from Chatter.Equations import Generator

import asyncio
import websocket
import json

SERVER_IP = "144.202.127.25"
SERVER_PORT = 8080

# SERVER_IP = "localhost"
# SERVER_PORT = 8080

class Game():
    def __init__(self, url=SERVER_IP, port=SERVER_PORT, wait_time=15):
        if not(isinstance(url, str) and
               isinstance(port, int) and
               isinstance(wait_time, int)):
               raise ValueError

        self.port = port
        self.url = url
        self.connection = self.establish_connection()

    def establish_connection(self):
        return websocket.create_connection(f'ws://{self.url}:{self.port}')
