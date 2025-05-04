# مسار الملف: iqoption/authentication.py
# يحتوي على كود لتسجيل الدخول والتعامل مع WebSocket.
import asyncio
import websockets
import json

class IQOptionAuthenticationError(Exception):
    pass

class IQOptionClient:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.websocket_url = "wss://iqoption.com/echo/websocket"
        self.connection = None

    async def connect(self):
        try:
            self.connection = await websockets.connect(self.websocket_url)
            print("Connected to IQ Option WebSocket.")
        except Exception as e:
            raise ConnectionError("Failed to connect to IQ Option WebSocket.") from e

    async def login(self):
        if not self.connection:
            raise ValueError("WebSocket connection is not established. Call 'connect' first.")
        
        login_payload = {
            "name": "ssid",
            "msg": {
                "email": self.username,
                "password": self.password
            }
        }
        await self.connection.send(json.dumps(login_payload))
        response = await self.connection.recv()
        response_data = json.loads(response)

        if response_data.get("name") == "authenticated" and response_data["msg"] is True:
            print("Login successful!")
        else:
            raise IQOptionAuthenticationError("Login failed. Check your username and password.")
