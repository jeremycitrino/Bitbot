[app]
title = TradingBot
package.name = tradingbot
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,json
version = 0.1
requirements = python3,kivy,plyer,pyjnius,yfinance,pandas,numpy,requests,urllib3
osx.python_version = 3
osx.kivy_version = 2.1.0
android.permissions = INTERNET, WAKE_LOCK, FOREGROUND_SERVICE
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30
android.ant_commands = release
