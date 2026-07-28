# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

[app]

title = AP AI

package.name = apai

package.domain = org.apai

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,ttf,json,txt,md

version = 4.0

requirements = python3,kivy,kivymd,requests

orientation = portrait

fullscreen = 0

icon.filename = assets/icon.png

presplash.filename = assets/splash.png

android.api = 34

android.minapi = 24

android.archs = arm64-v8a,armeabi-v7a

android.permissions = INTERNET,RECORD_AUDIO,VIBRATE

android.accept_sdk_license = True

android.logcat_filters = *:S python:D

log_level = 2

[buildozer]

log_level = 2

warn_on_root = 1
