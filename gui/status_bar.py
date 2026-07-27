# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable Status Bar
"""

from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout


class StatusBar(MDCard):
    """
    Reusable status bar for AP AI.
    """

    STATUS_READY = "Ready"
    STATUS_ONLINE = "Online"
    STATUS_OFFLINE = "Offline"
    STATUS_LISTENING = "Listening..."
    STATUS_THINKING = "Thinking..."
    STATUS_TYPING = "Typing..."
    STATUS_ERROR = "Error"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.adaptive_height = True
        self.elevation = 1
        self.radius = [12, 12, 12, 12]
        self.padding = "10dp"

        layout = MDBoxLayout(
            orientation="horizontal",
            adaptive_height=True
        )

        self.label = MDLabel(
            text=self.STATUS_READY,
            halign="left",
            adaptive_height=True
        )

        layout.add_widget(self.label)

        self.add_widget(layout)

    # ---------------------------------------------

    def set_status(self, text):
        self.label.text = str(text)

    # ---------------------------------------------

    def ready(self):
        self.set_status(self.STATUS_READY)

    def online(self):
        self.set_status(self.STATUS_ONLINE)

    def offline(self):
        self.set_status(self.STATUS_OFFLINE)

    def listening(self):
        self.set_status(self.STATUS_LISTENING)

    def thinking(self):
        self.set_status(self.STATUS_THINKING)

    def typing(self):
        self.set_status(self.STATUS_TYPING)

    def error(self, message="Error"):
        self.set_status(f"{self.STATUS_ERROR}: {message}")

    # ---------------------------------------------

    def get_status(self):
        return self.label.text

    def is_ready(self):
        return self.label.text == self.STATUS_READY

    def reset(self):
        self.ready()
