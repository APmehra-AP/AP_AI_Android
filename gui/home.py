# Created by : Amarchand Meghwal

from kivymd.uix.screen import MDScreen


class HomeScreen(MDScreen):

    def open_chat(self):
        self.manager.current = "chat"

    def open_voice(self):
        self.manager.current = "voice"

    def open_memory(self):
        self.manager.current = "memory"

    def open_tools(self):
        self.manager.current = "tools"

    def open_settings(self):
        self.manager.current = "settings"

    def open_home(self):
        self.manager.current = "home"
