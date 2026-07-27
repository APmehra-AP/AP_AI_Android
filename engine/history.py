# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Conversation History Manager
"""

from collections import deque
from engine.config import MAX_HISTORY


class HistoryManager:
    def __init__(self, limit=MAX_HISTORY):
        self.limit = limit
        self.history = deque(maxlen=limit)

    def add(self, role, message):
        """Add a message to history."""
        self.history.append({
            "role": role,
            "message": str(message).strip()
        })

    def clear(self):
        """Clear history."""
        self.history.clear()

    def get(self):
        """Return history as list."""
        return list(self.history)

    def last(self):
        """Return last message."""
        if self.history:
            return self.history[-1]
        return None

    def count(self):
        """Return total messages."""
        return len(self.history)

    def export_text(self):
        """Return formatted conversation."""
        lines = []

        for item in self.history:
            role = item["role"].capitalize()
            msg = item["message"]
            lines.append(f"{role}: {msg}")

        return "\n".join(lines)


# Global history instance
history = HistoryManager()
