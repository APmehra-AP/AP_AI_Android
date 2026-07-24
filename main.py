# Created by : Amarchand Meghwal

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from gui.splash import SplashScreen
from gui.home import HomeScreen
from gui.chat import ChatScreen
from gui.voice import VoiceScreen
from gui.memory import MemoryScreen
from gui.tools import ToolsScreen
from gui.settings import SettingsScreen

Builder.load_file("gui/splash.kv")
Builder.load_file("gui/home.kv")
Builder.load_file("gui/chat.kv")
Builder.load_file("gui/voice.kv")
Builder.load_file("gui/memory.kv")
Builder.load_file("gui/tools.kv")
Builder.load_file("gui/settings.kv")


class APAI(MDApp):
    def build(self):
        self.title = "AP AI"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        sm = ScreenManager()

        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ChatScreen(name="chat"))
        sm.add_widget(VoiceScreen(name="voice"))
        sm.add_widget(MemoryScreen(name="memory"))
        sm.add_widget(ToolsScreen(name="tools"))
        sm.add_widget(SettingsScreen(name="settings"))

        # अभी सीधे Home Screen खोलते हैं
        sm.current = "home"

        return sm


if __name__ == "__main__":
    APAI().run()
