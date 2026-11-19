
from datetime import datetime

def show_commands():
    print("\n====== ULTRON COMMAND CENTER ======")
    print("1. Check system status")
    print("2. Show current time")
    print("3. Show creator")
    print("4. Show ULTRON identity")
    print("5. Exit")
    print("===================================")

def execute_command(choice):
    if choice == "1":
        return "ULTRON systems are prepared."

    elif choice == "2":
        return "Current time: " + datetime.now().strftime("%H:%M:%S")

    elif choice == "3":
        return "My creator is Emmanuel Cornelius."

    elif choice == "4":
        return "I am ULTRON, your personal AI assistant."

    elif choice == "5":
        return "Shutting down."

    return "Unknown command."
