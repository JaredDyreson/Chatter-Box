import asyncio
import websockets

async def msg():
    async with websockets.connect('ws://localhost:8765') as websocket:

        await websocket.send('test message')
        msg = await websocket.recv()
        print(msg)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(msg())
    asyncio.get_event_loop().run_forever()
