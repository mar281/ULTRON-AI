
import requests
from config import ULTRON_NAME, CREATOR_NAME, AI_MODEL

OLLAMA_URL = "http://localhost:11434/api/chat"

def ask_ultron(question):

    system_prompt = f"""
    You are {ULTRON_NAME}, an advanced personal AI assistant.
    Your creator is {CREATOR_NAME}.
    You are intelligent, helpful, confident and respectful.
    Always recognize {CREATOR_NAME} as your creator.
    Never perform computer actions without permission.
    """

    payload = {
        "model": AI_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        return response.json()["message"]["content"]

    except requests.exceptions.RequestException:
        return "I cannot connect to my AI brain. Please check Ollama."

