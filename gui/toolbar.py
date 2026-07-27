# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Reusable Top Toolbar
"""

from kivymd.uix.appbar import (
    MDTopAppBar,
    MDTopAppBarLeadingButtonContainer,
    MDTopAppBarTrailingButtonContainer,
)
from kivymd.uix.button import MDActionTopAppBarButton


class APToolbar(MDTopAppBar):
    """
    Reusable AP AI Toolbar
    """

    def __init__(
        self,
        title="AP AI",
        left_callback=None,
        right_actions=None,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.title = title

        # -------------------------
        # Leading Buttons
        # -------------------------

        leading = MDTopAppBarLeadingButtonContainer()

        menu_button = MDActionTopAppBarButton(
            icon="menu"
        )

        if callable(left_callback):
            menu_button.bind(
                on_release=lambda *_: left_callback()
            )

        leading.add_widget(menu_button)
        self.add_widget(leading)

        # -------------------------
        # Trailing Buttons
        # -------------------------

        trailing = MDTopAppBarTrailingButtonContainer()

        if right_actions:
            for icon_name, callback in right_actions:

                button = MDActionTopAppBarButton(
                    icon=icon_name
                )

                if callable(callback):
                    button.bind(
                        on_release=lambda _, cb=callback: cb()
                    )

                trailing.add_widget(button)

        self.add_widget(trailing)

    # --------------------------------

    def set_title(self, title):
        self.title = title

    # --------------------------------

    def add_action(self, icon, callback=None):

        container = None

        for widget in self.children:
            if isinstance(
                widget,
                MDTopAppBarTrailingButtonContainer
            ):
                container = widget
                break

        if container is None:
            return

        button = MDActionTopAppBarButton(
            icon=icon
        )

        if callable(callback):
            button.bind(
                on_release=lambda *_: callback()
            )

        container.add_widget(button)

    # --------------------------------

    def clear_actions(self):

        for widget in self.children:
            if isinstance(
                widget,
                MDTopAppBarTrailingButtonContainer
            ):
                widget.clear_widgets()
