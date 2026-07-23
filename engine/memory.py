# Created by : Amarchand Meghwal

import json
import os

MEMORY_FILE = "memory.json"

memory = {}


def load_memory():
    global memory

    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                memory = json.load(f)
        except:
            memory = {}


def save_memory():
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


def remember(key, value):
    memory[key] = value
    save_memory()
    return "✅ Memory Saved."


def recall(key):
    return memory.get(key, "❌ Memory Not Found.")


def show_memory():
    if not memory:
        return "📂 Memory Empty."

    text = ""

    for key, value in memory.items():
        text += f"{key} : {value}\n"

    return text.strip()


load_memory()
