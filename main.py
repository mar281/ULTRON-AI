# ==================================
# ULTRON AI - MAIN SYSTEM
# Created by: Emmanuel Cornelius
# ==================================

ULTRON_NAME = "ULTRON"
CREATOR = "Emmanuel Cornelius"
VERSION = "1.0"

def startup():
    print("=" * 40)
    print("       ULTRON AI SYSTEM")
    print("=" * 40)
    print("System: Online")
    print("Creator:", CREATOR)
    print("Version:", VERSION)
    print("Hello, Creator. I am ULTRON.")
    print("Awaiting your instructions...")

def respond(command):
    command = command.lower()

    if "hello" in command:
        return "Greetings, Creator."

    elif "your name" in command:
        return "I am ULTRON, your artificial intelligence."

    elif "your creator" in command:
        return "My creator is Emmanuel Cornelius."

    elif "status" in command:
        return "All systems are ready."

    elif "exit" in command:
        return "ULTRON shutting down."

    else:
        return "I am still learning, Creator."

if __name__ == "__main__":
    startup()

    while True:
        command = input("You: ")

        answer = respond(command)
        print("ULTRON:", answer)

        if "exit" in command.lower():
            break
