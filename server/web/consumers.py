import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ScreenShotsConsumer(WebsocketConsumer):
    def connect(self):
        print("user is connect")

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
        message = text_data_json["message"]

        # send chat message event to the room
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
            },
        )

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))
