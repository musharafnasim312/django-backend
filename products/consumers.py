import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ProductConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket connection opened")  # Debug log to verify connection
        await self.channel_layer.group_add("product_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        print("WebSocket connection closed")  # Debug log to verify disconnection
        await self.channel_layer.group_discard("product_updates", self.channel_name)

    # Send a notification when the stock changes
    async def send_product_notification(self, event):
        print(f"Sending product notification: {event}")  # Debug log for notifications
        await self.send(text_data=json.dumps(event["message"]))

    async def receive(self, text_data):
        print(f"Message received: {text_data}")  # Debug log for receiving messages
        # You can add logic to handle incoming WebSocket messages here
