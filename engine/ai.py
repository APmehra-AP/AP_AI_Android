# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

import json
import ssl
import certifi

from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from engine.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_MODEL,
    OPENROUTER_BASE_URL,
    REQUEST_TIMEOUT,
    SYSTEM_PROMPT,
)

from engine.memory import memory
from engine.history import history


class AIEngine:

    def __init__(self):
        self.url = OPENROUTER_BASE_URL

    def ask(self, prompt):

        prompt = str(prompt).strip()

        if not prompt:
            return "🤖 Please ask something."

        if not OPENROUTER_API_KEY:
            return (
                "❌ OpenRouter API Key not configured.\n"
                "Please edit engine/config.py"
            )

        memory_text = json.dumps(
            memory.all(),
            ensure_ascii=False,
            indent=2,
        )

        history_text = history.export_text()

        context = f"""
User Memory:
{memory_text}

Conversation History:
{history_text}

Current User Message:
{prompt}
"""

        body = {
            "model": OPENROUTER_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": context,
                },
            ],
        }

        try:
            req = Request(
                self.url,
                data=json.dumps(body).encode("utf-8"),
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json",
                },
            )

            ssl_context = ssl.create_default_context(
                cafile=certifi.where()
            )

            with urlopen(
                req,
                timeout=REQUEST_TIMEOUT,
                context=ssl_context,
            ) as response:

                data = json.loads(
                    response.read().decode("utf-8")
                )

            choices = data.get("choices", [])

            if not choices:
                return "❌ Empty response from AI."

            message = (
                choices[0]
                .get("message", {})
                .get("content", "")
                .strip()
            )

            if not message:
                return "❌ AI returned an empty reply."

            history.add("user", prompt)
            history.add("assistant", message)

            return message

        except HTTPError as e:
            try:
                error = e.read().decode("utf-8")
                return f"HTTP Error {e.code}\n{error}"
            except Exception:
                return f"HTTP Error {e.code}"

        except URLError as e:
            return f"🌐 Network Error:\n{e}"

        except json.JSONDecodeError:
            return "❌ Invalid JSON response."

        except Exception as e:
            return f"❌ AI Error:\n{e}"


ai = AIEngine()
