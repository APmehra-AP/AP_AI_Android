# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
Custom Dialogs
"""

from kivymd.uix.dialog import (
    MDDialog,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
)
from kivymd.uix.button import (
    MDButton,
    MDButtonText,
)


class DialogManager:

    @staticmethod
    def info(title, message):

        dialog = MDDialog()

        dialog.add_widget(
            MDDialogHeadlineText(
                text=title
            )
        )

        dialog.add_widget(
            MDDialogSupportingText(
                text=message
            )
        )

        dialog.add_widget(
            MDDialogButtonContainer(
                MDButton(
                    MDButtonText(text="OK"),
                    on_release=lambda x: dialog.dismiss()
                )
            )
        )

        dialog.open()

        return dialog

    @staticmethod
    def error(message):

        return DialogManager.info(
            "Error",
            message
        )

    @staticmethod
    def success(message):

        return DialogManager.info(
            "Success",
            message
        )

    @staticmethod
    def warning(message):

        return DialogManager.info(
            "Warning",
            message
        )

    @staticmethod
    def confirm(
        title,
        message,
        yes_callback=None,
        no_callback=None
    ):

        dialog = MDDialog()

        dialog.add_widget(
            MDDialogHeadlineText(
                text=title
            )
        )

        dialog.add_widget(
            MDDialogSupportingText(
                text=message
            )
        )

        buttons = MDDialogButtonContainer()

        no_button = MDButton(
            MDButtonText(text="No")
        )

        yes_button = MDButton(
            MDButtonText(text="Yes")
        )

        def no_action(*_):
            dialog.dismiss()

            if callable(no_callback):
                no_callback()

        def yes_action(*_):
            dialog.dismiss()

            if callable(yes_callback):
                yes_callback()

        no_button.bind(
            on_release=no_action
        )

        yes_button.bind(
            on_release=yes_action
        )

        buttons.add_widget(no_button)
        buttons.add_widget(yes_button)

        dialog.add_widget(buttons)

        dialog.open()

        return dialog


dialogs = DialogManager()
