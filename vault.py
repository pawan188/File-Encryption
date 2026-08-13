import os
import argparse
from getpass import getpass
from file_operations import encrypt_file, decrypt_file
from cryptography.exceptions import InvalidTag

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

        password = getpass("Enter password: ")
        password_confirm = getpass("Re-enter password: ")

        if password != password_confirm:
            print("Passwords do not match. Exiting.")
            return
        try:
            output_path = encrypt_file(args.file, password, overwrite=args.overwrite, delete_original=args.delete_original)
            print(f"Encrypted file saved to: {output_path}")
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
        except FileExistsError as fee:
            print(f"Error: '{fee}' already exists.\nUse --overwrite to replace it.")
        except Exception as e:
            print(f"Unexpected error: {e}")
        
    else: # args.operation == "decrypt"

        if not args.file.endswith(".enc"):
            print("Error: Input file must have a '.enc' extension.")
            return
        
        password = getpass("Enter password: ")
        try:
            output_path = decrypt_file(args.file, password, overwrite=args.overwrite, delete_original=args.delete_original)
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