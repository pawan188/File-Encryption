import tkinter as tk
import tkinter.ttk as ttk

from tkinter import filedialog
from tkinter import messagebox

from cryptography.exceptions import InvalidTag
from file_operations import encrypt_file, decrypt_file

PLACEHOLDER = "Select a file to encrypt/decrypt"

def browse_file():
    selected_file = filedialog.askopenfilename()

    if selected_file:
        file_path.set(selected_file)
        status.config(text="File selected")

def encrypt_action():
    selected_file = file_path.get()

    if selected_file == PLACEHOLDER:
        messagebox.showerror("Error", "Please choose a file.")
        return

    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    try:
        output_path = encrypt_file(
            selected_file,
            password,
            overwrite=overwrite_var.get(),
            delete_original=delete_original_var.get()
        )

        password_entry.delete(0, tk.END)
        confirm_password_entry.delete(0, tk.END)

        status.config(
            text="Encryption successful",
        )

        messagebox.showinfo(
            "Success",
            f"File encrypted successfully.\n\nSaved to:\n{output_path}"
        )

    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "The selected file could not be found."
        )

    except FileExistsError:
        messagebox.showerror(
            "Error",
            "The encrypted file already exists.\n"
            "Use the CLI with --overwrite or choose another file."
        )

    except OSError as e:
        messagebox.showerror(
            "Error",
            f"File operation failed:\n{e}"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Unexpected error:\n{e}"
        )

def decrypt_action():
    selected_file = file_path.get()

    if selected_file == PLACEHOLDER:
        messagebox.showerror("Error", "Please choose a file.")
        return

    if not selected_file.endswith(".enc"):
        messagebox.showerror(
            "Error",
            "Please select a valid .enc encrypted file."
        )
        return

    password = password_entry.get()

    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return

    try:
        output_path = decrypt_file(
            selected_file,
            password,
            overwrite=overwrite_var.get(),
                delete_original=delete_original_var.get()
        )

        password_entry.delete(0, tk.END)
        confirm_password_entry.delete(0, tk.END)

        status.config(
            text="Decryption successful",
        )

        messagebox.showinfo(
            "Success",
            f"File decrypted successfully.\n\nSaved to:\n{output_path}"
        )

    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "The selected file could not be found."
        )

    except InvalidTag:
        messagebox.showerror(
            "Error",
            "Decryption failed. Incorrect password or corrupted encrypted file."
        )

    except ValueError as e:
        messagebox.showerror(
            "Error",
            str(e)
        )

    except FileExistsError:
        messagebox.showerror(
            "Error",
            "The decrypted file already exists."
        )

    except OSError as e:
        messagebox.showerror(
            "Error",
            f"File operation failed:\n{e}"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Unexpected error:\n{e}"
        )

# Main Window

root = tk.Tk()
root.title("Vault")
root.geometry("560x500")
root.resizable(False, False)

# Colors

BG = "#181818"
TEXT = "#F5F5F5"
SECONDARY = "#A0A0A0"
ACCENT = "#4F8CFF"
ACCENT_HOVER = "#6A9EFF"
ENTRY_BG = "#252525"
BORDER = "#3A3A3A"

root.configure(bg=BG)


# ttk Styling

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TFrame",
    background=BG
)

style.configure(
    "TLabel",
    background=BG,
    foreground=TEXT,
    font=("Segoe UI", 10)
)

style.configure(
    "Title.TLabel",
    background=BG,
    foreground=TEXT,
    font=("Segoe UI", 24, "bold")
)

style.configure(
    "Subtitle.TLabel",
    background=BG,
    foreground=SECONDARY,
    font=("Segoe UI", 10)
)

style.configure(
    "Section.TLabel",
    background=BG,
    foreground=SECONDARY,
    font=("Segoe UI", 9, "bold")
)

style.configure(
    "TEntry",
    fieldbackground=ENTRY_BG,
    foreground=TEXT,
    insertcolor=TEXT,
    borderwidth=1,
    padding=9,
    font=("Segoe UI", 10)
)

