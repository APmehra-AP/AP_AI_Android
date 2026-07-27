# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable Chat History
"""

from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout

from gui.chat_widgets import ChatBubble


class ChatHistory(MDScrollView):
    """
    Scrollable chat history widget.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.do_scroll_x = False

        self.container = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing="8dp",
            padding="10dp"
        )

        self.add_widget(self.container)

    # -------------------------------------------------

    def add_user_message(self, text):

        bubble = ChatBubble(
            text=text,
            sender="user"
        )

        self.container.add_widget(bubble)

        self.scroll_to_bottom()

    # -------------------------------------------------

    def add_ai_message(self, text):

        bubble = ChatBubble(
            text=text,
            sender="assistant"
        )

        self.container.add_widget(bubble)

        self.scroll_to_bottom()

    # -------------------------------------------------

    def add_system_message(self, text):

        bubble = ChatBubble(
            text=text,
            sender="assistant"
        )

        self.container.add_widget(bubble)

        self.scroll_to_bottom()

    # -------------------------------------------------

    def clear_history(self):

        self.container.clear_widgets()

    # -------------------------------------------------

    def message_count(self):

        return len(self.container.children)

    # -------------------------------------------------

    def scroll_to_bottom(self):

        self.scroll_y = 0

    # -------------------------------------------------

    def get_messages(self):

        messages = []

        for widget in reversed(self.container.children):
            if hasattr(widget, "label"):
                messages.append(widget.label.text)

        return messages

    # -------------------------------------------------

    def remove_last_message(self):

        if self.container.children:
            self.container.remove_widget(
                self.container.children[0]
            )
