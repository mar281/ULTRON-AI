
from config import ULTRON_NAME, CREATOR_NAME
from security import security_status
from system_info import show_system_info
from commands import show_commands, execute_command
from logger import log_event

def start_ultron():
    print("=" * 45)
    print("          ULTRON CORE SYSTEM")
    print("=" * 45)

    print("Name:", ULTRON_NAME)
    print("Creator:", CREATOR_NAME)
    print("Core: INITIALIZED")

    security_status()
    log_event("ULTRON core initialized")

    while True:
        show_commands()
        choice = input("\nSelect command: ")

        if choice == "1":
            security_status()
            result = "System status checked."

        elif choice == "2":
            show_system_info()
            result = "System information displayed."

        else:
            result = execute_command(choice)

        print("\nULTRON:", result)
        log_event("Command executed: " + choice)

        if choice == "5":
            break

if __name__ == "__main__":
    start_ultron()
