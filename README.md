# Password Generator with Encryption

This is a simple Python application for generating, encrypting, and decrypting passwords. It uses the `cryptography` library for encryption and decryption with the **Fernet** algorithm.

## Requirements

- Python 3.x
- cryptography library (install with `pip install cryptography`)

## Features

- **Generate random passwords**: The program generates passwords with random characters, including letters, digits, and punctuation.
- **Encrypt passwords**: The program encrypts the generated passwords using the **Fernet** encryption method.
- **Decrypt passwords**: The program allows decrypting passwords back to their original form.
- **Key management**: If the encryption key is missing, it will be automatically generated and saved in a file (`key.key`). If the key is already present, it will be used for encryption and decryption.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/LLR1/Python-Password_Generator.git
    cd Python-Password_Generator
    ```

2. Install the necessary dependencies:

    ```bash
    pip install cryptography
    ```

## Usage

1. Run the script to generate, encrypt, and decrypt a password:

    ```bash
    python password_generator.py
    ```

2. The program will ask for the desired password length and then show:
   - The generated password.
   - The encrypted password.
   - The decrypted password.

## How It Works

- **Password Generation**: The program uses the `secrets` and `string` modules to generate random passwords that include uppercase and lowercase letters, digits, and punctuation characters.
- **Encryption**: The password is encrypted using the **Fernet** symmetric encryption algorithm from the `cryptography` library.
- **Decryption**: The program decrypts the password back to its original form using the same encryption key that was used for encryption.
- **Key Management**: 
  - If the `key.key` file is missing, a new key is generated and saved to the file.
  - If the `key.key` file already exists, it is used to encrypt and decrypt passwords.

## Key Management

- If the `key.key` file is missing, the program will generate a new encryption key and save it to `key.key`.
- If the key file already exists, the program will load the existing key to use for encryption and decryption.
- For better security, consider storing the key in an environment variable instead of the file system (especially for production environments).

## Example Output

```bash
Welcome to the Password Generator with Encryption!
Enter the desired password length: 16
Generated password: Y#5gZ9b8%Nq7Lk@F
Encrypted password: b'gAAAAABlY... (encrypted string)'
Decrypted password: Y#5gZ9b8%Nq7Lk@F


