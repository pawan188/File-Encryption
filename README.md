# File Vault

A Python-based file encryption tool built using modern cryptographic practices. This project is being developed to understand password-based encryption, authenticated encryption, and secure software design.

## Features

- AES-256-GCM authenticated encryption
- Password-based key derivation using Scrypt
- Random salt generated for every encryption
- Random nonce generated for every encryption
- Modular cryptographic core

## Project Structure

```
file-vault/
│
├── crypto_core.py
├── vault.py
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
```

## Technologies

- Python 3
- cryptography
- pytest (coming soon)

## Current Progress

- [x] Scrypt key derivation
- [x] AES-256-GCM encryption
- [x] AES-256-GCM decryption
- [ ] Command-line interface
- [ ] File encryption & decryption
- [ ] Unit tests
- [ ] Streaming encryption
- [ ] Documentation

## Learning Objectives

This project focuses on understanding:

- Password-based key derivation
- Authenticated encryption (AEAD)
- Secure cryptographic design
- Python CLI application development

## Disclaimer

This project is intended for educational purposes. While it uses the `cryptography` library and follows modern cryptographic practices, it has not been independently audited and should not be used to protect highly sensitive or production data.