# ["vault", "packages.vault", ["vault"]]
# Made By OusmBlueNinja
import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64

# Global variables
key = None
passwords = []

def initialize_vault():
    global key

    print("Welcome to the Vault!")

    master_password = getpass.getpass("Enter your master password: ")
    salt = b'some_salt_here'  # Replace with a secure salt value

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,  # Adjust the number of iterations as needed for security
        salt=salt,
        length=32  # Use a fixed key length (256 bits)
    )

    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    print("Vault initialized successfully.")

def save_vault():
    global key, passwords
    if key is None:
        print("You must log in first to access the vault.")
        return

    cipher_suite = Fernet(key)
    encrypted_passwords = [cipher_suite.encrypt(password.encode()) for password in passwords]

    with open("vault.txt", "wb") as file:
        for encrypted_password in encrypted_passwords:
            file.write(encrypted_password + b'\n')

def load_vault():
    global key, passwords
    if key is None:
        print("You must log in first to access the vault.")
        return

    try:
        with open("vault.txt", "rb") as file:
            lines = file.read().splitlines()
            cipher_suite = Fernet(key)
            passwords = [cipher_suite.decrypt(line).decode() for line in lines]
    except FileNotFoundError:
        passwords = []

def vault_add(password):
    global key, passwords
    if key is None:
        print("You must log in first to access the vault.")
        return

    passwords.append(password)
    print("Password added to the vault.")

def vault_retrieve():
    global key, passwords
    if key is None:
        print("You must log in first to access the vault.")
        return

    for i, password in enumerate(passwords):
        print(f"Password {i + 1}: {password}")

def vault(command: list):
    if len(command) < 1:
        print("Usage: vault [login|add|retrieve|save|load]")
        return

    action = command[0].lower()

    if action == "login":
        initialize_vault()
    elif action == "add" and len(command) == 2:
        password = command[1]
        vault_add(password)
    elif action == "retrieve":
        vault_retrieve()
    elif action == "save":
        save_vault()
        print("Vault saved.")
    elif action == "load":
        load_vault()
        print("Vault loaded.")
    else:
        print("Invalid action or arguments. Usage: vault [login|add|retrieve|save|load]")

# Example usage:
# vault ["login"]
# vault ["add", "secretpassword"]
# vault ["retrieve"]
# vault ["save"]
# vault ["load"]
