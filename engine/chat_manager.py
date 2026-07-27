# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Chat Manager
Coordinates chat history, memory and AI client.
"""

from engine.ai_client import ai_client
from engine.history import history
from engine.memory import memory


class ChatManager:

    def __init__(self):
        self.ai = ai_client
        self.history = history
        self.memory = memory

    def build_prompt(self, message):
        """
        Build prompt using stored memory.
        """

        memory_data = self.memory.all()

        if not memory_data:
            return message

        memory_text = "\n".join(
            f"{key}: {value}"
            for key, value in memory_data.items()
        )

        return (
            "User Memory:\n"
            f"{memory_text}\n\n"
            f"User Message:\n{message}"
        )

    def send(self, message):
        """
        Send message to AI.
        """

        message = str(message).strip()

        if not message:
            return {
                "success": False,
                "message": "Message cannot be empty."
            }

        self.history.add("user", message)

        prompt = self.build_prompt(message)

        result = self.ai.ask(
            prompt,
            history=self.history.get()
        )

        if result.get("success"):

            reply = result["message"]

            self.history.add(
                "assistant",
                reply
            )

        return result

    def clear_history(self):
        """
        Clear conversation history.
        """

        self.history.clear()

    def history_text(self):
        """
        Export history as text.
        """

        return self.history.export_text()

    def remember(self, key, value):
        """
        Store long-term memory.
        """

        return self.memory.set(key, value)

    def recall(self, key, default=None):
        """
        Recall stored memory.
        """

        return self.memory.get(key, default)

    def forget(self, key):
        """
        Delete stored memory.
        """

        return self.memory.delete(key)


chat = ChatManager()
