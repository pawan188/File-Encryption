# Vault 

A secure command-line file encryption tool built in Python using **AES-256-GCM** for authenticated encryption and **Scrypt** for password-based key derivation.

Vault encrypts and decrypts files while ensuring both confidentiality and integrity. Every encrypted file is protected with a unique salt and nonce, making each encryption operation cryptographically secure.

---

## Features

- AES-256-GCM authenticated encryption
- Password-based key derivation using Scrypt
- Random salt generated for every encrypted file
- Random nonce generated for every encryption
- Secure password input using `getpass`
- Password confirmation before encryption
- Detects incorrect passwords
- Detects tampered or corrupted encrypted files
- Overwrite protection
- Option to delete the original file after encryption/decryption
- Comprehensive unit tests using pytest

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
├── vault.py
├── requirements.txt
└── README.md
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

---

## Usage

### Encrypt a file

```bash
python vault.py encrypt Sample_Files/example.pdf
```

### Decrypt a file

```bash
python vault.py decrypt Encrypted_Files/example.pdf.enc
```

### Overwrite existing output

```bash
python vault.py encrypt file.txt --overwrite
```

### Delete original file after successful encryption

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

The authentication tag is produced automatically by AES-GCM and is stored with the ciphertext.

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

Run the complete test suite:

```bash
python -m pytest -v
```

Current tests include:

- Round-trip encryption and decryption
- Wrong password detection
- Tampered ciphertext detection
- Empty plaintext
- Round-trip encryption and decryption with random binary data

---

## Technologies Used

- Python 3
- cryptography
- argparse
- getpass
- pytest

---

## Future Improvements

- GitHub Actions (CI)
- Code formatting with Black
- Linting using Ruff
- Streaming encryption for large files
- Progress indicator
- Configurable output directory
- Package distribution via PyPI

---

## License

This project is intended for educational purposes and cybersecurity learning.