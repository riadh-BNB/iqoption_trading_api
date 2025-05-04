# iqoption_trading_api

مكتبة Python احترافية للتداول الآلي على منصة IQ Option.

## **المزايا:**
- تسجيل الدخول باستخدام WebSocket.
- واجهة برمجية مرنة وسهلة الاستخدام.
- دعم للتداول اللحظي.

## **المتطلبات:**
- Python 3.7 أو أحدث.
- المكتبة `websockets` للتعامل مع WebSocket.

## **التثبيت:**
قم بتثبيت المكتبة باستخدام الأمر:
```bash
pip install iqoption_trading_api
```

## **الاستخدام:**
### تسجيل الدخول:
```python
import asyncio
from iqoption.authentication import IQOptionClient

async def main():
    username = "your_email@example.com"
    password = "your_password"
    
    client = IQOptionClient(username, password)
    await client.connect()
    await client.login()

if __name__ == "__main__":
    asyncio.run(main())
```

## **المجلدات:**
- `iqoption`: يحتوي على الأكواد الرئيسية للمكتبة.
- `examples`: يحتوي على أمثلة عملية لاستخدام المكتبة.

## **المساهمات:**
مرحب بأي مساهمات لتحسين المكتبة! افتح طلب سحب (Pull Request) أو تواصل معنا عبر قسم القضايا (Issues).
# iqoption_trading_api
