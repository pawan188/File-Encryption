import tkinter as tk

from tkinter import filedialog
from tkinter import messagebox

from cryptography.exceptions import InvalidTag
from file_operations import encrypt_file, decrypt_file

PLACEHOLDER = "Select a file to encrypt/decrypt"

def browse_file():
    selected_file = filedialog.askopenfilename()

    if selected_file:
        file_path.set(selected_file)
        status.config(text="File selected", fg="blue")

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
            fg="green"
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
            fg="green"
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

root = tk.Tk()
root.title("Vault")
root.geometry("500x320")
root.resizable(False, False)

# TITLE
title = tk.Label(
    root,
    text="Vault File Encryption",
    font=("Helvetica", 16, "bold")
)
title.pack(pady=20)

# FILE SELECTION
file_frame = tk.Frame(root)
file_frame.pack(pady=5)

file_path = tk.StringVar(value=PLACEHOLDER)
overwrite_var = tk.BooleanVar(value=False)
delete_original_var = tk.BooleanVar(value=False)

entry = tk.Entry(
    file_frame,
    textvariable=file_path,
    width=40,
    state="readonly"
)
entry.pack(side="left")

browse_button = tk.Button(
    file_frame,
    text="Browse",
    command=browse_file
)
browse_button.pack(side="left", padx=5)

#PASSWORD ENTRY
tk.Label(root, text="Password").pack(pady=(15, 0))

password_entry = tk.Entry(
    root,
    show="*",
    width=40
)
password_entry.pack(pady=5)

#CONFIRM PASSWORD
tk.Label(root, text="Confirm Password").pack()

confirm_password_entry = tk.Entry(
    root,
    show="*",
    width=40
)
confirm_password_entry.pack(pady=5)

#OPTIONS
options_frame = tk.Frame(root)
options_frame.pack(pady=5)

overwrite_check = tk.Checkbutton(
    options_frame,
    text="Overwrite existing output",
    variable=overwrite_var
)
overwrite_check.pack(side="left", padx=10)

delete_check = tk.Checkbutton(
    options_frame,
    text="Delete original after success",
    variable=delete_original_var
)
delete_check.pack(side="left", padx=10)

#BUTTONS
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

encrypt_button = tk.Button(
    button_frame,
    text="Encrypt",
    width=15,
    command=encrypt_action
)
encrypt_button.pack(side="left", padx=10)

decrypt_button = tk.Button(
    button_frame,
    text="Decrypt",
    width=15,
    command=decrypt_action
)
decrypt_button.pack(side="left", padx=10)

#STATUS
status = tk.Label(
    root,
    text="Ready",
    fg="blue"
)
status.pack(pady=10)

root.mainloop()