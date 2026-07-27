# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Notification Manager
"""

from datetime import datetime


class Notification:
    def __init__(
        self,
        title,
        message,
        level="info"
    ):
        self.title = title
        self.message = message
        self.level = level
        self.time = datetime.now()

    def to_dict(self):
        return {
            "title": self.title,
            "message": self.message,
            "level": self.level,
            "time": self.time.strftime("%Y-%m-%d %H:%M:%S")
        }


class NotificationManager:
    def __init__(self):
        self.notifications = []

    def push(self, title, message, level="info"):
        """
        Add a notification.
        """

        notification = Notification(
            title,
            message,
            level
        )

        self.notifications.append(notification)

        return notification

    def info(self, message):
        return self.push(
            "Information",
            message,
            "info"
        )

    def success(self, message):
        return self.push(
            "Success",
            message,
            "success"
        )

    def warning(self, message):
        return self.push(
            "Warning",
            message,
            "warning"
        )

    def error(self, message):
        return self.push(
            "Error",
            message,
            "error"
        )

    def latest(self):
        """
        Return latest notification.
        """

        if not self.notifications:
            return None

        return self.notifications[-1]

    def all(self):
        """
        Return all notifications.
        """

        return [
            item.to_dict()
            for item in self.notifications
        ]

    def clear(self):
        """
        Remove all notifications.
        """

        self.notifications.clear()

    def count(self):
        """
        Total notifications.
        """

        return len(self.notifications)


notifications = NotificationManager()
