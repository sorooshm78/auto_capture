import pyscreenshot as ImageGrab
import requests
from datetime import datetime

import secret

USERNAME = secret.USERNAME
PASSWORD = secret.PASSWORD

UPLOAD_URL = "http://127.0.0.1:8000/upload/"
LOGIN_URL = "http://127.0.0.1:8000/account/login/"

SHOT_TIME = secret.SHOT_TIME
MEDIA_FOLDER_NAME = "media"


def take_screenshot(filename):
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


def send_screenshot_to_server(session, filename):
    files = {"image": open(f"media/{filename}.png", "rb")}
    session.post(UPLOAD_URL, files=files)


with requests.Session() as session:
    session = requests.Session()
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    take_screenshot(filename)
    login_user(session)
    send_screenshot_to_server(session, filename)
