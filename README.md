// ...existing code...
# Vault

A secure file encryption tool built in Python using **AES-256-GCM** for authenticated encryption and **Scrypt** for password-based key derivation.

Vault encrypts and decrypts files while ensuring both confidentiality and integrity. Every encrypted file is protected with a unique salt and nonce, making each encryption operation cryptographically secure. This project now provides both a CLI and a simple GUI (tkinter).

---

## Features

- AES-256-GCM authenticated encryption
- Password-based key derivation using Scrypt
- Random salt generated for every encrypted file
- Random nonce generated for every encryption
- Secure password input using `getpass` (CLI) and masked entry with confirmation (GUI)
- Password confirmation enforced in GUI before encryption
- Detects incorrect passwords
- Detects tampered or corrupted encrypted files
- Overwrite protection
- Option to delete the original file after encryption/decryption
- Unit tests using pytest

---

## Project Structure

```
Vault/
│
├── Encrypted_Files/
├── Decrypted_Files/
├── Sample_Files/
├── tests/
│   └── test_crypto.py
│
├── crypto_core.py
├── file_operations.py
├── vault.py        # CLI entrypoint
├── gui.py          # Simple tkinter GUI frontend
├── requirements.txt
└── Readme.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Vault
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Note: Tkinter is required for the GUI. On Windows, Tkinter is usually included with Python. On Debian/Ubuntu:

```bash
sudo apt install python3-tk
```

---

## Usage

### Run the GUI

```bash
python gui.py
```

GUI highlights:
- File browser to select input file
- Password and confirm password fields (masked)
- Overwrite and "delete original after success" checkboxes
- Separate Encrypt and Decrypt buttons
- Status label and dialog popups for success/errors

The GUI calls file_operations.encrypt_file / decrypt_file and uses the same backend as the CLI.

### CLI: Encrypt a file

```bash
python vault.py encrypt Sample_Files/example.pdf
```

### CLI: Decrypt a file

```bash
python vault.py decrypt Encrypted_Files/example.pdf.enc
```

### Overwrite existing output (CLI)

```bash
python vault.py encrypt file.txt --overwrite
```

### Delete original file after successful encryption (CLI)

```bash
python vault.py encrypt file.txt --delete-original
```

---

## Encryption Process

For every encryption:

1. A random 16-byte salt is generated.
2. A 256-bit encryption key is derived from the user's password using Scrypt.
3. A random 12-byte nonce is generated.
4. AES-256-GCM encrypts the file.
5. The encrypted file stores:

```
+----------------+----------------+---------------------------+
| Salt (16 B)    | Nonce (12 B)   | Ciphertext + Auth Tag     |
+----------------+----------------+---------------------------+
```

The authentication tag is produced by AES-GCM and stored with the ciphertext.

---

## Security Features

- Unique encryption key for every password/salt combination
- Random nonce for every encryption
- Authenticated encryption prevents undetected tampering
- Wrong passwords are rejected
- Corrupted or modified encrypted files are rejected
- Passwords are never stored

---

## Testing

Run the test suite:

```bash
python -m pytest -v
```

Tests include:
- Round-trip encryption and decryption
- Wrong password detection
- Tampered ciphertext detection
- Empty plaintext
- Binary data round-trips

---

## Technologies Used

- Python 3
- cryptography
- argparse
- getpass
- tkinter (GUI)
- pytest

---

## Future Improvements

- CI (GitHub Actions)
- Code formatting with Black
- Linting with Ruff
- Streaming encryption for large files
- Progress indicator in GUI
- Configurable output directory
- Package distribution via PyPI

---

## License

This project is intended for educational purposes and cybersecurity learning.
```// filepath: c:\Users\pawan\Documents\Projects\File Encryption\Readme.md
// ...existing code...
# Vault

A secure file encryption tool built in Python using **AES-256-GCM** for authenticated encryption and **Scrypt** for password-based key derivation.

Vault encrypts and decrypts files while ensuring both confidentiality and integrity. Every encrypted file is protected with a unique salt and nonce, making each encryption operation cryptographically secure. This project now provides both a CLI and a simple GUI (tkinter).

---

## Features

- AES-256-GCM authenticated encryption
- Password-based key derivation using Scrypt
- Random salt generated for every encrypted file
- Random nonce generated for every encryption
- Secure password input using `getpass` (CLI) and masked entry with confirmation (GUI)
- Password confirmation enforced in GUI before encryption
- Detects incorrect passwords
- Detects tampered or corrupted encrypted files
- Overwrite protection
- Option to delete the original file after encryption/decryption
- Unit tests using pytest

---

## Project Structure

```
Vault/
│
├── Encrypted_Files/
├── Decrypted_Files/
├── Sample_Files/
├── tests/
│   └── test_crypto.py
│
├── crypto_core.py
├── file_operations.py
├── vault.py        # CLI entrypoint
├── gui.py          # Simple tkinter GUI frontend
├── requirements.txt
└── Readme.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Vault
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Note: Tkinter is required for the GUI. On Windows, Tkinter is usually included with Python. On Debian/Ubuntu:

```bash
sudo apt install python3-tk
```

---

## Usage

### Run the GUI

```bash
python gui.py
```

GUI highlights:
- File browser to select input file
- Password and confirm password fields (masked)
- Overwrite and "delete original after success" checkboxes
- Separate Encrypt and Decrypt buttons
- Status label and dialog popups for success/errors

The GUI calls file_operations.encrypt_file / decrypt_file and uses the same backend as the CLI.

### CLI: Encrypt a file

```bash
python vault.py encrypt Sample_Files/example.pdf
```

### CLI: Decrypt a file

```bash
python vault.py decrypt Encrypted_Files/example.pdf.enc
```

### Overwrite existing output (CLI)

```bash
python vault.py encrypt file.txt --overwrite
```

### Delete original file after successful encryption (CLI)

```bash
python vault.py encrypt file.txt --delete-original
```

---

## Encryption Process

For every encryption:

1. A random 16-byte salt is generated.
2. A 256-bit encryption key is derived from the user's password using Scrypt.
3. A random 12-byte nonce is generated.
4. AES-256-GCM encrypts the file.
5. The encrypted file stores:

```
+----------------+----------------+---------------------------+
| Salt (16 B)    | Nonce (12 B)   | Ciphertext + Auth Tag     |
+----------------+----------------+---------------------------+
```

The authentication tag is produced by AES-GCM and stored with the ciphertext.

---

## Security Features

- Unique encryption key for every password/salt combination
- Random nonce for every encryption
- Authenticated encryption prevents undetected tampering
- Wrong passwords are rejected
- Corrupted or modified encrypted files are rejected
- Passwords are never stored

---

## Testing

Run the test suite:

```bash
python -m pytest -v
```

Tests include:
- Round-trip encryption and decryption
- Wrong password detection
- Tampered ciphertext detection
- Empty plaintext
- Binary data round-trips

---

## Technologies Used

- Python 3
- cryptography
- argparse
- getpass
- tkinter (GUI)
- pytest

---

## Future Improvements

- CI (GitHub Actions)
- Code formatting with Black
- Linting with Ruff
- Streaming encryption for large files
- Progress indicator in GUI
- Configurable output directory
- Package distribution via PyPI

---

## License

This project is intended for educational purposes and cybersecurity learning.