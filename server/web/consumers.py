import json
import base64

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.core.files.base import ContentFile
from django.contrib.auth.models import User

from .models import ScreenShot


class ScreenShotsConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = "chat_0"

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

        image = text_data_json["image"]
        created = text_data_json["created"]
        filename = text_data_json["filename"]

        bytes_data = base64.b64decode(image)

        u = User.objects.get(id=1)

        shot = ScreenShot.objects.create(created=created, user=u)
        shot.image.save(f"{filename}.png", ContentFile(bytes_data), save=True)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "send_message",
                "message": "ok",
            },
        )

    def send_message(self, event):
        self.send(text_data=json.dumps(event))
