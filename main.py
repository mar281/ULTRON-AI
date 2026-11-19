
from brain import ask_ultron
from memory import save_memory
from voice import speak
from config import ULTRON_NAME, CREATOR_NAME

def startup():
    message = f"Hello Emmanuel Cornelius. I am {ULTRON_NAME}. Your system is ready."
    print("=" * 45)
    print("          ULTRON AI SYSTEM")
    print("=" * 45)
    print("Creator:", CREATOR_NAME)
    print("AI Brain: Ready")
    print("Memory: Enabled")
    print("Voice: Enabled")
    speak(message)

def main():
    startup()

    while True:
        command = input("\nYou: ")

        if command.lower() in ["exit", "quit", "shutdown"]:
            message = "Goodbye, Creator. ULTRON shutting down."
            print("ULTRON:", message)
            speak(message)
            break

        answer = ask_ultron(command)

        print(f"\n{ULTRON_NAME}: {answer}")

        speak(answer)
        save_memory(command, answer)

if __name__ == "__main__":
    main()
