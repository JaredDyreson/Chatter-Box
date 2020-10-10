#!/usr/bin/env python3.8

import requests
import json

url = "http://127.0.0.1:5000/api"

payload = {
    "expression": "50 50 +"
}

x = requests.post(url, data=payload)
resultant = json.loads(requests.get(url).text)['evaluation']
print(f'sending {payload}')
print(f'recieved: {resultant}')
