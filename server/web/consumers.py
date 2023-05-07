import json
import base64

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.core.files.base import ContentFile
from django.contrib.auth.models import User

from .models import ScreenShot


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

        self.room_group_name = f"client_{self.user.username}"

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)

        # Receive screenshot
        if text_data_json.get("screenshot"):
            data = text_data_json["screenshot"]

            image = data["image"]
            created = data["created"]
            filename = data["filename"]

            bytes_data = base64.b64decode(image)

            shot = ScreenShot.objects.create(created=created, user=self.user)
            shot.image.save(f"{filename}.png", ContentFile(bytes_data), save=True)

        # Receive result command
        elif text_data_json.get("result_command"):
            result_command = text_data_json["result_command"]
            print(f"result command : {result_command}")

    def send_message(self, event):
        self.send(text_data=json.dumps(event))


class CommandConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.room_group_name = f"browser_{self.user.username}"

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)

    def send_message(self, event):
        self.send(text_data=json.dumps(event))
