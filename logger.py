
from datetime import datetime

LOG_FILE = "ultron_activity.log"

def log_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {event}\n")

def show_logs():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            print(file.read())

    except FileNotFoundError:
        print("No activity recorded yet.")
