# Created by : Amarchand Meghwal

search_data = {
    "python": (
        "🐍 Python ek high-level programming language hai. "
        "Ye AI, automation, web development aur data science me bahut use hoti hai."
    ),

    "ai": (
        "🤖 AI (Artificial Intelligence) computers ko sochne, "
        "seekhne aur decision lene ki capability dene ki technology hai."
    ),

    "android": (
        "📱 Android Google ka mobile operating system hai."
    ),

    "termux": (
        "💻 Termux Android par Linux terminal environment provide karta hai."
    ),

    "ap ai": (
        "🚀 AP AI ek personal AI assistant project hai jo AP bana rahe hain."
    ),
}


def search(query):

    query = query.strip()

    if not query:
        return "⚠️ Search keyword required."

    lower = query.lower()

    # search list
    if lower == "list":

        result = "📚 Available Topics\n\n"

        for topic in sorted(search_data.keys()):
            result += f"• {topic}\n"

        return result.strip()

    # search add topic = information
    if lower.startswith("add "):

        text = query[4:].strip()

        if "=" not in text:
            return "❌ Use : search add topic = information"

        topic, info = text.split("=", 1)

        topic = topic.strip().lower()
        info = info.strip()

        if not topic or not info:
            return "❌ Invalid format."

        search_data[topic] = info

        return f"✅ '{topic}' added successfully."

    # Normal search
    if lower in search_data:
        return search_data[lower]

    return (
        f"❌ '{query}' ke baare me information available nahi hai.\n"
        "💡 Type 'search list' to see available topics."
    )
