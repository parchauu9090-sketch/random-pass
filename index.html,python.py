import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")
        return

    characters = ""

    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showerror("Error", "Select at least one option!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("480x450")
root.resizable(False, False)

title = tk.Label(root, text="Advanced Password Generator", font=("Arial", 16, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Enter Length:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
length_entry = tk.Entry(frame, width=10, font=("Arial", 12))
length_entry.grid(row=0, column=1, padx=5)


options_frame = tk.LabelFrame(root, text="Options", font=("Arial", 12))
options_frame.pack(pady=10)

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(options_frame, text="Uppercase Letters (A-Z)", variable=var_upper).pack(anchor="w")
tk.Checkbutton(options_frame, text="Lowercase Letters (a-z)", variable=var_lower).pack(anchor="w")
tk.Checkbutton(options_frame, text="Numbers (0-9)", variable=var_digits).pack(anchor="w")
tk.Checkbutton(options_frame, text="Symbols (!@#$%^&*)", variable=var_symbols).pack(anchor="w")

generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password)
generate_btn.pack(pady=10)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=30)
password_entry.pack(pady=5)

copy_btn = tk.Button(root, text="Copy Password", font=("Arial", 12), command=copy_password)
copy_btn.pack(pady=10)

root.mainloop()
