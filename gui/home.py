# Created by : Amarchand Meghwal

from kivymd.uix.screen import MDScreen


class HomeScreen(MDScreen):

    def goto(self, screen):
        if self.manager:
            self.manager.current = screen

    def open_home(self):
        self.goto("home")

    def open_chat(self):
        self.goto("chat")

    def open_voice(self):
        self.goto("voice")

    def open_memory(self):
        self.goto("memory")

    def open_tools(self):
        self.goto("tools")

    def open_settings(self):
        self.goto("settings")
