import os
import argparse
from getpass import getpass
from crypto_core import encrypt_bytes, decrypt_bytes
from cryptography.exceptions import InvalidTag


OUTPUT_DIR_EN = "Encrypted_Files"
OUTPUT_DIR_DE = "Decrypted_Files"
SALT_SIZE = 16
NONCE_SIZE = 12

def encrypt_file(file_path: str, password: str, output_dir: str, overwrite: bool = False, delete_original: bool = False) -> str:
    with open(file_path, "rb") as f:
        data = f.read()

    filename = os.path.basename(file_path)     
    salt, nonce, ciphertext = encrypt_bytes(data, password)

    output_path = os.path.join(output_dir, filename + ".enc")

    if not overwrite and os.path.exists(output_path):
        raise FileExistsError(output_path)

    with open(output_path, "wb") as f:
        f.write(salt)
        f.write(nonce)
        f.write(ciphertext)

    if delete_original:
        try:
            os.remove(file_path)
        except OSError as e:
            print(f"Warning: Encryption succeeded, but the original file could not be deleted: {e}")

    return output_path

def decrypt_file(file_path: str, password: str, output_dir: str, overwrite: bool = False, delete_original: bool = False) -> str:
    with open(file_path, "rb") as f:
        salt = f.read(SALT_SIZE)
        nonce = f.read(NONCE_SIZE)
        ciphertext = f.read()

    if len(salt) != SALT_SIZE or len(nonce) != NONCE_SIZE:
        raise ValueError("File is too small or corrupted to be a valid .enc file.")

    filename = os.path.basename(file_path).removesuffix(".enc")
    plaintext = decrypt_bytes(ciphertext, password, salt, nonce)

    output_path = os.path.join(output_dir, filename)

    if not overwrite and os.path.exists(output_path):
        raise FileExistsError(output_path)

    with open(output_path, "wb") as f:
        f.write(plaintext)

    if delete_original:
        try:
            os.remove(file_path)
        except OSError as e:
            print(f"Warning: Decryption succeeded, but the original file could not be deleted: {e}")
    
    return output_path

def main():

    parser = argparse.ArgumentParser(description="Encrypt or decrypt files using AES-256-GCM.")
    parser.add_argument("operation", choices=["encrypt", "decrypt"], help="Operation to perform: encrypt or decrypt.")
    parser.add_argument("file", help="Path to the input file.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite the output file if it already exists.")
    parser.add_argument("--delete-original", action="store_true", help="Delete the original file after successful encryption/decryption.")
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f"Error: '{args.file}' does not exist.")
        return

    if args.operation == "encrypt":

        os.makedirs(OUTPUT_DIR_EN, exist_ok=True)

        password = getpass("Enter password: ")
        password_confirm = getpass("Re-enter password: ")

        if password != password_confirm:
            print("Passwords do not match. Exiting.")
            return
        try:
            output_path = encrypt_file(args.file, password, OUTPUT_DIR_EN, overwrite=args.overwrite, delete_original=args.delete_original)
            print(f"Encrypted file saved to: {output_path}")
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
        except FileExistsError as fee:
            print(f"Error: '{fee}' already exists.\nUse --overwrite to replace it.")
        except Exception as e:
            print(f"Unexpected error: {e}")
        
    else: # args.operation == "decrypt"

        os.makedirs(OUTPUT_DIR_DE, exist_ok=True)
        if not args.file.endswith(".enc"):
            print("Error: Input file must have a '.enc' extension.")
            return
        
        password = getpass("Enter password: ")
        try:
            output_path = decrypt_file(args.file, password, OUTPUT_DIR_DE, overwrite=args.overwrite, delete_original=args.delete_original)
            print(f"Decrypted file saved to: {output_path}")
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
        except InvalidTag:
            print("Error: Decryption failed. Incorrect password or corrupted encrypted file.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except FileExistsError as fee:
            print(f"Error: '{fee}' already exists.\nUse --overwrite to replace it.")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()