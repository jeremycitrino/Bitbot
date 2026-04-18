[app]

title = TradingBot
package.name = tradingbot
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,json
version = 0.1
requirements = python3,kivy,plyer,pyjnius,yfinance,pandas,numpy,requests,urllib3
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, WAKE_LOCK, FOREGROUND_SERVICE
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30
android.entrypoint = org.kivy.android.PythonActivity
android.release = True
android.debug = False
android.verbose = False
android.log_level = info
android.source = 1.8
android.target = 1.8
android.android_support = True
android.androidx = True
android.arch = arm64-v8a
pyjnius = True
plyer = True
