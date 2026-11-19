
import json
import os

MEMORY_FILE = "ultron_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return []

def save_memory(user_message, ai_response):
    memory = load_memory()

    memory.append({
        "user": user_message,
        "ultron": ai_response
    })

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4)

def get_memory():
    return load_memory()
