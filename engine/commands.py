# Created by : Amarchand Meghwal
# AP AI Android v42.3

from engine.chat import chat
from engine.brain import brain
from engine.ai import ai
from engine.weather import weather

from engine.memory import (
    remember,
    recall,
    show_memory,
)

from engine.history import (
    add_history,
    show_history,
    clear_history,
)

from engine.calculator import (
    calculate,
    square,
    cube,
    sqrt,
)

from engine.search import search

from engine.settings import (
    show_settings,
    set_setting,
)


def execute(command):

    cmd = command.strip()

    if not cmd:
        return "⚠️ Empty command."

    lower = cmd.lower()

    # ----------------------------
    # Save History
    # ----------------------------

    if lower not in (
        "history",
        "clear history",
    ):
        add_history(cmd)

    # ----------------------------
    # Brain Decision
    # ----------------------------

    try:
        decision = brain.think(cmd)

    except Exception as e:
        return f"🧠 Brain Error:\n{e}"

    decision_type = decision.get("type", "chat")

    # ----------------------------
    # Exit
    # ----------------------------

    if decision_type == "exit":
        return "👋 Goodbye AP!"

    # ----------------------------
    # Auto Memory Reply
    # ----------------------------

    if decision_type == "memory":
        return decision.get(
            "reply",
            "Memory updated.",
        )

    # ----------------------------
    # History
    # ----------------------------

    if decision_type == "history":

        if lower == "history":
            return show_history()

        if lower == "clear history":
            return clear_history()

    # ----------------------------
    # AI
    # ----------------------------

    if decision_type == "ai":

        question = cmd[3:].strip()

        if not question:
            return "🤖 Ask something after ai"

        try:
            return ai.ask(question)

        except Exception as e:
            return f"AI Error:\n{e}"

    # ----------------------------
    # Weather
    # ----------------------------

    if decision_type == "weather":

        city = cmd[8:].strip()

        if not city:
            return "🌤️ Use: weather <city>"

        try:
            return weather(city)

        except Exception as e:
            return f"Weather Error:\n{e}"

    # ----------------------------
    # Search
    # ----------------------------

    if decision_type == "search":

        query = cmd[7:].strip()

        if not query:
            return "🔍 What do you want to search?"

        try:
            return search(query)

        except Exception as e:
            return f"Search Error:\n{e}"

    # ----------------------------
    # Calculator
    # ----------------------------

    if decision_type == "calculator":

        try:

            if any(op in cmd for op in ["+", "-", "*", "/"]):

                result = calculate(cmd)

                if result is not None:
                    return result

            if lower.startswith("square "):
                return square(cmd[7:].strip())

            if lower.startswith("cube "):
                return cube(cmd[5:].strip())

            if lower.startswith("sqrt "):
                return sqrt(cmd[5:].strip())

        except Exception as e:
            return f"Calculator Error:\n{e}"

    # ----------------------------
    # Memory Commands
    # ----------------------------

    if decision_type == "memory_command":

        if lower.startswith("remember my "):

            text = cmd[12:].strip()
            parts = text.split(maxsplit=1)

            if len(parts) != 2:
                return "Use: remember my name AP"

            return remember(parts[0], parts[1])

        if lower.startswith("remember "):

            text = cmd[9:].strip()
            parts = text.split(maxsplit=1)

            if len(parts) != 2:
                return "Use: remember key value"

            return remember(parts[0], parts[1])

        if lower.startswith("recall "):
            return recall(cmd[7:].strip())

        if lower == "memory":
            return show_memory()

    # ----------------------------
    # Settings
    # ----------------------------

    if decision_type == "settings":

        if lower == "settings":
            return show_settings()

        if lower.startswith("set "):

            text = cmd[4:].strip()

            if "=" not in text:
                return "Use: set key=value"

            key, value = text.split("=", 1)

            return set_setting(
                key.strip(),
                value.strip(),
            )

    # ----------------------------
    # Default Chat
    # ----------------------------

    try:

        reply = chat.reply(cmd)

        if reply:
            return reply

    except Exception:
        pass

    return (
        "🤔 Mujhe abhi iska jawab nahi pata.\n"
        "💡 Type 'help' to see available commands."
    )
