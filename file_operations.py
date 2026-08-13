import os
from crypto_core import encrypt_bytes, decrypt_bytes

OUTPUT_DIR_EN = "Encrypted_Files"
OUTPUT_DIR_DE = "Decrypted_Files"
SALT_SIZE = 16
NONCE_SIZE = 12

def encrypt_file(file_path: str, password: str, overwrite: bool = False, delete_original: bool = False) -> str:
    os.makedirs(OUTPUT_DIR_EN, exist_ok=True)
    
    with open(file_path, "rb") as f:
        data = f.read()

    filename = os.path.basename(file_path)     
    salt, nonce, ciphertext = encrypt_bytes(data, password)

    output_path = os.path.join(OUTPUT_DIR_EN, filename + ".enc")

    if not overwrite and os.path.exists(output_path):
        raise FileExistsError(output_path)

    with open(output_path, "wb") as f:
        f.write(salt)
        f.write(nonce)
        f.write(ciphertext)

    if delete_original:
        os.remove(file_path)

    return output_path

def decrypt_file(file_path: str, password: str, overwrite: bool = False, delete_original: bool = False) -> str:
    os.makedirs(OUTPUT_DIR_DE, exist_ok=True)
    
    with open(file_path, "rb") as f:
        salt = f.read(SALT_SIZE)
        nonce = f.read(NONCE_SIZE)
        ciphertext = f.read()

    if len(salt) != SALT_SIZE or len(nonce) != NONCE_SIZE:
        raise ValueError("File is too small or corrupted to be a valid .enc file.")

    filename = os.path.basename(file_path).removesuffix(".enc")
    plaintext = decrypt_bytes(ciphertext, password, salt, nonce)

    output_path = os.path.join(OUTPUT_DIR_DE, filename)

    if not overwrite and os.path.exists(output_path):
        raise FileExistsError(output_path)

    with open(output_path, "wb") as f:
        f.write(plaintext)

    if delete_original:
        os.remove(file_path)

    return output_path