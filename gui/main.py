# Created by : Amarchand Meghwal

import flet as ft


def main(page: ft.Page):

    page.title = "AP AI Android"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 420
    page.window.height = 800
    page.padding = 20

    title = ft.Text(
        "🤖 AP AI Android",
        size=28,
        weight=ft.FontWeight.BOLD,
    )

    subtitle = ft.Text(
        "Your Personal AI Assistant",
        size=16,
    )

    chat = ft.Text(
        "👋 Welcome AP!\n\nGUI successfully started.",
        selectable=True,
    )

    message = ft.TextField(
        label="Type your message",
        expand=True,
    )

    def send(e):

        if not message.value:
            return

        chat.value += (
            "\n\n🧑 You : "
            + message.value
        )

        chat.value += (
            "\n🤖 AP AI : "
            + "GUI connected successfully."
        )

        message.value = ""

        page.update()

    send_button = ft.ElevatedButton(
        "Send",
        on_click=send,
    )

    page.add(

        title,

        subtitle,

        ft.Divider(),

        chat,

        ft.Row(
            [
                message,
                send_button,
            ]
        ),
    )


ft.app(target=main)
