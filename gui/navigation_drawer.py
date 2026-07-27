# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Navigation Drawer
"""

from kivymd.uix.navigationdrawer import (
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerItem,
)
from kivymd.uix.label import MDLabel


class APNavigationDrawer(MDNavigationDrawer):

    def __init__(self, navigation=None, **kwargs):
        super().__init__(**kwargs)

        self.navigation = navigation

        menu = MDNavigationDrawerMenu()

        menu.add_widget(
            MDLabel(
                text="AP AI",
                bold=True,
                halign="center",
                adaptive_height=True
            )
        )

        self._add_item(
            menu,
            "Home",
            "home"
        )

        self._add_item(
            menu,
            "Chat",
            "chat"
        )

        self._add_item(
            menu,
            "Profile",
            "profile"
        )

        self._add_item(
            menu,
            "Settings",
            "settings"
        )

        self._add_item(
            menu,
            "About",
            "about"
        )

        self.add_widget(menu)

    def _add_item(self, menu, text, screen):

        item = MDNavigationDrawerItem(
            text=text
        )

        item.bind(
            on_release=lambda *_: self.open_screen(screen)
        )

        menu.add_widget(item)

    def open_screen(self, screen):

        self.set_state("close")

        if (
            self.navigation
            and self.navigation.has_screen(screen)
        ):
            self.navigation.go(screen)
