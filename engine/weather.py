# Created by : Amarchand Meghwal

import json
from urllib.request import urlopen
from urllib.parse import quote


def weather(city):

    city = city.strip()

    if not city:
        return "🌤️ Use: weather <city>"

    try:
        url = (
            "https://wttr.in/"
            + quote(city)
            + "?format=j1"
        )

        with urlopen(url, timeout=10) as response:
            data = json.loads(
                response.read().decode("utf-8")
            )

        current = data["current_condition"][0]

        temp = current["temp_C"]
        feels = current["FeelsLikeC"]
        humidity = current["humidity"]
        wind = current["windspeedKmph"]
        desc = current["weatherDesc"][0]["value"]

        return (
            f"🌤️ Weather : {city.title()}\n\n"
            f"🌡️ Temperature : {temp}°C\n"
            f"🤗 Feels Like : {feels}°C\n"
            f"💧 Humidity : {humidity}%\n"
            f"💨 Wind : {wind} km/h\n"
            f"☁️ Condition : {desc}"
        )

    except Exception:
        return (
            "❌ Weather information not available.\n"
            "Check city name or internet connection."
        )
