# Created by : Amarchand Meghwal
# AP AI Android v42.1

from engine.auto_memory import auto_memory


class Brain:

    def __init__(self):

        self.name = "AP AI Brain"
        self.version = "42.1"

    def think(self, text):

        msg = text.strip()

        if not msg:
            return {
                "type": "chat",
                "intent": "chat",
                "reply": "⚠️ Empty command.",
                "tasks": ["chat"],
            }

        lower = msg.lower()

        # -----------------------------
        # Auto Memory
        # -----------------------------

        memory_reply = auto_memory(msg)

        if memory_reply:

            return {
                "type": "memory",
                "intent": "auto_memory",
                "reply": memory_reply,
                "tasks": ["memory"],
            }

        # -----------------------------
        # Intent Detection
        # -----------------------------

        tasks = []

        # AI

        if lower.startswith("ai "):
            tasks.append("ai")

        # Search

        elif lower.startswith("search "):
            tasks.append("search")

        # Weather

        elif lower.startswith("weather "):
            tasks.append("weather")

        # Date

        elif lower == "date":
            tasks.append("date")

        # Time

        elif lower == "time":
            tasks.append("time")

        # Version

        elif lower == "version":
            tasks.append("version")

        # About AP AI

        elif lower in (
            "who are you",
            "about",
            "about ap",
            "about ap ai",
        ):
            tasks.append("about")

        # Calculator

        elif (
            any(op in msg for op in ["+", "-", "*", "/"])
            or lower.startswith(("square ", "cube ", "sqrt "))
        ):
            tasks.append("calculator")

        # Memory

        elif (
            lower.startswith(("remember ", "remember my ", "recall "))
            or lower == "memory"
        ):
            tasks.append("memory_command")

        # History

        elif lower in ("history", "clear history"):
            tasks.append("history")

        # Settings

        elif lower == "settings" or lower.startswith("set "):
            tasks.append("settings")

        # Help

        elif lower == "help":
            tasks.append("help")

        # Voice

        elif lower == "voice":
            tasks.append("voice")

        # Exit

        elif lower in (
            "bye",
            "exit",
            "quit",
        ):
            tasks.append("exit")

        # Default Chat

        else:
            tasks.append("chat")

        return {
            "type": tasks[0],
            "intent": tasks[0],
            "reply": None,
            "tasks": tasks,
        }


brain = Brain()
