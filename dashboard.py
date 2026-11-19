
import tkinter as tk
from tkinter import scrolledtext
import threading

from brain import ask_ultron
from memory import save_memory, get_recent_memory
from config import ULTRON_NAME, CREATOR_NAME

BG = "#080d1a"
PANEL = "#111a2e"
CYAN = "#00d9ff"
WHITE = "#eaf6ff"
GREEN = "#00e676"


class UltronDashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("ULTRON AI - Control Dashboard")
        self.root.geometry("900x650")
        self.root.configure(bg=BG)

        header = tk.Frame(root, bg=BG)
        header.pack(fill="x", padx=20, pady=15)

        tk.Label(
            header,
            text="ULTRON",
            font=("Arial", 28, "bold"),
            fg=CYAN,
            bg=BG
        ).pack(side="left")

        tk.Label(
            header,
            text="AI CONTROL DASHBOARD",
            font=("Arial", 10),
            fg=WHITE,
            bg=BG
        ).pack(side="left", padx=15, pady=12)

        self.status = tk.Label(
            root,
            text="● READY",
            fg=GREEN,
            bg=BG,
            font=("Arial", 10, "bold")
        )
        self.status.pack(anchor="w", padx=25)

        self.chat = scrolledtext.ScrolledText(
            root,
            bg=PANEL,
            fg=WHITE,
            insertbackground=WHITE,
            font=("Arial", 11),
            wrap=tk.WORD,
            state="disabled"
        )
        self.chat.pack(fill="both", expand=True, padx=20, pady=15)

        self.show_message(
            "ULTRON",
            f"Hello {CREATOR_NAME}. Your dashboard is online."
        )

        bottom = tk.Frame(root, bg=BG)
        bottom.pack(fill="x", padx=20, pady=15)

        self.entry = tk.Entry(
            bottom,
            bg=PANEL,
            fg=WHITE,
            insertbackground=WHITE,
            font=("Arial", 12)
        )
        self.entry.pack(side="left", fill="x", expand=True, ipady=10)
        self.entry.bind("<Return>", lambda event: self.send_message())

        self.send_button = tk.Button(
            bottom,
            text="SEND",
            bg=CYAN,
            fg=BG,
            font=("Arial", 10, "bold"),
            command=self.send_message
        )
        self.send_button.pack(side="left", padx=8)

        tk.Label(
            root,
            text=f"CREATOR: {CREATOR_NAME}",
            fg=CYAN,
            bg=BG,
            font=("Arial", 9)
        ).pack(pady=8)

    def show_message(self, speaker, message):
        self.chat.configure(state="normal")
        self.chat.insert(tk.END, f"\n{speaker}: {message}\n")
        self.chat.configure(state="disabled")
        self.chat.see(tk.END)

    def send_message(self):
        question = self.entry.get().strip()

        if not question:
            return

        self.entry.delete(0, tk.END)
        self.show_message("YOU", question)

        self.status.config(text="● THINKING...", fg=CYAN)
        self.send_button.config(state="disabled")

        threading.Thread(
            target=self.get_answer,
            args=(question,),
            daemon=True
        ).start()

    def get_answer(self, question):
        answer = ask_ultron(question)

        save_memory(question, answer)

        self.root.after(
            0,
            lambda: self.finish_answer(answer)
        )

    def finish_answer(self, answer):
        self.show_message(ULTRON_NAME, answer)
        self.status.config(text="● READY", fg=GREEN)
        self.send_button.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = UltronDashboard(root)
    root.mainloop()
