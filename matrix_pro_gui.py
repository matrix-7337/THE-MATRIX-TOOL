import customtkinter as ctk
import subprocess
import os
import sys
from tkinter import messagebox

# =================================================
# PYINSTALLER SAFE BASE DIRECTORY (DO NOT REMOVE)
# =================================================
if getattr(sys, "frozen", False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TOOLS_DIR = os.path.join(BASE_DIR, "tools")

# =================================================
# CUSTOMTKINTER THEME (UNCHANGED – FABULOUS)
# =================================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# =================================================
# MAIN WINDOW
# =================================================
app = ctk.CTk()
app.title("THE MATRIX — PRO")
app.geometry("600x600")
app.resizable(False, False)

# =================================================
# HEADER
# =================================================
title = ctk.CTkLabel(
    app,
    text="THE MATRIX",
    font=("Orbitron", 40, "bold"),
    text_color="#00ff88"
)
title.pack(pady=(30, 5))

subtitle = ctk.CTkLabel(
    app,
    text="~ MADE BY RAUNAK ~",
    font=("Cascadia Code", 14, "bold"),
    text_color="#00ffaa"
)
subtitle.pack(pady=(0, 25))

# =================================================
# TOOL LAUNCHER (EXE SAFE)
# =================================================
def run_tool(script_name):
    tool_path = os.path.join(TOOLS_DIR, script_name)

    if not os.path.exists(tool_path):
        messagebox.showerror(
            "Tool Missing",
            f"{script_name} not found inside tools folder."
        )
        return

    try:
        subprocess.Popen([sys.executable, tool_path])
    except Exception as e:
        messagebox.showerror("Error", str(e))

# =================================================
# BUTTON GRID FRAME
# =================================================
frame = ctk.CTkFrame(
    app,
    fg_color="#0b0b0b",
    corner_radius=20
)
frame.pack(pady=10, padx=40, fill="both", expand=True)

# =================================================
# BUTTON STYLE
# =================================================
BTN_FONT = ("Cascadia Code", 15)
BTN_WIDTH = 260
BTN_HEIGHT = 45

# =================================================
# TOOLS LIST
# =================================================
tools = [
    ("📧 Emaily", "emaily_gui.py"),
    ("🔐 Password Generator", "pyswrd_gui.py"),
    ("🧮 Calculator", "calc_gui.py"),
    ("📝 Tasker", "tasker_gui.py"),
    ("📘 Bookix", "bookix_gui.py"),
    ("🤖 Buddy Bot", "search_gui.py"),
    ("📷 QR Generator", "qr_gui.py"),
]

# =================================================
# BUTTON CREATION
# =================================================
for name, script in tools:
    btn = ctk.CTkButton(
        frame,
        text=name,
        width=BTN_WIDTH,
        height=BTN_HEIGHT,
        font=BTN_FONT,
        corner_radius=15,
        command=lambda s=script: run_tool(s)
    )
    btn.pack(pady=8)

# =================================================
# EXIT BUTTON
# =================================================
exit_btn = ctk.CTkButton(
    app,
    text="EXIT MATRIX",
    width=300,
    height=45,
    font=("Cascadia Code", 15, "bold"),
    fg_color="#aa0000",
    hover_color="#ff3333",
    corner_radius=20,
    command=app.destroy
)
exit_btn.pack(pady=20)

# =================================================
# START APP
# =================================================
app.mainloop()