style.map(
    "TEntry",
    fieldbackground=[
        ("focus", ENTRY_BG)
    ]
)

style.configure(
    "TButton",
    font=("Segoe UI", 10),
    padding=(14, 8)
)

style.configure(
    "Accent.TButton",
    background=ACCENT,
    foreground="white",
    borderwidth=0,
    padding=(22, 9),
    font=("Segoe UI", 10, "bold")
)

style.map(
    "Accent.TButton",
    background=[
        ("active", ACCENT_HOVER),
        ("pressed", "#3D73D9")
    ]
)

style.configure(
    "TCheckbutton",
    background=BG,
    foreground=TEXT,
    font=("Segoe UI", 9)
)

style.map(
    "TCheckbutton",
    background=[
        ("active", BG)
    ],
    foreground=[
        ("active", TEXT)
    ]
)


# Main Container

main_frame = ttk.Frame(root)
main_frame.pack(
    fill="both",
    expand=True,
    padx=45,
    pady=30
)


# Header

title = ttk.Label(
    main_frame,
    text="VAULT",
    style="Title.TLabel"
)
title.pack()

subtitle = ttk.Label(
    main_frame,
    text="Secure File Encryption",
    style="Subtitle.TLabel"
)
subtitle.pack(pady=(2, 28))


# File Selection

file_label = ttk.Label(
    main_frame,
    text="FILE",
    style="Section.TLabel"
)
file_label.pack(anchor="w")

file_frame = ttk.Frame(main_frame)
file_frame.pack(
    fill="x",
    pady=(6, 20)
)

file_path = tk.StringVar(
    value="Select a file to encrypt/decrypt"
)

entry = ttk.Entry(
    file_frame,
    textvariable=file_path,
    state="readonly"
)
entry.pack(
    side="left",
    fill="x",
    expand=True
)

browse_button = ttk.Button(
    file_frame,
    text="Browse",
    command=browse_file
)
browse_button.pack(
    side="left",
    padx=(8, 0)
)


# Password

password_label = ttk.Label(
    main_frame,
    text="PASSWORD",
    style="Section.TLabel"
)
password_label.pack(anchor="w")

password_entry = ttk.Entry(
    main_frame,
    show="*"
)
password_entry.pack(
    fill="x",
    pady=(6, 18)
)


# Confirm Password

confirm_label = ttk.Label(
    main_frame,
    text="CONFIRM PASSWORD",
    style="Section.TLabel"
)
confirm_label.pack(anchor="w")

confirm_password_entry = ttk.Entry(
    main_frame,
    show="*"
)
confirm_password_entry.pack(
    fill="x",
    pady=(6, 18)
)


# Options

overwrite_var = tk.BooleanVar(value=False)
delete_original_var = tk.BooleanVar(value=False)

options_frame = ttk.Frame(main_frame)
options_frame.pack(
    fill="x",
    pady=(0, 22)
)

overwrite_check = ttk.Checkbutton(
    options_frame,
    text="Overwrite existing output",
    variable=overwrite_var
)
overwrite_check.pack(side="left")

delete_check = ttk.Checkbutton(
    options_frame,
    text="Delete original after success",
    variable=delete_original_var
)
delete_check.pack(
    side="left",
    padx=(30, 0)
)


# Action Buttons

button_frame = ttk.Frame(main_frame)
button_frame.pack()

encrypt_button = ttk.Button(
    button_frame,
    text="Encrypt",
    style="Accent.TButton",
    command=encrypt_action
)
encrypt_button.pack(
    side="left",
    padx=6
)

decrypt_button = ttk.Button(
    button_frame,
    text="Decrypt",
    style="Accent.TButton",
    command=decrypt_action
)
decrypt_button.pack(
    side="left",
    padx=6
)


# Status

status = ttk.Label(
    main_frame,
    text="Ready",
    style="Subtitle.TLabel"
)
status.pack(
    pady=(22, 0)
)


# Start Application

root.mainloop()