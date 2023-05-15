#!/usr/bin/env python

import os
import sys
from cryptography.fernet import Fernet

# Check the number of command-line arguments
if len(sys.argv) != 4:
    print("Usage: python crypto_tool.py <encrypt/decrypt> <input_file> <output_file>")
    sys.exit(1)

# Generate a random encryption key
key = Fernet.generate_key()

# Save the encryption key to a file for future use
with open('encryption_key.txt', 'wb') as key_file:
    key_file.write(key)

# Read the encryption key from the file
with open('encryption_key.txt', 'rb') as key_file:
    key = key_file.read()

# Create a Fernet cipher object
cipher = Fernet(key)

# Encrypt a file
def encrypt_file(input_file, output_file):
    with open(input_file, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open(output_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    os.remove(input_file)

# Decrypt a file
def decrypt_file(input_file, output_file):
    with open(input_file, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(output_file, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    os.remove(input_file)

# Retrieve command-line arguments
operation = sys.argv[1].lower()
input_file = sys.argv[2]
output_file = sys.argv[3]

# Perform the requested operation
if operation == 'encrypt':
    encrypt_file(input_file, output_file)
    print(f"File '{input_file}' encrypted and saved as '{output_file}'")
elif operation == 'decrypt':
    decrypt_file(input_file, output_file)
    print(f"File '{input_file}' decrypted and saved as '{output_file}'")
else:
    print("Invalid operation. Use 'encrypt' or 'decrypt'")
