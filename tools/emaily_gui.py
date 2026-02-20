import customtkinter as ctk
from tkinter import messagebox
import smtplib

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# -----------------------------
# Hardcoded Gmail credentials
# -----------------------------
your_email = "matrix.tests67@gmail.com"  # Replace with your email
your_app_password = "mkacxbyftomwxwbg"                  # Replace with your app password

# -----------------------------
# Function to send email
# -----------------------------
def send_email():
    subject = subject_entry.get().strip()
    message = message_text.get("1.0", ctk.END).strip()
    emails = recipients_entry.get().strip().split(",")

    if not subject or not message or not emails:
        messagebox.showerror("Error", "Please fill all fields!")
        return

    try:
        for e in emails:
            e = e.strip()
            text = f"Subject: {subject}\n\n{message}"
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(your_email, your_app_password)
            server.sendmail(your_email, e, text)
            server.quit()
        messagebox.showinfo("Success", "Emails sent successfully!")
    except Exception as err:
        messagebox.showerror("Error", f"Failed to send emails.\n{err}")

# -----------------------------
# GUI WINDOW
# -----------------------------
root = ctk.CTk()
root.title("EMAILY")
root.geometry("550x500")
root.resizable(False, False)

# Title
title = ctk.CTkLabel(
    root,
    text="EMAILY",
    font=("Orbitron", 24, "bold"),
    text_color="#00ff66"
)
title.pack(pady=20)

# Subject Entry
subject_label = ctk.CTkLabel(root, text="Subject:", font=("Cascadia Code", 14))
subject_label.pack(pady=5)
subject_entry = ctk.CTkEntry(root, width=450)
subject_entry.pack(pady=5)

# Message Text
message_label = ctk.CTkLabel(root, text="Message:", font=("Cascadia Code", 14))
message_label.pack(pady=5)
message_text = ctk.CTkTextbox(root, width=500, height=150, font=("Cascadia Code", 12))
message_text.pack(pady=5)

# Recipients Entry
recipients_label = ctk.CTkLabel(root, text="Recipients (comma separated):", font=("Cascadia Code", 14))
recipients_label.pack(pady=5)
recipients_entry = ctk.CTkEntry(root, width=450)
recipients_entry.pack(pady=5)

# Send Button
send_button = ctk.CTkButton(
    root,
    text="Send Email",
    width=200,
    height=45,
    font=("Cascadia Code", 14),
    fg_color="#00aa55",
    hover_color="#00ff66",
    text_color="black",
    command=send_email
)
send_button.pack(pady=20)

root.mainloop()
