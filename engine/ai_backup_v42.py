# Created by : Amarchand Meghwal

import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from engine.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_MODEL,
)

from engine.memory import memory
from engine.history import history_list


class AIEngine:

    def __init__(self):
        self.url = "https://openrouter.ai/api/v1/chat/completions"

    def ask(self, prompt):

        prompt = prompt.strip()

        if not prompt:
            return "🤖 Please ask something."

        if (
            not OPENROUTER_API_KEY
            or OPENROUTER_API_KEY == "YOUR_API_KEY"
        ):
            return (
                "❌ OpenRouter API Key not configured.\n"
                "Please edit engine/config.py"
            )

        memory_text = "\n".join(
            f"{k}: {v}"
            for k, v in memory.items()
        )

        history_text = "\n".join(
            history_list[-10:]
        )

        context = f"""User Memory:
{memory_text}

Recent History:
{history_text}

Current User Message:
{prompt}
"""

        body = {
            "model": OPENROUTER_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are AP AI created by Amarchand Meghwal. "
                        "Always reply in the same language as the user. "
                        "If the user writes in Hindi, reply in Hindi. "
                        "Use memory and recent history whenever useful. "
                        "Be accurate, concise and helpful."
                    ),
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

            with urlopen(req, timeout=30) as response:

                data = json.loads(
                    response.read().decode("utf-8")
                )

            if "choices" not in data:
                return "❌ Invalid response received from AI."

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

            return message

        except HTTPError as e:

            try:
                error = e.read().decode("utf-8")
                return f"HTTP Error {e.code}\n{error}"

            except Exception:
                return f"HTTP Error {e.code}"

        except URLError:
            return (
                "🌐 Internet connection failed.\n"
                "Please check your network."
            )

        except json.JSONDecodeError:
            return "❌ Invalid JSON response."

        except Exception as e:
            return f"❌ AI Error:\n{e}"


ai = AIEngine()
