from website.models import *
from channels.generic.websocket import WebsocketConsumer
import json
import time
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class TestConsumer(WebsocketConsumer):

    def connect(self):
        self.channel_layer = get_channel_layer()
        self.mess = "test"
        group_add_sync = async_to_sync(self.channel_layer.group_add)
        group_add_sync(self.mess, self.channel_name)
        self.accept()
        time.sleep(600)

    def disconnect(self, close_code):

        if self.channel_layer:
            self.channel_layer.group_discard(self.mess, self.channel_name)

    def receive(self, text_data):

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        save = history(message=message, PFI=True)
        save.save()

        self.channel_layer.group_send(self.mess,{
                "type": "chat_message",
                "message": message
                })

