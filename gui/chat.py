# Created by : Amarchand Meghwal

from kivymd.uix.screen import MDScreen


class ChatScreen(MDScreen):

    def go_home(self):
        if self.manager:
            self.manager.current = "home"

    def send_message(self):
        message = self.ids.message_input.text.strip()

        if not message:
            return

        self.ids.chat_label.text += f"\n👤 You: {message}\n"

        self.ids.message_input.text = ""
