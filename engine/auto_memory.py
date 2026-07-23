# Created by : Amarchand Meghwal

from engine.memory import remember


def auto_memory(text):

    msg = text.strip()
    lower = msg.lower()

    # Name
    if lower.startswith("my name is "):
        value = msg[11:].strip()
        remember("name", value)
        return f"😊 I will remember your name is {value}."

    if lower.startswith("mera naam "):
        value = msg[10:].replace("hai", "").strip()
        remember("name", value)
        return f"😊 मैंने आपका नाम {value} याद रख लिया।"

    # City
    if lower.startswith("my city is "):
        value = msg[11:].strip()
        remember("city", value)
        return f"📍 I will remember your city is {value}."

    if lower.startswith("i live in "):
        value = msg[10:].strip()
        remember("city", value)
        return f"📍 I will remember that you live in {value}."

    # State
    if lower.startswith("i am from "):
        value = msg[10:].strip()
        remember("state", value)
        return f"🗺️ I will remember that you are from {value}."

    if lower.startswith("i'm from "):
        value = msg[9:].strip()
        remember("state", value)
        return f"🗺️ I will remember that you are from {value}."

    # Age
    if lower.startswith("my age is "):
        value = msg[10:].strip()
        remember("age", value)
        return f"🎂 I will remember your age is {value}."

    # Job
    if lower.startswith("i am a "):
        value = msg[7:].strip()
        remember("job", value)
        return f"💼 I will remember you are a {value}."

    if lower.startswith("i work as "):
        value = msg[10:].strip()
        remember("job", value)
        return f"💼 I will remember you work as {value}."

    # Phone
    if lower.startswith("my phone is "):
        value = msg[12:].strip()
        remember("phone", value)
        return f"📱 I will remember your phone is {value}."

    # Education
    if lower.startswith("i am ") and "pass" in lower:
        value = msg[5:].strip()
        remember("education", value)
        return f"🎓 I will remember your education is {value}."

    # Favourite Color
    if lower.startswith("my favourite color is "):
        value = msg[22:].strip()
        remember("favorite_color", value)
        return f"🎨 I will remember your favourite color is {value}."

    # Likes
    if lower.startswith("i like "):
        value = msg[7:].strip()
        remember("likes", value)
        return f"❤️ I will remember that you like {value}."

    if lower.startswith("i love "):
        value = msg[7:].strip()
        remember("likes", value)
        return f"❤️ I will remember that you love {value}."

    # Dislikes
    if lower.startswith("i don't like "):
        value = msg[13:].strip()
        remember("dislikes", value)
        return f"💔 I will remember that you don't like {value}."

    if lower.startswith("i dont like "):
        value = msg[12:].strip()
        remember("dislikes", value)
        return f"💔 I will remember that you don't like {value}."

    # Hobby
    if lower.startswith("my hobby is "):
        value = msg[12:].strip()
        remember("hobby", value)
        return f"🎯 I will remember your hobby is {value}."

    # Goal
    if lower.startswith("my goal is "):
        value = msg[11:].strip()
        remember("goal", value)
        return f"🚀 I will remember your goal is {value}."

    if lower.startswith("my dream is "):
        value = msg[12:].strip()
        remember("goal", value)
        return f"🚀 I will remember your dream is {value}."

    return None
