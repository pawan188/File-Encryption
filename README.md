# Vault

A secure command-line file encryption and decryption tool written in Python using **AES-256-GCM** for authenticated encryption and **Scrypt** for password-based key derivation.

---

## Features

- AES-256-GCM authenticated encryption
- Password-based key derivation using Scrypt
- Random 16-byte salt and 12-byte nonce generated for every encryption
- Secure password input using `getpass`
- Password confirmation before encryption
- Command-line interface built with `argparse`
- Overwrite protection using `--overwrite`
- Optional deletion of the original file using `--delete-original`
- Graceful error handling for:
  - Missing files
  - Invalid `.enc` files
  - Incorrect passwords
  - Corrupted encrypted files

---

## Project Structure

```text
vault/
│
├── crypto_core.py          # Cryptographic operations
├── vault.py                # Command-line interface
├── Encrypted_Files/        # Encrypted output files
├── Decrypted_Files/        # Decrypted output files
├── tests/                  # Pytest unit tests (Yet to implement)
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository and install the dependencies.

```bash
git clone <repository-url>
cd "File Encryption"

python -m venv .venv
```

Activate the virtual environment.

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

---

## Usage

### Encrypt a file

```bash
python vault.py encrypt Sample_Files/example.pdf
```

Encrypted output:

```text
Encrypted_Files/example.pdf.enc
```

---

### Decrypt a file

```bash
python vault.py decrypt Encrypted_Files/example.pdf.enc
```

Decrypted output:

```text
Decrypted_Files/example.pdf
```

---

### Overwrite an existing output file

```bash
python vault.py encrypt Sample_Files/example.pdf --overwrite
```

---

### Delete the original file after success

```bash
python vault.py encrypt Sample_Files/example.pdf --delete-original
```

Both flags can be combined:

```bash
python vault.py encrypt Sample_Files/example.pdf --overwrite --delete-original
```

---

## Encrypted File Format

```
[ Salt (16 bytes) ][ Nonce (12 bytes) ][ Ciphertext + Authentication Tag ]
```

---

## Security Notes

- Every encryption operation uses a fresh random salt and nonce.
- AES-GCM provides both confidentiality and integrity.
- Scrypt protects against brute-force attacks by making key derivation computationally expensive.
- Passwords are never stored.
- Incorrect passwords and tampered files produce the same authentication failure.

---

## Current Limitations

- Files are currently loaded entirely into memory before encryption/decryption.
- Password recovery is not possible.
- Streaming encryption for very large files is not yet implemented.

---

## Future Improvements

- Streaming encryption using the lower-level `Cipher` API
- Configurable output directory
- Progress indicator for large files

---

## License

This project is intended for educational and learning purposes.