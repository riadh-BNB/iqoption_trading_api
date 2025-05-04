# مسار الملف: examples/login_example.py
# مثال لتسجيل الدخول باستخدام المكتبة.

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
