# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable Notification Panel
"""

from datetime import datetime

from kivymd.uix.card import MDCard
from kivymd.uix.list import (
    MDList,
    MDListItem,
    MDListItemHeadlineText,
    MDListItemSupportingText,
)
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout


class NotificationPanel(MDCard):
    """
    Reusable notification panel.
    """

    def __init__(self, max_notifications=100, **kwargs):
        super().__init__(**kwargs)

        self.max_notifications = max_notifications
        self.notifications = []

        self.orientation = "vertical"
        self.padding = "8dp"
        self.radius = [12, 12, 12, 12]
        self.elevation = 1

        self.scroll = MDScrollView()

        self.container = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True
        )

        self.list_view = MDList()

        self.container.add_widget(self.list_view)
        self.scroll.add_widget(self.container)
        self.add_widget(self.scroll)

    # --------------------------------------------------

    def add_notification(self, title, message):

        time_text = datetime.now().strftime("%H:%M")

        item = MDListItem()

        item.add_widget(
            MDListItemHeadlineText(
                text=str(title)
            )
        )

        item.add_widget(
            MDListItemSupportingText(
                text=f"{message}\n{time_text}"
            )
        )

        self.list_view.add_widget(item)

        self.notifications.append({
            "title": str(title),
            "message": str(message),
            "time": time_text
        })

        while len(self.notifications) > self.max_notifications:
            self.notifications.pop(0)

            if self.list_view.children:
                self.list_view.remove_widget(
                    self.list_view.children[-1]
                )

    # --------------------------------------------------

    def clear(self):

        self.notifications.clear()
        self.list_view.clear_widgets()

    # --------------------------------------------------

    def count(self):

        return len(self.notifications)

    # --------------------------------------------------

    def latest(self):

        if not self.notifications:
            return None

        return self.notifications[-1]

    # --------------------------------------------------

    def all(self):

        return list(self.notifications)

    # --------------------------------------------------

    def remove_last(self):

        if not self.notifications:
            return

        self.notifications.pop()

        if self.list_view.children:
            self.list_view.remove_widget(
                self.list_view.children[0]
            )
