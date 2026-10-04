# Vault — Secure File Encryption

Vault is a Python-based file encryption tool that provides both a command-line interface (CLI) and a graphical user interface (GUI) for securely encrypting and decrypting files.

It uses **AES-256-GCM** for authenticated encryption and **Scrypt** for password-based key derivation.

## Features

- AES-256-GCM authenticated encryption
- Scrypt password-based key derivation
- Random salt generated for every encrypted file
- Random nonce generated for every encryption operation
- Password confirmation during encryption
- Secure file authentication and tamper detection
- CLI and Tkinter GUI
- Overwrite protection
- Optional deletion of the original file
- Separate encrypted and decrypted output directories
- Automated tests using Pytest
- Standalone Windows executable using PyInstaller

## How It Works

For every encryption operation:

1. A random 16-byte salt is generated.
2. Scrypt derives a 256-bit AES key from the password and salt.
3. A random 12-byte nonce is generated.
4. AES-256-GCM encrypts the file.
5. The salt, nonce, ciphertext, and authentication tag are written to the encrypted file.

The encrypted file format is:

```text
[ Salt (16 bytes) ][ Nonce (12 bytes) ][ Ciphertext + Authentication Tag ]
```

Because AES-GCM provides authentication, modifying the encrypted file causes decryption to fail.

## Project Structure

```text
Vault/
├── crypto_core.py
├── file_operations.py
├── vault.py
├── gui.py
├── tests/
│   └── test_crypto.py
├── Encrypted_Files/
├── Decrypted_Files/
├── Sample_Files/
├── requirements.txt
├── README.md
└── .gitignore
```

| File | Purpose |
|---|---|
| `crypto_core.py` | Cryptographic operations |
| `file_operations.py` | File encryption/decryption logic |
| `vault.py` | Command-line interface |
| `gui.py` | Tkinter graphical interface |
| `tests/test_crypto.py` | Automated cryptographic tests |

The CLI and GUI both use the same backend encryption functions.

## Requirements

- Python 3.10+
- `cryptography`
- `pytest` for testing

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the CLI

```bash
python vault.py
```

For available options:

```bash
python vault.py --help
```

The CLI supports encryption, decryption, password confirmation, overwrite control, and optional deletion of the original file.

## Running the GUI

```bash
python gui.py
```

The GUI provides file selection, password input, encryption, decryption, overwrite control, delete-original control, status messages, and error handling.

## Security Design

### AES-256-GCM

Vault uses AES-GCM with a 256-bit key.

AES-GCM provides:

- **Confidentiality** — the original file contents cannot be read without the key.
- **Integrity/authentication** — unauthorized modifications are detected during decryption.

### Scrypt

Passwords are not used directly as AES keys. Vault uses Scrypt to derive a 256-bit key.

Current parameters:

```text
N = 2^14
r = 8
p = 1
```

Each encrypted file receives its own random salt.

### Random Nonces

A fresh 12-byte nonce is generated for every encryption operation. Nonce reuse with AES-GCM must be avoided.

## Error Handling

Vault handles common failure cases including:

- Missing files
- Existing output files
- Incorrect passwords
- Tampered encrypted files
- Invalid encrypted file data
- Permission and filesystem errors

An incorrect password or modified ciphertext results in authentication failure.

## Testing

Tests are located in:

```text
tests/test_crypto.py
```

Run the test suite:

```bash
python -m pytest
```

Current tests cover:

- Successful encryption/decryption round trip
- Incorrect password detection
- Tampered ciphertext detection

## Building the Windows Executable

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the executable:

```bash
pyinstaller --onefile --windowed --name Vault gui.py
```

The executable will be generated at:

```text
dist/Vault.exe
```

## GitHub Releases

The Windows executable is best distributed through **GitHub Releases** rather than committed directly to the source repository.

A release can contain:

```text
Vault-Windows-x64.exe
```

while the repository contains the source code and project files.

Example workflow:

1. Create a Git tag such as `v1.0.0`.
2. Create a GitHub Release from that tag.
3. Attach the Windows executable.
4. Add release notes.

## Development Workflow

```bash
git clone <repository-url>
cd Vault

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
```

Run tests:

```bash
python -m pytest
```

Run the GUI:

```bash
python gui.py
```

Run the CLI:

```bash
python vault.py
```

## Design Philosophy

Vault demonstrates how a small security-focused application can be separated into layers:

```text
             ┌─────────────────┐
             │       GUI       │
             │     gui.py      │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ File Operations │
             │file_operations.py│
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Cryptographic   │
             │     Core        │
             │ crypto_core.py  │
             └─────────────────┘

             ┌─────────────────┐
             │       CLI       │
             │    vault.py     │
             └────────┬────────┘
                      │
                      └──────────► File Operations
```

The cryptographic implementation is kept separate from the user interfaces so that both the CLI and GUI use the same encryption backend.

## Limitations

Vault is primarily an educational and portfolio project and has not undergone an independent security audit.

Important considerations:

- Password strength directly affects security.
- The current Scrypt parameters may not suit every threat model.
- File metadata such as filenames and filesystem timestamps may remain exposed.
- Deleting an original file does not guarantee secure erasure from storage.
- For highly sensitive data, professionally audited encryption software should be preferred.

## Future Improvements

Potential improvements include:

- Stronger/configurable Scrypt parameters
- Password strength estimation
- Drag-and-drop file support
- Directory encryption
- Progress indicators for large files
- Secure temporary-file handling
- Custom application icon and metadata
- Automated Windows builds using GitHub Actions
- More extensive test coverage
- Support for additional platforms

## License

This project can be distributed under the license specified in the repository.

If the repository uses the MIT License, see the `LICENSE` file for the complete license text.

## Author

**Pawan Manigandan**

Mechanical Engineering undergraduate interested in software engineering, cybersecurity, computational engineering, photography, and filmmaking.
