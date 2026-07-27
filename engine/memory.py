# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Memory Manager
Stores long-term user information.
"""

import json
import os

from engine.config import MAX_MEMORY


class MemoryManager:
    def __init__(self, filename="memory.json"):
        self.filename = filename
        self.memory = {}
        self.load()

    def load(self):
        """Load memory from disk."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    self.memory = json.load(file)
            except Exception:
                self.memory = {}
        else:
            self.memory = {}

    def save(self):
        """Save memory to disk."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                self.memory,
                file,
                ensure_ascii=False,
                indent=4
            )

    def set(self, key, value):
        """Save a memory value."""
        if len(self.memory) >= MAX_MEMORY and key not in self.memory:
            return False

        self.memory[str(key)] = value
        self.save()
        return True

    def get(self, key, default=None):
        """Get a memory value."""
        return self.memory.get(str(key), default)

    def delete(self, key):
        """Delete a memory value."""
        if str(key) in self.memory:
            del self.memory[str(key)]
            self.save()
            return True
        return False

    def exists(self, key):
        """Check if key exists."""
        return str(key) in self.memory

    def clear(self):
        """Clear all memory."""
        self.memory.clear()
        self.save()

    def all(self):
        """Return all memory."""
        return dict(self.memory)

    def count(self):
        """Return number of stored items."""
        return len(self.memory)


# Global memory instance
memory = MemoryManager()
