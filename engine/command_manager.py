# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Command Manager
Handles built-in AP AI commands.
"""

from engine.chat_manager import chat
from engine.settings import settings


class CommandManager:

    def __init__(self):
        self.chat = chat

    def execute(self, command):
        """
        Execute built-in commands.
        """

        if command is None:
            return None

        command = str(command).strip()

        if not command.startswith("/"):
            return None

        parts = command.split(maxsplit=1)

        name = parts[0].lower()
        argument = parts[1] if len(parts) > 1 else ""

        # -----------------------------
        # Help
        # -----------------------------
        if name == "/help":
            return {
                "success": True,
                "message": (
                    "Available Commands:\n"
                    "/help\n"
                    "/clear\n"
                    "/history\n"
                    "/remember key=value\n"
                    "/recall key\n"
                    "/forget key\n"
                    "/settings"
                )
            }

        # -----------------------------
        # Clear history
        # -----------------------------
        if name == "/clear":
            self.chat.clear_history()

            return {
                "success": True,
                "message": "Conversation history cleared."
            }

        # -----------------------------
        # Show history
        # -----------------------------
        if name == "/history":
            return {
                "success": True,
                "message": self.chat.history_text()
            }

        # -----------------------------
        # Remember
        # -----------------------------
        if name == "/remember":

            if "=" not in argument:
                return {
                    "success": False,
                    "message": "Usage: /remember key=value"
                }

            key, value = argument.split("=", 1)

            self.chat.remember(
                key.strip(),
                value.strip()
            )

            return {
                "success": True,
                "message": "Memory saved."
            }

        # -----------------------------
        # Recall
        # -----------------------------
        if name == "/recall":

            value = self.chat.recall(argument.strip())

            if value is None:
                value = "Not found."

            return {
                "success": True,
                "message": str(value)
            }

        # -----------------------------
        # Forget
        # -----------------------------
        if name == "/forget":

            self.chat.forget(argument.strip())

            return {
                "success": True,
                "message": "Memory removed."
            }

        # -----------------------------
        # Settings
        # -----------------------------
        if name == "/settings":

            values = settings.all()

            text = "\n".join(
                f"{k}: {v}"
                for k, v in values.items()
            )

            return {
                "success": True,
                "message": text
            }

        return {
            "success": False,
            "message": "Unknown command."
        }


commands = CommandManager()
