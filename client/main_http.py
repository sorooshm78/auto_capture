import os
import requests
import time
import pyscreenshot as ImageGrab
from datetime import datetime

import config


def create_meida_folder():
    if not os.path.exists(config.MEDIA_FOLDER_NAME):
        os.makedirs(config.MEDIA_FOLDER_NAME)


def take_screenshot(filename):
    create_meida_folder()
    screenshot = ImageGrab.grab()
    screenshot.save(f"{config.MEDIA_FOLDER_NAME}/{filename}.png")


def login_user(session):
    res = session.get(config.LOGIN_URL)
    csrf_token = res.cookies["csrftoken"]
    session.post(
        config.LOGIN_URL,
        data={
            "username": config.USERNAME,
            "password": config.PASSWORD,
            "csrfmiddlewaretoken": csrf_token,
        },
    )


def send_screenshot_to_server(session, filename, created):
    files = {
        "image": open(f"media/{filename}.png", "rb"),
    }

    data = {
        "created": created.isoformat(),
    }

    session.post(config.UPLOAD_URL, files=files, data=data)


if __name__ == "__main__":
    with requests.Session() as session:
        session = requests.Session()
        login_user(session)

        while True:
            created = datetime.now()
            filename = created.strftime("%Y-%m-%d_%H-%M-%S")
            take_screenshot(filename)
            send_screenshot_to_server(session, filename, created)
            time.sleep(config.SHOT_TIME)
