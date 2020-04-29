import json
from channels.generic.websocket import WebsocketConsumer

from asgiref.sync import async_to_sync


class PlayConsumer(WebsocketConsumer):

    def connect(self):
        pass

    def disconnect(self, close_code):
        pass
