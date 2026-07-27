# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Chat Screen
"""

from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView

from gui.components import (
    HeaderBar,
    ChatBubble,
    StatusBar,
)

from gui.widgets import (
    APButton,
    APTextField,
)


class ChatScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = "chat"

        root = MDBoxLayout(
            orientation="vertical",
            spacing="10dp",
            padding="10dp"
        )

        # Header
        self.header = HeaderBar("Chat")
        root.add_widget(self.header)

        # Scroll Area
        self.scroll = MDScrollView()

        self.messages = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing="8dp"
        )

        self.scroll.add_widget(self.messages)

        root.add_widget(self.scroll)

        # Input Area
        self.input_bar = MDBoxLayout(
            adaptive_height=True,
            spacing="8dp"
        )

        self.input = APTextField(
            hint_text="Ask anything..."
        )

        self.send = APButton(
            text="Send"
        )

        self.input_bar.add_widget(self.input)
        self.input_bar.add_widget(self.send)

        root.add_widget(self.input_bar)

        # Status
        self.status = StatusBar()

        root.add_widget(self.status)

        self.add_widget(root)

    # --------------------------------------------------

    def add_user_message(self, text):

        bubble = ChatBubble(
            message=text,
            sender="user"
        )

        self.messages.add_widget(bubble)

    # --------------------------------------------------

    def add_ai_message(self, text):

        bubble = ChatBubble(
            message=text,
            sender="assistant"
        )

        self.messages.add_widget(bubble)

    # --------------------------------------------------

    def clear_chat(self):

        self.messages.clear_widgets()

    # --------------------------------------------------

    def get_message(self):

        return self.input.text.strip()

    # --------------------------------------------------

    def clear_input(self):

        self.input.text = ""

    # --------------------------------------------------

    def set_status(self, text):

        self.status.set_status(text)
