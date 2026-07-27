# Created by : Amarchand Meghwal

from threading import Thread

from kivy.clock import Clock
from kivymd.uix.screen import MDScreen

from engine.ai import ai


class ChatScreen(MDScreen):

    def on_kv_post(self, base_widget):
        self.chat_text = "AP AI\n\nWelcome!\n"
        self.refresh_chat()

    def go_home(self):
        if self.manager:
            self.manager.current = "home"

    def refresh_chat(self):
        if "chat_label" in self.ids:
            self.ids.chat_label.text = self.chat_text

    def send_message(self):
        text = self.ids.message_input.text.strip()

        if not text:
            return

        self.chat_text += f"\nYou: {text}\n"
        self.chat_text += "\nAP AI: Thinking...\n"

        self.refresh_chat()
        self.ids.message_input.text = ""

        Thread(
            target=self.ask_ai,
            args=(text,),
            daemon=True,
        ).start()

    def ask_ai(self, prompt):
        try:
            reply = ai.ask(prompt)
        except Exception as e:
            reply = f"Error: {e}"

        Clock.schedule_once(
            lambda dt: self.show_ai_reply(reply)
        )

    def show_ai_reply(self, reply):
        thinking = "\nAP AI: Thinking...\n"

        if thinking in self.chat_text:
            self.chat_text = self.chat_text.replace(
                thinking,
                f"\nAP AI: {reply}\n",
                1,
            )
        else:
            self.chat_text += f"\nAP AI: {reply}\n"

        self.refresh_chat()

        if "chat_scroll" in self.ids:
            Clock.schedule_once(
                lambda dt: setattr(
                    self.ids.chat_scroll,
                    "scroll_y",
                    0,
                ),
                0.1,
            )
