# Created by : Amarchand Meghwal

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from kivymd.app import MDApp

from gui.splash import SplashScreen
from gui.home import HomeScreen
from gui.chat import ChatScreen
from gui.voice import VoiceScreen
from gui.tools import ToolsScreen
from gui.memory import MemoryScreen
from gui.settings import SettingsScreen


Builder.load_file("gui/splash.kv")
Builder.load_file("gui/home.kv")
Builder.load_file("gui/chat.kv")
Builder.load_file("gui/voice.kv")
Builder.load_file("gui/tools.kv")
Builder.load_file("gui/memory.kv")
Builder.load_file("gui/settings.kv")


class APAI(MDApp):

    def build(self):
        self.title = "AP AI"

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        sm = ScreenManager()

        sm.add_widget(SplashScreen())
        sm.add_widget(HomeScreen())
        sm.add_widget(ChatScreen())
        sm.add_widget(VoiceScreen())
        sm.add_widget(ToolsScreen())
        sm.add_widget(MemoryScreen())
        sm.add_widget(SettingsScreen())

        sm.current = "splash"

        return sm


if __name__ == "__main__":
    APAI().run()
