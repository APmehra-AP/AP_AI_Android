# Created by : Amarchand Meghwal

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from engine.commands import execute


class APAI(App):

    def build(self):
        self.title = "AP AI Android"

        root = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10,
        )

        title = Label(
            text="🤖 AP AI Android",
            font_size=28,
            size_hint=(1, 0.1),
        )

        self.chat = Label(
            text="👋 Welcome AP!\n\nAsk me anything.",
            markup=True,
            valign="top",
            halign="left",
            text_size=(350, None),
            size_hint_y=None,
        )
        self.chat.bind(texture_size=self.update_height)

        scroll = ScrollView()
        scroll.add_widget(self.chat)

        bottom = BoxLayout(
            size_hint=(1, 0.12),
            spacing=5,
        )

        self.input = TextInput(
            multiline=False,
            hint_text="Type your message...",
        )

        send = Button(
            text="Send",
            size_hint=(0.25, 1),
        )
        send.bind(on_press=self.send)

        bottom.add_widget(self.input)
        bottom.add_widget(send)

        root.add_widget(title)
        root.add_widget(scroll)
        root.add_widget(bottom)

        return root

    def update_height(self, instance, size):
        instance.height = size[1]

    def send(self, instance):
        text = self.input.text.strip()

        if not text:
            return

        try:
            reply = execute(text)
        except Exception as e:
            reply = str(e)

        self.chat.text += (
            f"\n\n🧑 You: {text}\n🤖 AP AI: {reply}"
        )

        self.input.text = ""


if __name__ == "__main__":
    APAI().run()
