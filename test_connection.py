
import requests

OLLAMA_URL = "http://localhost:11434/api/tags"

def test_connection():
    try:
        response = requests.get(OLLAMA_URL, timeout=5)

        if response.status_code == 200:
            print("ULTRON: Ollama connection successful!")
            print("Available AI models:")
            print(response.json())

        else:
            print("Ollama returned an error.")

    except requests.exceptions.RequestException:
        print("ULTRON: Ollama is not reachable.")

if __name__ == "__main__":
    test_connection()
