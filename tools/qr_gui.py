import customtkinter as ctk
from tkinter import messagebox, filedialog
import qrcode

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# ---------------- GUI WINDOW ----------------
root = ctk.CTk()
root.title("QR Code Generator")
root.geometry("450x300")
root.resizable(False, False)

# Title label
title = ctk.CTkLabel(
    root,
    text="QR CODE GENERATOR",
    font=("Orbitron", 24, "bold"),
    text_color="#00ff66"
)
title.pack(pady=20)

# Instruction label
label_instr = ctk.CTkLabel(
    root,
    text="Enter URL to generate QR:",
    font=("Cascadia Code", 14),
    text_color="#00ffaa"
)
label_instr.pack(pady=5)

# Entry field
entry_url = ctk.CTkEntry(root, width=350, placeholder_text="Enter URL here")
entry_url.pack(pady=10)

# Function
def generate_qr():
    url = entry_url.get().strip()
    if url == "":
        messagebox.showerror("Error", "Please enter a URL!")
        return
    try:
        # Generate QR image
        img = qrcode.make(url)
        # Ask user where to save the file
        filepath = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")],
            title="Save QR Code"
        )
        if filepath:
            img.save(filepath)
            messagebox.showinfo("Success", f"QR Code saved:\n{filepath}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# Generate button
button_generate = ctk.CTkButton(
    root,
    text="Generate QR Code",
    width=250,
    height=45,
    font=("Cascadia Code", 14),
    fg_color="#00aa55",
    hover_color="#00ff66",
    text_color="black",
    command=generate_qr
)
button_generate.pack(pady=20)

# Run window
root.mainloop()
