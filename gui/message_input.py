# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable Message Input
"""

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton

from gui.voice_button import VoiceButton


class MessageInput(MDBoxLayout):
    """
    Chat message input widget.
    """

    def __init__(
        self,
        send_callback=None,
        voice_callback=None,
        hint="Type a message...",
        **kwargs
    ):
        super().__init__(**kwargs)

        self.orientation = "horizontal"
        self.adaptive_height = True
        self.spacing = "8dp"

        self.send_callback = send_callback

        self.text_field = MDTextField(
            hint_text=hint,
            mode="outlined"
        )

        self.text_field.bind(
            on_text_validate=self.send_message
        )

        self.voice_button = VoiceButton(
            callback=voice_callback
        )

        self.send_button = MDIconButton(
            icon="send"
        )

        self.send_button.bind(
            on_release=self.send_message
        )

        self.add_widget(self.text_field)
        self.add_widget(self.voice_button)
        self.add_widget(self.send_button)

    # ------------------------------------------

    def send_message(self, *args):

        text = self.get_text()

        if not text:
            return

        if callable(self.send_callback):
            self.send_callback(text)

        self.clear()

    # ------------------------------------------

    def get_text(self):
        return self.text_field.text.strip()

    # ------------------------------------------

    def set_text(self, text):
        self.text_field.text = str(text)

    # ------------------------------------------

    def clear(self):
        self.text_field.text = ""

    # ------------------------------------------

    def focus(self):
        self.text_field.focus = True

    # ------------------------------------------

    def disable(self):
        self.text_field.disabled = True
        self.send_button.disabled = True
        self.voice_button.disabled = True

    # ------------------------------------------

    def enable(self):
        self.text_field.disabled = False
        self.send_button.disabled = False
        self.voice_button.disabled = False

    # ------------------------------------------

    def set_hint(self, hint):
        self.text_field.hint_text = hint
