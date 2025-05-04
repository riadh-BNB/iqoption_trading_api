# مسار الملف: setup.py
# ملف إعداد المكتبة لتثبيتها باستخدام pip.

from setuptools import setup, find_packages

setup(
    name="iqoption_trading_api",
    version="0.1.0",
    description="مكتبة Python احترافية للتداول الآلي على منصة IQ Option.",
    author="Riadh-BNB",
    author_email="your_email@example.com",
    packages=find_packages(),
    install_requires=[
        "websockets>=10.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
