import customtkinter as ctk
from tkinter import messagebox, simpledialog
import os

# ------------------ CONFIG ------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

FILE = "tasks.txt"

# ------------------ TASK LOGIC ------------------
def read_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return [t.strip() for t in f.readlines()]

def write_tasks(tasks):
    with open(FILE, "w") as f:
        for t in tasks:
            f.write(t + "\n")

# ------------------ GUI FUNCTIONS ------------------
tasks = read_tasks()

def refresh_list():
    task_list.configure(state="normal")
    task_list.delete("1.0", ctk.END)
    for i, t in enumerate(tasks, 1):
        task_list.insert(ctk.END, f"{i}. {t}\n")
    task_list.configure(state="disabled")

def add_task():
    task = simpledialog.askstring("Add Task", "Enter your task:")
    if task:
        tasks.append(task)
        write_tasks(tasks)
        refresh_list()

def remove_task():
    selected = task_list.get("sel.first", "sel.last") if task_list.tag_ranges("sel") else None
    if not selected:
        messagebox.showerror("Error", "Select a task to remove.")
        return
    index = task_list.index("sel.first").split(".")[0]
    tasks.pop(int(index)-1)
    write_tasks(tasks)
    refresh_list()

def modify_task():
    selected = task_list.get("sel.first", "sel.last") if task_list.tag_ranges("sel") else None
    if not selected:
        messagebox.showerror("Error", "Select a task to modify.")
        return
    index = int(task_list.index("sel.first").split(".")[0])-1
    current = tasks[index]
    new_text = simpledialog.askstring("Modify Task", "Edit your task:", initialvalue=current)
    if new_text:
        tasks[index] = new_text
        write_tasks(tasks)
        refresh_list()

def exit_app():
    root.destroy()

# ------------------ MAIN WINDOW ------------------
root = ctk.CTk()
root.title("TASKER — Matrix Pro")
root.geometry("700x600")
root.resizable(False, False)

# Title
title = ctk.CTkLabel(
    root,
    text="TASKER",
    font=("Orbitron", 32, "bold"),
    text_color="#00ff66"
)
title.pack(pady=(20, 10))

subtitle = ctk.CTkLabel(
    root,
    text="~ BY RAUNAQ",
    font=("Cascadia Code", 14, "bold"),
    text_color="#00ffaa"
)
subtitle.pack(pady=(0, 20))

# ------------------ TASK LIST FRAME ------------------
frame_list = ctk.CTkFrame(
    root,
    fg_color="#0a0a0a",
    corner_radius=15
)
frame_list.pack(pady=10, padx=20, fill="both", expand=True)

# Task Listbox (CustomTkinter Textbox)
task_list = ctk.CTkTextbox(
    frame_list,
    font=("Cascadia Code", 14, "bold"),
    width=600,
    height=350,
    corner_radius=10,
    fg_color="#0a0a0a",
    text_color="#00ff66",
    border_color="#00ffaa",
    border_width=2
)
task_list.pack(pady=15, padx=15, fill="both", expand=True)
task_list.configure(state="disabled")

refresh_list()

# ------------------ BUTTONS FRAME ------------------
btn_frame = ctk.CTkFrame(
    root,
    fg_color="#0a0a0a",
    corner_radius=10
)
btn_frame.pack(pady=15)

btn_add = ctk.CTkButton(
    btn_frame,
    text="Add",
    width=150,
    height=40,
    font=("Cascadia Code", 14, "bold"),
    fg_color="#004400",
    hover_color="#006600",
    command=add_task
)
btn_add.grid(row=0, column=0, padx=10, pady=10)

btn_remove = ctk.CTkButton(
    btn_frame,
    text="Remove",
    width=150,
    height=40,
    font=("Cascadia Code", 14, "bold"),
    fg_color="#440000",
    hover_color="#660000",
    command=remove_task
)
btn_remove.grid(row=0, column=1, padx=10, pady=10)

btn_modify = ctk.CTkButton(
    btn_frame,
    text="Modify",
    width=150,
    height=40,
    font=("Cascadia Code", 14, "bold"),
    fg_color="#004466",
    hover_color="#006688",
    command=modify_task
)
btn_modify.grid(row=0, column=2, padx=10, pady=10)

btn_exit = ctk.CTkButton(
    root,
    text="Exit",
    width=200,
    height=50,
    font=("Cascadia Code", 16, "bold"),
    fg_color="#aa0000",
    hover_color="#ff4444",
    command=exit_app
)
btn_exit.pack(pady=20)

root.mainloop()
