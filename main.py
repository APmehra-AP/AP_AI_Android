# Created by : Amarchand Meghwal

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from gui.home import HomeScreen

Builder.load_file("gui/home.kv")


class APAI(MDApp):
    def build(self):
        self.title = "AP AI"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        sm = ScreenManager()
        sm.add_widget(HomeScreen())
        sm.current = "home"

        return sm


if __name__ == "__main__":
    APAI().run()
