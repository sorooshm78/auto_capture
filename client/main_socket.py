import pyscreenshot as ImageGrab
import websockets
import asyncio
import base64
import json

from datetime import datetime

import config


async def send_screenshot(websocket):
    while True:
        now = datetime.now()

        created = now.isoformat()
        filename = now.strftime("%Y-%m-%d_%H-%M-%S")
        file_path = f"{config.MEDIA_FOLDER_NAME}/{filename}.png"

        # take screenshot
        screenshot = ImageGrab.grab()
        screenshot.save(file_path)

        with open(file_path, "rb") as f:
            image = f.read()

        image_data = base64.b64encode(image).decode("utf-8")

        data = json.dumps(
            {
                "image": image_data,
                "created": created,
                "filename": filename,
            }
        )

        await websocket.send(data)
        await asyncio.sleep(config.SHOT_TIME)


async def receive_message(websocket):
    while True:
        async for message in websocket:
            print("Received message:", message)


async def main(websocket):
    send_task = asyncio.create_task(send_screenshot(websocket))
    receive_task = asyncio.create_task(receive_message(websocket))
    await asyncio.gather(send_task, receive_task)


async def connect_and_run():
    async with websockets.connect(config.WEBSOCKET_URL) as websocket:
        await main(websocket)


asyncio.run(connect_and_run())
