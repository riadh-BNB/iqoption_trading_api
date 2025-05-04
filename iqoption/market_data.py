# مسار الملف: iqoption/market_data.py
# يحتوي على وظائف لجلب بيانات السوق (الأسعار والشموع).

import json

class MarketDataError(Exception):
    pass

class IQOptionMarketData:
    def __init__(self, connection):
        self.connection = connection

    async def get_candles(self, asset, interval, count):
        """
        جلب بيانات الشموع (Candlesticks) لأصل معين.
        
        Parameters:
        - asset (str): اسم الأصل (مثل EURUSD).
        - interval (int): مدة الشمعة بالثواني (مثل 60 للشموع الدقيقة).
        - count (int): عدد الشموع المطلوبة.

        Returns:
        - list: قائمة تحتوي على بيانات الشموع.
        """
        if not self.connection:
            raise ValueError("WebSocket connection is not established. Please connect first.")
        
        candles_payload = {
            "name": "get-candles",
            "msg": {
                "asset": asset,
                "interval": interval,
                "count": count
            }
        }
        await self.connection.send(json.dumps(candles_payload))
        response = await self.connection.recv()
        response_data = json.loads(response)

        if response_data.get("name") == "candles" and response_data.get("msg"):
            print(f"Received {count} candles for {asset}.")
            return response_data["msg"]
        else:
            raise MarketDataError("Failed to fetch market data. Please check your parameters.")
