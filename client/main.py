import os
import requests
import time
import pyscreenshot as ImageGrab
from datetime import datetime


import secret

USERNAME = secret.USERNAME
PASSWORD = secret.PASSWORD

UPLOAD_URL = "http://127.0.0.1:8000/upload/"
LOGIN_URL = "http://127.0.0.1:8000/account/login/"

SHOT_TIME = secret.SHOT_TIME
MEDIA_FOLDER_NAME = "media"


def create_meida_folder():
    if not os.path.exists(MEDIA_FOLDER_NAME):
        os.makedirs(MEDIA_FOLDER_NAME)


def take_screenshot(filename):
    create_meida_folder()
    screenshot = ImageGrab.grab()
    screenshot.save(f"{MEDIA_FOLDER_NAME}/{filename}.png")


def login_user(session):
    res = session.get(LOGIN_URL)
    csrf_token = res.cookies["csrftoken"]
    session.post(
        LOGIN_URL,
        data={
            "username": USERNAME,
            "password": PASSWORD,
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

    session.post(UPLOAD_URL, files=files, data=data)


with requests.Session() as session:
    session = requests.Session()
    login_user(session)

    while True:
        time.sleep(SHOT_TIME)
        created = datetime.now()
        filename = created.strftime("%Y-%m-%d_%H-%M-%S")
        take_screenshot(filename)
        send_screenshot_to_server(session, filename, created)
