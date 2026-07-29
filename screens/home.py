# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Home Screen
"""

import threading

from kivy.clock import Clock

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView

from gui.components import (
    HeaderBar,
    StatusBar,
    LoadingIndicator,
    ChatBubble,
)

from gui.widgets import (
    APButton,
    APTextField,
)

from engine.ai import ai


class HomeScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = "home"

        root = MDBoxLayout(
            orientation="vertical",
            spacing="12dp",
            padding="12dp",
        )

        # Header
        self.header = HeaderBar("AP AI")
        root.add_widget(self.header)

        # Chat Area
        self.scroll = MDScrollView()

        self.chat_area = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing="8dp",
        )

        self.scroll.add_widget(self.chat_area)
        root.add_widget(self.scroll)

        # Loading
        self.loading = LoadingIndicator()
        self.loading.opacity = 0
        root.add_widget(self.loading)

        # Input
        self.input_box = MDBoxLayout(
            adaptive_height=True,
            spacing="10dp",
        )

        self.message = APTextField(
            hint_text="Type your message..."
        )

        self.send_button = APButton(
            text="Send"
        )

        self.send_button.bind(
            on_release=self.send_message
        )

        self.input_box.add_widget(self.message)
        self.input_box.add_widget(self.send_button)

        root.add_widget(self.input_box)

        # Status
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
        Clock.schedule_once(lambda dt: setattr(self.scroll, "scroll_y", 0), 0)

    def send_message(self, *args):
        text = self.get_message()

        if not text:
            return

        self.add_message(
            ChatBubble(
                message=text,
                sender="user",
            )
        )

        self.clear_input()
        self.show_loading()

        threading.Thread(
            target=self._ask_ai,
            args=(text,),
            daemon=True,
        ).start()

    def _ask_ai(self, text):
        try:
            reply = ai.ask(text)
        except Exception as e:
            reply = f"❌ {e}"

        Clock.schedule_once(
            lambda dt: self._show_reply(reply)
        )

    def _show_reply(self, reply):
        self.hide_loading()

        self.add_message(
            ChatBubble(
                message=reply,
                sender="assistant",
            )
        )
