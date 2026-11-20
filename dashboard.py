
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import time
import math
import psutil
import requests
import subprocess
import sys
import os

from brain import ask_ultron
from memory import save_memory
from voice import speak
from listen import listen
from config import ULTRON_NAME, CREATOR_NAME
from commands import get_command_action, execute_action

BG = "#080000"
PANEL = "#190707"
RED = "#ff2020"
WHITE = "#ffffff"
MUTED = "#a66b6b"


class UltronDashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("ULTRON AI - RED EDITION")
        self.root.geometry("1100x700")
        self.root.minsize(900, 650)
        self.root.configure(bg=BG)

        self.animation_angle = 0
        self.start_time = time.monotonic()

        self.build_header()
        self.build_main()
        self.build_chat()

        self.update_clock()
        self.animate_core()
        self.start_monitor()

        self.show_message(
            "ULTRON",
            f"Welcome back, {CREATOR_NAME}. ULTRON is online."
        )

    def build_header(self):
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", padx=20, pady=8)

        tk.Label(
            header,
            text="ULTRON",
            font=("Arial", 27, "bold"),
            fg=RED,
            bg=BG
        ).pack(side="left")

        self.clock_label = tk.Label(
            header,
            text="",
            font=("Arial", 11),
            fg=WHITE,
            bg=BG
        )
        self.clock_label.pack(side="right")

        tk.Label(
            self.root,
            text="ARTIFICIAL INTELLIGENCE COMMAND SYSTEM",
            font=("Arial", 10, "bold"),
            fg=MUTED,
            bg=BG
        ).pack()

    def build_main(self):
        main = tk.Frame(self.root, bg=BG)
        main.pack(fill="x", padx=20, pady=5)

        self.core = tk.Canvas(
            main,
            width=300,
            height=200,
            bg=BG,
            highlightthickness=0
        )
        self.core.pack(side="left", padx=20)

        panel = tk.Frame(
            main,
            bg=PANEL,
            highlightbackground=RED,
            highlightthickness=1
        )
        panel.pack(side="right", fill="both", expand=True, padx=15)

        tk.Label(
            panel,
            text="SYSTEM STATUS",
            font=("Arial", 15, "bold"),
            fg=RED,
            bg=PANEL
        ).pack(pady=6)

        self.status_label = tk.Label(
            panel,
            text="ULTRON: ONLINE",
            fg=WHITE,
            bg=PANEL,
            font=("Arial", 11)
        )
        self.status_label.pack(pady=3)

        tk.Label(
            panel,
            text=f"CREATOR: {CREATOR_NAME}",
            fg=WHITE,
            bg=PANEL
        ).pack(pady=3)

        tk.Label(
            panel,
            text="AI ENGINE: OLLAMA / LLAMA 3",
            fg=WHITE,
            bg=PANEL
        ).pack(pady=3)

        tk.Label(
            panel,
            text="VOICE: ENABLED",
            fg=WHITE,
            bg=PANEL
        ).pack(pady=3)

        tk.Label(
            panel,
            text="MEMORY: ENABLED",
            fg=WHITE,
            bg=PANEL
        ).pack(pady=3)

        self.monitor_label = tk.Label(
            panel,
            text="CPU: --   RAM: --",
            fg=RED,
            bg=PANEL,
            font=("Arial", 10, "bold")
        )
        self.monitor_label.pack(pady=5)

        self.ollama_label = tk.Label(
            panel,
            text="AI CONNECTION: CHECKING",
            fg=MUTED,
            bg=PANEL
        )
        self.ollama_label.pack(pady=3)

    def animate_core(self):
        self.core.delete("all")

        cx = 150
        cy = 100

        for radius in [30, 50, 70, 90]:
            self.core.create_oval(
                cx - radius,
                cy - radius,
                cx + radius,
                cy + radius,
                outline=RED,
                width=2
            )

        for i in range(8):
            angle = math.radians(
                self.animation_angle + i * 45
            )

            x = cx + 80 * math.cos(angle)
            y = cy + 80 * math.sin(angle)

            self.core.create_oval(
                x - 5, y - 5,
                x + 5, y + 5,
                fill=RED,
                outline=WHITE
            )

        self.core.create_text(
            cx,
            cy,
            text="ULTRON",
            fill=WHITE,
            font=("Arial", 18, "bold")
        )

        self.animation_angle += 3
        self.root.after(50, self.animate_core)

    def build_chat(self):
        chat = tk.Frame(
            self.root,
            bg=PANEL,
            highlightbackground=RED,
            highlightthickness=2,
            height=240
        )

        chat.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=5
        )

        chat.pack_propagate(False)

        tk.Label(
            chat,
            text="ULTRON COMMUNICATION TERMINAL",
            font=("Arial", 15, "bold"),
            fg=RED,
            bg=PANEL
        ).pack(pady=5)

        tk.Button(
            chat,
            text="OPEN COMMAND CENTER",
            command=self.open_command_center,
            bg="#990000",
            fg=WHITE,
            activebackground=RED,
            font=("Arial", 10, "bold"),
            relief="flat"
        ).pack(pady=3)

        self.chat_display = scrolledtext.ScrolledText(
            chat,
            wrap=tk.WORD,
            font=("Arial", 11),
            bg="#050000",
            fg=WHITE,
            insertbackground=WHITE,
            height=4,
            relief="flat"
        )

        self.chat_display.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=5
        )

        self.chat_display.config(state="disabled")

        input_frame = tk.Frame(chat, bg=PANEL)
        input_frame.pack(
            fill="x",
            padx=10,
            pady=8,
            side="bottom"
        )

        self.message_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            bg="#300000",
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat"
        )

        self.message_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=10,
            padx=5
        )

        self.message_entry.bind(
            "<Return>",
            lambda event: self.send_message()
        )

        self.send_button = tk.Button(
            input_frame,
            text="SEND",
            command=self.send_message,
            bg=RED,
            fg=WHITE,
            font=("Arial", 11, "bold"),
            relief="flat",
            width=10
        )
        self.send_button.pack(side="left", padx=5)

        self.mic_button = tk.Button(
            input_frame,
            text="MIC",
            command=self.start_listening,
            bg="#990000",
            fg=WHITE,
            font=("Arial", 11, "bold"),
            relief="flat",
            width=8
        )
        self.mic_button.pack(side="left", padx=5)

    def show_message(self, sender, message):
        self.chat_display.config(state="normal")

        self.chat_display.insert(
            tk.END,
            f"\n{sender}: {message}\n"
        )

        self.chat_display.see(tk.END)
        self.chat_display.config(state="disabled")

    def send_message(self):
        question = self.message_entry.get().strip()

        if not question:
            return

        self.message_entry.delete(0, tk.END)
        self.show_message(CREATOR_NAME, question)

        action = get_command_action(question)

        if action:
            approved = messagebox.askyesno(
                "ULTRON SECURITY",
                f"Do you want ULTRON to perform this action?\n\n{question}"
            )

            if approved:
                try:
                    result = execute_action(action)
                    self.show_message("ULTRON", result)

                    threading.Thread(
                        target=speak,
                        args=(result,),
                        daemon=True
                    ).start()

                except Exception as error:
                    self.show_message(
                        "ULTRON",
                        f"Action error: {error}"
                    )
            else:
                self.show_message(
                    "ULTRON",
                    "Action cancelled."
                )

            return

        self.send_button.config(state="disabled")
        self.status_label.config(text="ULTRON: THINKING")

        threading.Thread(
            target=self.get_answer,
            args=(question,),
            daemon=True
        ).start()

    def get_answer(self, question):
        try:
            answer = ask_ultron(question)
            save_memory(question, answer)

            self.root.after(
                0,
                lambda a=answer: self.show_message("ULTRON", a)
            )

            speak(answer)

        except Exception as error:
            self.root.after(
                0,
                lambda e=str(error): self.show_message(
                    "ULTRON",
                    f"Error: {e}"
                )
            )

        finally:
            self.root.after(
                0,
                lambda: self.send_button.config(state="normal")
            )

            self.root.after(
                0,
                lambda: self.status_label.config(
                    text="ULTRON: ONLINE"
                )
            )

    def start_listening(self):
        self.mic_button.config(state="disabled")
        self.show_message("ULTRON", "Listening...")

        threading.Thread(
            target=self.listen_thread,
            daemon=True
        ).start()

    def listen_thread(self):
        try:
            command = listen()

            self.root.after(
                0,
                lambda c=command: self.receive_voice(c)
            )

        except Exception as error:
            self.root.after(
                0,
                lambda e=str(error): self.show_message(
                    "ULTRON",
                    f"Microphone error: {e}"
                )
            )

            self.root.after(
                0,
                lambda: self.mic_button.config(state="normal")
            )

    def receive_voice(self, command):
        self.mic_button.config(state="normal")

        if command:
            self.message_entry.delete(0, tk.END)
            self.message_entry.insert(0, command)
            self.send_message()
        else:
            self.show_message(
                "ULTRON",
                "I did not hear anything. Please try again."
            )

    def open_command_center(self):
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "command_center.py"
        )

        if os.path.exists(file_path):
            subprocess.Popen([sys.executable, file_path])
        else:
            messagebox.showerror(
                "ULTRON",
                "command_center.py was not found."
            )

    def update_clock(self):
        current_time = time.strftime(
            "%d %B %Y  |  %H:%M:%S"
        )

        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

    def start_monitor(self):

        def monitor():
            while True:
                try:
                    cpu = psutil.cpu_percent(interval=1)
                    ram = psutil.virtual_memory().percent

                    try:
                        requests.get(
                            "http://localhost:11434/api/tags",
                            timeout=2
                        )
                        connection = "AI CONNECTION: ONLINE"

                    except requests.RequestException:
                        connection = "AI CONNECTION: OFFLINE"

                    self.root.after(
                        0,
                        lambda c=cpu, r=ram:
                        self.monitor_label.config(
                            text=f"CPU: {c}%   RAM: {r}%"
                        )
                    )

                    self.root.after(
                        0,
                        lambda s=connection:
                        self.ollama_label.config(text=s)
                    )

                except Exception:
                    pass

        threading.Thread(
            target=monitor,
            daemon=True
        ).start()


if __name__ == "__main__":
    root = tk.Tk()
    app = UltronDashboard(root)
    root.mainloop()
