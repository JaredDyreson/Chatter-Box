#!/usr/bin/env python3.8

import requests
import json

port = 8081
url = f'http://remote.belownitrogen.com:{port}'

x = requests.get(url)
print(x)

quit()

payload = {
    "expression": "50 50 +"
}

x = requests.post(url, data=payload)
resultant = json.loads(requests.get(url).text)['evaluation']
print(f'sending {payload}')
print(f'recieved: {resultant}')
