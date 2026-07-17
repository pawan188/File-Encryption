import pytest
import os

from cryptography.exceptions import InvalidTag
from crypto_core import encrypt_bytes, decrypt_bytes

def test_round_trip():
    plaintext = b"Hello, Vault!"
    password = "correct_password"

    salt, nonce, ciphertext = encrypt_bytes(plaintext, password)
    decrypted = decrypt_bytes(ciphertext, password, salt, nonce)

    assert decrypted == plaintext


def test_decrypt_with_wrong_password():
    plaintext = b"Hello, Vault!"
    password = "correct_password"
    wrong_password = "incorrect_password"

    salt, nonce, ciphertext = encrypt_bytes(plaintext, password)

    with pytest.raises(InvalidTag):
        decrypt_bytes(ciphertext, wrong_password, salt, nonce)

def test_tampered_ciphertext():
    plaintext = b"Hello, Vault!"
    password = "correct_password"

    salt, nonce, ciphertext = encrypt_bytes(plaintext, password)
    tampered = bytearray(ciphertext)
    tampered[0] ^= 1 
    tampered = bytes(tampered)

    with pytest.raises(InvalidTag):
        decrypt_bytes(tampered, password, salt, nonce)

def test_empty_plaintext():
    plaintext = b""
    password = "correct_password"

    salt, nonce, ciphertext = encrypt_bytes(plaintext, password)
    decrypted = decrypt_bytes(ciphertext, password, salt, nonce)

    assert decrypted == plaintext

def test_random_binary_data():
    plaintext = os.urandom(4096)
    password = "correct_password"

    salt, nonce, ciphertext = encrypt_bytes(plaintext, password)
    decrypted = decrypt_bytes(ciphertext, password, salt, nonce)

    assert decrypted == plaintext