# Created by : Amarchand Meghwal

import json
import ssl
import certifi

from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from engine.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_MODEL,
)


def internet_search(query):

    query = query.strip()

    if not query:
        return "🌐 Search query required."

    if (
        not OPENROUTER_API_KEY
        or OPENROUTER_API_KEY == "YOUR_API_KEY"
    ):
        return "❌ OpenRouter API Key not configured."

    url = "https://openrouter.ai/api/v1/chat/completions"

    body = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are AP AI Search Engine. "
                    "Answer the user's search query briefly, accurately and clearly. "
                    "Reply in the same language as the user."
                ),
            },
            {
                "role": "user",
                "content": f"Search: {query}",
            },
        ],
    }

    try:

        req = Request(
            url,
            data=json.dumps(body).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
        )

        context_ssl = ssl.create_default_context(
            cafile=certifi.where()
        )

        with urlopen(
            req,
            timeout=30,
            context=context_ssl,
        ) as response:

            data = json.loads(
                response.read().decode("utf-8")
            )

        if "choices" not in data:
            return "❌ Invalid response from server."

        choices = data.get("choices", [])

        if not choices:
            return "❌ No result found."

        message = (
            choices[0]
            .get("message", {})
            .get("content", "")
            .strip()
        )

        if not message:
            return "❌ Empty response."

        return "🌐 Internet Search\n\n" + message

    except HTTPError as e:
        try:
            return e.read().decode("utf-8")
        except Exception:
            return f"HTTP Error {e.code}"

    except URLError as e:
        return f"🌐 Network Error:\n{e}"

    except Exception as e:
        return f"❌ Internet Error:\n{e}"
