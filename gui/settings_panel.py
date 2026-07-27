# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable Settings Panel
"""

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import (
    MDList,
    MDListItem,
    MDListItemHeadlineText,
)
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.scrollview import MDScrollView


class SettingsPanel(MDScrollView):
    """
    Reusable Settings Panel
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.settings = {}

        self.list_view = MDList()

        self.add_widget(self.list_view)

    # --------------------------------------------------

    def add_switch(
        self,
        title,
        active=False,
        callback=None
    ):

        item = MDListItem()

        item.add_widget(
            MDListItemHeadlineText(
                text=title
            )
        )

        switch = MDSwitch(
            active=active
        )

        if callable(callback):
            switch.bind(active=callback)

        item.add_widget(switch)

        self.list_view.add_widget(item)

        self.settings[title] = switch

        return switch

    # --------------------------------------------------

    def get(self, title):

        widget = self.settings.get(title)

        if widget:
            return widget.active

        return None

    # --------------------------------------------------

    def set(self, title, value):

        widget = self.settings.get(title)

        if widget:
            widget.active = bool(value)

    # --------------------------------------------------

    def toggle(self, title):

        widget = self.settings.get(title)

        if widget:
            widget.active = not widget.active

    # --------------------------------------------------

    def clear(self):

        self.list_view.clear_widgets()
        self.settings.clear()

    # --------------------------------------------------

    def count(self):

        return len(self.settings)

    # --------------------------------------------------

    def titles(self):

        return list(self.settings.keys())
