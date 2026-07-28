# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Home Screen
"""

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

from gui.components import (
    HeaderBar,
    StatusBar,
    LoadingIndicator,
)

from gui.widgets import (
    APButton,
    APTextField,
)


class HomeScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = "home"

        root = MDBoxLayout(
            orientation="vertical",
            spacing="12dp",
            padding="12dp"
        )

        # Header
        self.header = HeaderBar("AP AI")
        root.add_widget(self.header)

        # Chat Area
        self.chat_area = MDBoxLayout(
            orientation="vertical"
        )
        root.add_widget(self.chat_area)

        return

        # Loading Indicator
        self.loading = LoadingIndicator()
        self.loading.opacity = 0
        root.add_widget(self.loading)

        # Input Area
        self.input_box = MDBoxLayout(
            adaptive_height=True,
            spacing="10dp"
        )

        self.message = APTextField(
            hint_text="Type your message..."
        )

        self.send_button = APButton(
            text="Send"
        )

        self.input_box.add_widget(self.message)
        self.input_box.add_widget(self.send_button)

        root.add_widget(self.input_box)


        # Status Bar
        self.status = StatusBar()
        root.add_widget(self.status)

        self.add_widget(root)

    def show_loading(self):
        self.loading.opacity = 1
        self.status.set_status("Thinking...")

    def hide_loading(self):
        self.loading.opacity = 0
        self.status.set_status("Ready")

    def clear_input(self):
        self.message.text = ""

    def get_message(self):
        return self.message.text.strip()

    def add_message(self, widget):
        self.chat_area.add_widget(widget)
