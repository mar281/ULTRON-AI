
from brain import ask_ultron
from memory import save_memory
from voice import speak
from listen import listen
from config import ULTRON_NAME, CREATOR_NAME

def startup():
    message = f"Hello {CREATOR_NAME}. ULTRON is online and listening."
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
        command = listen()

        if not command:
            continue

        if command.lower() in ["exit", "shutdown", "stop"]:
            speak("Goodbye, Creator.")
            break

        answer = ask_ultron(command)

        print(f"\n{ULTRON_NAME}: {answer}")

        speak(answer)
        save_memory(command, answer)

if __name__ == "__main__":
    main()

