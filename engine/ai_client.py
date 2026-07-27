# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
OpenRouter AI Client
"""

import requests

from engine.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_BASE_URL,
    DEFAULT_MODEL,
    SYSTEM_PROMPT,
    REQUEST_TIMEOUT
)


class AIClient:
    def __init__(self):
        self.api_key = OPENROUTER_API_KEY
        self.model = DEFAULT_MODEL
        self.base_url = OPENROUTER_BASE_URL

    def set_api_key(self, api_key):
        self.api_key = api_key

    def set_model(self, model):
        self.model = model

    def available(self):
        return bool(self.api_key.strip())

    def ask(self, prompt, history=None):
        """
        Send a chat request.
        """

        if not self.available():
            return {
                "success": False,
                "message": "OpenRouter API key not configured."
            }

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        if history:
            for item in history:
                messages.append({
                    "role": item.get("role", "user"),
                    "content": item.get("message", "")
                })

        messages.append({
            "role": "user",
            "content": prompt
        })

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": messages
        }

        try:
            response = requests.post(
                self.base_url,
                headers=headers,
                json=payload,
                timeout=REQUEST_TIMEOUT
            )

            response.raise_for_status()

            data = response.json()

            text = (
                data["choices"][0]["message"]["content"]
                .strip()
            )

            return {
                "success": True,
                "message": text,
                "raw": data
            }

        except Exception as error:
            return {
                "success": False,
                "message": str(error)
            }


ai_client = AIClient()
