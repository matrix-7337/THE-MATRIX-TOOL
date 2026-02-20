import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# ---------------- GUI WINDOW ----------------
window = ctk.CTk()
window.title("Calculator (Matrix Tool)")
window.geometry("400x400")
window.resizable(False, False)

# Title
title = ctk.CTkLabel(
    window,
    text="CALCULATOR",
    font=("Orbitron", 24, "bold"),
    text_color="#00ff66"
)
title.pack(pady=20)

# Frame for inputs
frame_inputs = ctk.CTkFrame(window, fg_color="#0a0a0a")
frame_inputs.pack(pady=10, padx=20, fill="both", expand=True)

# Entry fields
entry_num1 = ctk.CTkEntry(frame_inputs, placeholder_text="Enter first number", width=250)
entry_num1.pack(pady=10)

entry_op = ctk.CTkEntry(frame_inputs, placeholder_text="Operator (+, -, *, /)", width=250)
entry_op.pack(pady=10)

entry_num2 = ctk.CTkEntry(frame_inputs, placeholder_text="Enter second number", width=250)
entry_num2.pack(pady=10)

# Result Label
label_result = ctk.CTkLabel(window, text="Result: ", font=("Cascadia Code", 16), text_color="#00ff66")
label_result.pack(pady=15)

# Function
def calculate():
    try:
        num1 = float(entry_num1.get())
        op = entry_op.get().strip()
        num2 = float(entry_num2.get())

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operator")
            return

        label_result.configure(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Calculate button
button = ctk.CTkButton(
    window,
    text="Calculate",
    command=calculate,
    width=200,
    height=40,
    corner_radius=10,
    fg_color="#00aa55",
    hover_color="#00ff66",
    text_color="black"
)
button.pack(pady=10)

# Run the window
window.mainloop()
