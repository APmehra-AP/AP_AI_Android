# Created by : Amarchand Meghwal

from kivymd.uix.screen import MDScreen


class ChatScreen(MDScreen):

    def go_home(self):
        if self.manager:
            self.manager.current = "home"
