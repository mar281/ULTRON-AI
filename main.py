

from brain import ask_ultron
from config import ULTRON_NAME, CREATOR_NAME

def startup():
    print("=" * 45)
    print("          ULTRON AI SYSTEM")
    print("=" * 45)
    print("System: Online")
    print("Creator:", CREATOR_NAME)
    print("AI Brain: Connected when Ollama is running")
    print("Welcome, Creator.")

def main():
    startup()

    while True:
        command = input("\nYou: ")

        if command.lower() in ["exit", "quit", "shutdown"]:
            print("ULTRON: Shutting down. Goodbye, Creator.")
            break

        answer = ask_ultron(command)
        print(f"\n{ULTRON_NAME}: {answer}")

if __name__ == "__main__":
    main()
