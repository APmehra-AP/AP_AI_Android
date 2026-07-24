# Created by : Amarchand Meghwal

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

Builder.load_file("gui/splash.kv")
Builder.load_file("gui/home.kv")
Builder.load_file("gui/chat.kv")
Builder.load_file("gui/voice.kv")
Builder.load_file("gui/tools.kv")
Builder.load_file("gui/memory.kv")
Builder.load_file("gui/settings.kv")


class Manager(ScreenManager):
    pass


class APAI(MDApp):

    def build(self):
        self.title = "AP AI"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        return Manager()


if __name__ == "__main__":
    APAI().run()
