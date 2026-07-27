# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

# AP AI V4 Stable

AP AI V4 Stable is a personal AI assistant built with Python, Kivy and KivyMD for Android.

## Features

- AI Chat
- Voice Input
- Memory System
- Chat History
- Search
- Profile Management
- Settings
- Notifications
- Dark Theme
- Modular Architecture
- Android Ready

## Project Structure

```
AP_AI_Android/

├── assets/
├── engine/
├── gui/
├── screens/
├── main.py
├── buildozer.spec
├── requirements.txt
└── README.md
```

## Requirements

- Python 3
- Kivy
- KivyMD
- Buildozer
- Android SDK
- Android NDK

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Open the project:

```bash
cd AP_AI_Android
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Android Build

Build the APK:

```bash
buildozer android debug
```

Release build:

```bash
buildozer android release
```

APK output:

```
bin/
```

## Permissions

- Internet
- Microphone
- Vibration

## Modules

- engine
- gui
- screens
- assets

## Author

**Created by : Amarchand Meghwal**

## Version

**AP AI V4 Stable**

## License

This project is intended for educational and personal use.
