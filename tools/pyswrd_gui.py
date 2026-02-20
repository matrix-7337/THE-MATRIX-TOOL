import customtkinter as ctk
from tkinter import messagebox
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

FILE = "passwords2.txt"

# -------------------- Function --------------------
def generate_password():
    try:
        length = int(entry_length.get())
        characters = entry_chars.get().strip()

        if length <= 0 or not characters:
            messagebox.showerror("Error", "Enter valid length and characters")
            return

        password = "".join(random.choice(characters) for _ in range(length))

        entry_result.configure(state="normal")
        entry_result.delete(0, ctk.END)
        entry_result.insert(0, password)
        entry_result.configure(state="readonly")

        # Save to file
        with open(FILE, "a") as f:
            f.write(password + "\n")

        messagebox.showinfo("Saved", f"Password saved in {FILE}")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for length")

# -------------------- GUI WINDOW --------------------
root = ctk.CTk()
root.title("PYSWRD — Password Generator")
root.geometry("450x450")
root.resizable(True,True)

# Title
title = ctk.CTkLabel(
    root,
    text="PYSWRD",
    font=("Orbitron", 24, "bold"),
    text_color="#00ff66"
)
title.pack(pady=15)

subtitle = ctk.CTkLabel(
    root,
    text="Generate Secure Passwords",
    font=("Cascadia Code", 14),
    text_color="#00ffaa"
)
subtitle.pack(pady=5)

# Entry for Length
label_length = ctk.CTkLabel(root, text="Password Length:", font=("Cascadia Code", 14))
label_length.pack(pady=5)
entry_length = ctk.CTkEntry(root, width=250, placeholder_text="Enter length")
entry_length.pack(pady=5)

# Entry for Characters
label_chars = ctk.CTkLabel(root, text="Characters to Use:", font=("Cascadia Code", 14))
label_chars.pack(pady=5)
entry_chars = ctk.CTkEntry(root, width=250, placeholder_text="Enter characters")
entry_chars.pack(pady=5)

# Generate Button
btn_generate = ctk.CTkButton(
    root,
    text="Generate Password",
    width=200,
    height=40,
    font=("Cascadia Code", 14),
    fg_color="#00aa55",
    hover_color="#00ff66",
    text_color="black",
    command=generate_password
)
btn_generate.pack(pady=15)

# Result
label_result = ctk.CTkLabel(root, text="Generated Password:", font=("Cascadia Code", 14))
label_result.pack(pady=5)
entry_result = ctk.CTkEntry(root, width=300, state="readonly")
entry_result.pack(pady=5)

root.mainloop()
