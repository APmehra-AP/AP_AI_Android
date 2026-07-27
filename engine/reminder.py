# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reminder Manager
"""

from datetime import datetime


class ReminderManager:

    def __init__(self):
        self.reminders = []

    def add(self, title, reminder_time, note=""):
        """
        Add a reminder.

        reminder_time format:
        YYYY-MM-DD HH:MM
        """

        item = {
            "title": str(title),
            "note": str(note),
            "time": str(reminder_time),
            "completed": False
        }

        self.reminders.append(item)

        return item

    def all(self):
        """
        Return all reminders.
        """

        return list(self.reminders)

    def remove(self, index):
        """
        Remove reminder by index.
        """

        if 0 <= index < len(self.reminders):
            del self.reminders[index]
            return True

        return False

    def complete(self, index):
        """
        Mark reminder as completed.
        """

        if 0 <= index < len(self.reminders):
            self.reminders[index]["completed"] = True
            return True

        return False

    def pending(self):
        """
        Return pending reminders.
        """

        return [
            item
            for item in self.reminders
            if not item["completed"]
        ]

    def due(self):
        """
        Return reminders whose time has passed.
        """

        now = datetime.now()

        due_items = []

        for item in self.reminders:

            if item["completed"]:
                continue

            try:
                reminder_time = datetime.strptime(
                    item["time"],
                    "%Y-%m-%d %H:%M"
                )

                if reminder_time <= now:
                    due_items.append(item)

            except Exception:
                continue

        return due_items

    def clear(self):
        """
        Remove all reminders.
        """

        self.reminders.clear()

    def count(self):
        """
        Total reminders.
        """

        return len(self.reminders)


reminders = ReminderManager()
