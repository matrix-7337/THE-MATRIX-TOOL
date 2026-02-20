import customtkinter as ctk
from tkinter import scrolledtext, messagebox
from groq import Groq

# ------------------ CONFIG ------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

API_KEY = ""
client = Groq(api_key=API_KEY)

# ------------------ FUNCTIONS ------------------
def send_message(event=None):
    user_input = entry.get().strip()
    if not user_input:
        return

    chat_box.configure(state="normal")
    chat_box.insert(ctk.END, f"You: {user_input}\n", "user")
    chat_box.configure(state="disabled")
    entry.delete(0, ctk.END)

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": user_input}]
        )
        bot_reply = response.choices[0].message.content
    except Exception as e:
        bot_reply = f"Error: {e}"

    chat_box.configure(state="normal")
    chat_box.insert(ctk.END, f"Buddy: {bot_reply}\n\n", "bot")
    chat_box.configure(state="disabled")
    chat_box.see(ctk.END)

def exit_app():
    root.destroy()

# ------------------ GUI WINDOW ------------------
root = ctk.CTk()
root.title("Buddy Bot — Matrix Pro")
root.geometry("700x600")
root.resizable(True,True)

# Title
title = ctk.CTkLabel(
    root,
    text="BUDDY BOT",
    font=("Orbitron", 32, "bold"),
    text_color="#00ff66"
)
title.pack(pady=(20, 5))

subtitle = ctk.CTkLabel(
    root,
    text="~ BY RAUNAQ",
    font=("Cascadia Code", 14, "bold"),
    text_color="#00ffaa"
)
subtitle.pack(pady=(0, 20))

# Chat Box Frame
frame_chat = ctk.CTkFrame(root, fg_color="#0a0a0a", corner_radius=15)
frame_chat.pack(padx=20, pady=10, fill="both", expand=True)

chat_box = scrolledtext.ScrolledText(
    frame_chat,
    width=80,
    height=25,
    font=("Cascadia Code", 12, "bold"),
    bg="#0a0a0a",
    fg="#00ff66",
    insertbackground="#00ffaa",  # cursor color
    state="disabled",
    wrap="word"
)
chat_box.pack(padx=10, pady=10, fill="both", expand=True)

# Tag colors
chat_box.tag_config("user", foreground="#00ffaa")
chat_box.tag_config("bot", foreground="#00ff66")

# Entry Frame
entry_frame = ctk.CTkFrame(root, fg_color="#0a0a0a", corner_radius=10)
entry_frame.pack(padx=20, pady=10, fill="x")

entry = ctk.CTkEntry(entry_frame, width=500, font=("Cascadia Code", 14))
entry.pack(side="left", padx=10, pady=10, fill="x", expand=True)
entry.bind("<Return>", send_message)

send_btn = ctk.CTkButton(entry_frame, text="Send", width=100, font=("Cascadia Code", 14, "bold"), command=send_message)
send_btn.pack(side="right", padx=10)

# Exit Button
btn_exit = ctk.CTkButton(root, text="Exit", width=200, height=50,
                         font=("Cascadia Code", 16, "bold"),
                         fg_color="#aa0000", hover_color="#ff4444", command=exit_app)
btn_exit.pack(pady=20)

root.mainloop()
