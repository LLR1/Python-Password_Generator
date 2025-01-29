import os
import secrets
import string
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    try:
        with open("key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Key file not found! Please generate the key first.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while loading the key: {e}")
        exit(1)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

if __name__ == "__main__":
    # Generate or load the encryption key
    if not os.path.exists("key.key"):
        print("Key file not found, generating a new key...")
        key = generate_key()
    else:
        key = load_key()

    print("Welcome to the Password Generator with Encryption!")
    
    # Input validation for password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length should be a positive integer. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    password = generate_password(length)

    print(f"Generated password: {password}")

    encrypted_password = encrypt_password(password, key)
    print(f"Encrypted password: {encrypted_password}")

    decrypted_password = decrypt_password(encrypted_password, key)
    print(f"Decrypted password: {decrypted_password}")

