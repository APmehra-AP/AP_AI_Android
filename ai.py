# Created by : Amarchand Meghwal

from datetime import datetime


def reply(message):
    msg = message.lower().strip()

    greetings = ["hi", "hello", "hey", "namaste"]

    if msg in greetings:
        return "👋 Hello! Kaise ho?"

    elif msg == "name":
        return "🤖 Mera naam AP AI hai."

    elif msg == "creator":
        return "👨‍💻 Mujhe Amarchand Meghwal ne banaya hai."

    elif msg == "time":
        return "🕒 " + datetime.now().strftime("%I:%M:%S %p")

    elif msg == "date":
        return "📅 " + datetime.now().strftime("%d-%m-%Y")

    elif msg == "version":
        return "🚀 AP AI Android Version 30.0"

    elif msg == "thanks":
        return "😊 Aapka swagat hai."

    elif msg == "how are you":
        return "😊 Main bilkul theek hoon."

    else:
        return "🤔 Mujhe abhi iska jawab nahi pata. Type 'help' for commands."
