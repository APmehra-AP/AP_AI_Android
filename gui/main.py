# Created by : Amarchand Meghwal

import flet as ft

from engine.commands import execute


def main(page: ft.Page):
    page.title = "AP AI Android"
    page.theme_mode = ft.ThemeMode.DARK

    try:
        page.window.width = 420
        page.window.height = 800
    except Exception:
        pass

    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    title = ft.Text(
        "🤖 AP AI Android",
        size=28,
        weight=ft.FontWeight.BOLD,
    )

    subtitle = ft.Text(
        "Your Personal AI Assistant",
        size=16,
    )

    output = ft.Text(
        "👋 Welcome AP!\n\nAsk me anything.",
        selectable=True,
    )

    message = ft.TextField(
        label="Type your message...",
        hint_text="Example: help",
        expand=True,
        autofocus=True,
    )

    def send(e=None):
        text = message.value.strip()

        if not text:
            return

        output.value += f"\n\n🧑 You : {text}"

        try:
            reply = execute(text)
        except Exception as ex:
            reply = f"❌ Error:\n{ex}"

        output.value += f"\n🤖 AP AI : {reply}"

        message.value = ""

        page.update()

    message.on_submit = send

    send_button = ft.ElevatedButton(
        "Send",
        on_click=send,
    )

    page.add(
        title,
        subtitle,
        ft.Divider(),
        output,
        ft.Row(
            [
                message,
                send_button,
            ]
        ),
    )


if __name__ == "__main__":
    ft.app(target=main)
