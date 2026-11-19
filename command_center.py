
import tkinter as tk
from tkinter import messagebox
import subprocess
import platform
import os

BG = "#080000"
PANEL = "#190707"
RED = "#ff2020"
WHITE = "#ffffff"

def show_system_info():
    info = (
        f"Computer: {platform.node()}\n"
        f"Operating System: {platform.system()}\n"
        f"Version: {platform.version()}\n"
        f"Processor: {platform.processor()}"
    )
    messagebox.showinfo("ULTRON SYSTEM INFORMATION", info)

def open_notepad():
    if messagebox.askyesno(
        "ULTRON SECURITY",
        "Do you want ULTRON to open Notepad?"
    ):
        subprocess.Popen(["notepad.exe"])

def open_calculator():
    if messagebox.askyesno(
        "ULTRON SECURITY",
        "Do you want ULTRON to open Calculator?"
    ):
        subprocess.Popen(["calc.exe"])

def open_project_folder():
    if messagebox.askyesno(
        "ULTRON SECURITY",
        "Do you want ULTRON to open its project folder?"
    ):
        os.startfile(os.getcwd())

def show_about():
    messagebox.showinfo(
        "ABOUT ULTRON",
        "ULTRON AI COMMAND CENTER\n\n"
        "Creator: Emmanuel Cornelius\n"
        "AI Engine: Ollama / Llama 3\n"
        "Theme: Red Edition\n"
        "Status: Active"
    )

root = tk.Tk()
root.title("ULTRON COMMAND CENTER")
root.geometry("650x550")
root.configure(bg=BG)
root.resizable(False, False)

tk.Label(
    root,
    text="ULTRON",
    font=("Arial", 30, "bold"),
    fg=RED,
    bg=BG
).pack(pady=(20, 0))

tk.Label(
    root,
    text="COMMAND CENTER",
    font=("Arial", 13, "bold"),
    fg=WHITE,
    bg=BG
).pack(pady=5)

panel = tk.Frame(
    root,
    bg=PANEL,
    highlightbackground=RED,
    highlightthickness=2
)
panel.pack(fill="both", expand=True, padx=30, pady=25)

def create_button(text, command):
    tk.Button(
        panel,
        text=text,
        command=command,
        bg=RED,
        fg=WHITE,
        activebackground="#990000",
        activeforeground=WHITE,
        font=("Arial", 12, "bold"),
        relief="flat",
        width=32,
        pady=10
    ).pack(pady=10)

create_button("OPEN NOTEPAD", open_notepad)
create_button("OPEN CALCULATOR", open_calculator)
create_button("OPEN PROJECT FOLDER", open_project_folder)
create_button("SYSTEM INFORMATION", show_system_info)
create_button("ABOUT ULTRON", show_about)

tk.Label(
    root,
    text="ULTRON AI | SECURE COMMAND CENTER",
    fg="#a66b6b",
    bg=BG,
    font=("Arial", 9)
).pack(pady=10)

root.mainloop()
