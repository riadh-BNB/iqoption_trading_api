import asyncio
import websockets
import json
import logging
from websockets.exceptions import WebSocketException

# إعداد نظام تسجيل الأخطاء
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("IQOptionClient")

class IQOptionAuthenticationError(Exception):
    pass

class IQOptionClient:
    def __init__(self, username, password, max_retries=3):
        self.username = username
        self.password = password
        self.websocket_url = "wss://iqoption.com/echo/websocket"
        self.connection = None
        self.max_retries = max_retries

    async def connect(self):
        retries = 0
        while retries < self.max_retries:
            try:
                self.connection = await websockets.connect(self.websocket_url)
                logger.info("Connected to IQ Option WebSocket.")

            
