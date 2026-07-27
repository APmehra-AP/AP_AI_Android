# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable Chat Widgets
"""

from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp


class ChatBubble(MDCard):

    def __init__(self, text="", sender="assistant", **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = dp(12)
        self.spacing = dp(6)
        self.adaptive_height = True
        self.radius = [18, 18, 18, 18]
        self.size_hint_x = 0.85
        self.ripple_behavior = False
        self.elevation = 1

        if sender == "user":
            self.pos_hint = {"right": 1}
        else:
            self.pos_hint = {"left": 1}

        self.label = MDLabel(
            text=text,
            adaptive_height=True,
            markup=True
        )

        self.add_widget(self.label)

    def set_text(self, text):
        self.label.text = text


class TypingIndicator(MDBoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "horizontal"
        self.adaptive_height = True
        self.spacing = dp(4)

        self.label = MDLabel(
            text="AP AI is typing...",
            adaptive_height=True
        )

        self.add_widget(self.label)

    def show(self):
        self.opacity = 1

    def hide(self):
        self.opacity = 0


class ChatContainer(MDBoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = dp(10)
        self.padding = dp(10)
        self.adaptive_height = True

    def add_user_message(self, text):
        self.add_widget(
            ChatBubble(text=text, sender="user")
        )

    def add_ai_message(self, text):
        self.add_widget(
            ChatBubble(text=text, sender="assistant")
        )

    def clear_chat(self):
        self.clear_widgets()
