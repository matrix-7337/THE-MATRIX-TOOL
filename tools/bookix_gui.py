import customtkinter as ctk
from tkinter import messagebox, ttk
import requests
import webbrowser

# ------------------ CONFIG ------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# ------------------ FUNCTIONS ------------------
def search_books():
    query = entry_search.get().strip()
    if not query:
        messagebox.showerror("Error", "Please enter a book name!")
        return

    # Clear previous results
    for row in tree.get_children():
        tree.delete(row)

    try:
        q = query.replace(" ", "+")
        url = f"https://archive.org/advancedsearch.php?q={q}&fl[]=identifier&fl[]=title&fl[]=creator&sort[]=downloads+desc&rows=10&page=1&output=json"
        response = requests.get(url).json()

        if response["response"]["numFound"] == 0:
            messagebox.showinfo("No Results", "No books found on archive.org")
            return

        docs = response["response"]["docs"]
        for doc in docs:
            title = doc.get("title", "Untitled")
            author = doc.get("creator", "Unknown")
            identifier = doc["identifier"]
            link = f"https://archive.org/details/{identifier}"
            tree.insert("", ctk.END, values=(title, author, link))

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

def open_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showerror("Error", "Select a book to open.")
        return
    link = tree.item(selected[0], "values")[2]
    webbrowser.open(link)

def exit_app():
    root.destroy()

# ------------------ GUI WINDOW ------------------
root = ctk.CTk()
root.title("BOOKIX — Matrix Pro Book Finder")
root.geometry("800x600")
root.resizable(True,True)

# Title
title = ctk.CTkLabel(
    root,
    text="BOOKIX",
    font=("Orbitron", 32, "bold"),
    text_color="#00ff66"
)
title.pack(pady=(20, 5))

subtitle = ctk.CTkLabel(
    root,
    text="~ Free Book Finder ~",
    font=("Cascadia Code", 14, "bold"),
    text_color="#00ffaa"
)
subtitle.pack(pady=(0, 20))

# Search Frame
frame_search = ctk.CTkFrame(root, fg_color="#0a0a0a", corner_radius=15)
frame_search.pack(padx=20, pady=10, fill="x")

entry_search = ctk.CTkEntry(frame_search, width=600, font=("Cascadia Code", 14))
entry_search.pack(side="left", padx=10, pady=10, fill="x", expand=True)
entry_search.bind("<Return>", lambda event: search_books())

btn_search = ctk.CTkButton(frame_search, text="Search", width=120, font=("Cascadia Code", 14, "bold"), command=search_books)
btn_search.pack(side="right", padx=10)

# Results Frame
frame_results = ctk.CTkFrame(root, fg_color="#0a0a0a", corner_radius=15)
frame_results.pack(padx=20, pady=10, fill="both", expand=True)

columns = ("Title", "Author", "Link")
tree = ttk.Treeview(frame_results, columns=columns, show="headings", height=15)
tree.heading("Title", text="Title")
tree.heading("Author", text="Author")
tree.heading("Link", text="Archive Link")

tree.column("Title", width=300)
tree.column("Author", width=150)
tree.column("Link", width=300)

# Style Treeview for dark theme
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
                background="#0a0a0a",
                foreground="#00ff66",
                fieldbackground="#0a0a0a",
                font=("Cascadia Code", 12))
style.map('Treeview', background=[('selected', '#00ffaa')], foreground=[('selected', '#0a0a0a')])

tree.pack(padx=10, pady=10, fill="both", expand=True)

# Buttons Frame
btn_frame = ctk.CTkFrame(root, fg_color="#0a0a0a", corner_radius=15)
btn_frame.pack(padx=20, pady=10)

btn_open = ctk.CTkButton(btn_frame, text="Open Selected", width=180, font=("Cascadia Code", 14, "bold"), command=open_selected)
btn_open.pack(side="left", padx=20, pady=10)

btn_exit = ctk.CTkButton(btn_frame, text="Exit", width=180, font=("Cascadia Code", 14, "bold"), fg_color="#aa0000", hover_color="#ff4444", command=exit_app)
btn_exit.pack(side="right", padx=20, pady=10)

root.mainloop()
