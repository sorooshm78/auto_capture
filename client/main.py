import pyscreenshot as ImageGrab
from datetime import datetime

import settings
import requests


def take_screenshot(filename):
    screenshot = ImageGrab.grab()
    screenshot.save(f"media/{filename}.png")


def login_user(session):
    res = session.get(settings.LOGIN_URL)
    csrf_token = res.cookies["csrftoken"]
    res = session.post(
        settings.LOGIN_URL,
        data={
            "username": settings.USERNAME,
            "password": settings.PASSWORD,
            "csrfmiddlewaretoken": csrf_token,
        },
    )


def send_screenshot_to_server(session, filename):
    files = {"image": open(f"media/{filename}.png", "rb")}
    res = session.post(settings.UPLOAD_URL, files=files)


with requests.Session() as session:
    session = requests.Session()
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    take_screenshot(filename)
    login_user(session)
    send_screenshot_to_server(session, filename)
