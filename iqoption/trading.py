# مسار الملف: iqoption/trading.py
# يحتوي على وظائف فتح وإغلاق الصفقات.
import json

class TradeError(Exception):
    pass

class IQOptionTrade:
    def __init__(self, connection):
        self.connection = connection

    async def open_trade(self, asset, amount, direction, expiration_time):
        """
        فتح صفقة جديدة على IQ Option.
        
        Parameters:
        - asset (str): اسم الأصل (مثل EURUSD).
        - amount (float): مبلغ الاستثمار.
        - direction (str): اتجاه الصفقة ("call" أو "put").
        - expiration_time (int): وقت انتهاء الصفقة بالدقائق.

        Returns:
        - dict: تفاصيل الصفقة المفتوحة.
        """
        if not self.connection:
            raise ValueError("WebSocket connection is not established. Please connect first.")
        
        trade_payload = {
            "name": "binary-options.open-option",
            "msg": {
                "asset": asset,
                "amount": amount,
                "direction": direction,
                "expiration": expiration_time
            }
        }
        await self.connection.send(json.dumps(trade_payload))
        response = await self.connection.recv()
        response_data = json.loads(response)

        if response_data.get("name") == "option-opened" and response_data["msg"].get("success"):
            print("Trade opened successfully!")
            return response_data["msg"]
        else:
            raise TradeError("Failed to open trade. Please check your parameters and try again.")
