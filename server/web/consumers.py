import json
import base64

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.core.files.base import ContentFile
from django.contrib.auth.models import User

from .models import ScreenShot


SCREENSHOT = "screenshot"
RESULT_COMMAND = "result_command"
COMMAND = "command"


def get_client_connection_name(username):
    return f"client_{username}"


def get_browser_connection_name(username):
    return f"browser_{username}"


class ScreenShotsConsumer(WebsocketConsumer):
    def connect(self):
        auth = dict(self.scope["headers"]).get(b"auth").decode()
        username, password = auth.split(":")

        # Check username exist
        try:
            self.user = User.objects.get(username=username)
        except User.DoesNotExist:
            return

        # Check password
        if not self.user.check_password(password):
            return

        self.connection_name = get_client_connection_name(self.user.username)

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.connection_name,
            self.channel_name,
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.connection_name,
            self.channel_name,
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)

        # Receive screenshot
        if text_data_json.get(SCREENSHOT):
            data = text_data_json[SCREENSHOT]

            image = data["image"]
            created = data["created"]
            filename = data["filename"]

            bytes_data = base64.b64decode(image)

            shot = ScreenShot.objects.create(created=created, user=self.user)
            shot.image.save(f"{filename}.png", ContentFile(bytes_data), save=True)

        # Receive result command
        elif text_data_json.get(RESULT_COMMAND):
            result_command = text_data_json[RESULT_COMMAND]
            async_to_sync(self.channel_layer.group_send)(
                get_browser_connection_name(self.user.username),
                {
                    "type": "send_message",
                    "result_command": result_command,
                },
            )

    def send_message(self, event):
        self.send(text_data=json.dumps(event))


class CommandConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.connection_name = get_browser_connection_name(self.user.username)

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.connection_name,
            self.channel_name,
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.connection_name,
            self.channel_name,
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)

        if text_data_json.get(COMMAND):
            command = text_data_json[COMMAND]
            async_to_sync(self.channel_layer.group_send)(
                get_client_connection_name(self.user.username),
                {
                    "type": "send_message",
                    "command": command,
                },
            )

    def send_message(self, event):
        self.send(text_data=json.dumps(event))
