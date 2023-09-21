# ["vault", "packages.vault", ["vault"]]
# Made By OusmBlueNinja
import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# Initialize the Fernet symmetric key
key = None
cipher_suite = None

def initialize_vault():
    global key, cipher_suite

    print("Welcome to the Vault!")

    while True:
        master_password = getpass.getpass("Enter your master password: ")

        salt = b'some_salt_here'  # Replace with a secure salt value
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=100000,  # Adjust the number of iterations as needed for security
            salt=salt,
        )

        key = Fernet(base64.urlsafe_b64encode(kdf.derive(master_password.encode())))
        cipher_suite = Fernet(key)

        print("Vault initialized successfully.")
        break

# Dictionary to store encrypted passwords (service as key, encrypted password as value)
passwords = {}

def vault(command: list):
    if len(command) != 1:
        print("Usage: vault login")
        return

    action = command[0].lower()

    if action == "login":
        initialize_vault()

    elif action == "add":
        if key is None:
            print("You must log in first to access the vault.")
            return

        service = input("Enter the service or website name: ")
        password = getpass.getpass("Enter the password: ")

        # Encrypt the password before storing it
        encrypted_password = cipher_suite.encrypt(password.encode())

        passwords[service] = encrypted_password
        print(f"Password for {service} added and encrypted.")

    elif action == "retrieve":
        if key is None:
            print("You must log in first to access the vault.")
            return

        service = input("Enter the service or website name: ")

        if service in passwords:
            # Decrypt and display the password
            decrypted_password = cipher_suite.decrypt(passwords[service]).decode()
            print(f"Password for {service}: {decrypted_password}")
        else:
            print(f"No password found for {service}.")

    else:
        print("Invalid action. Use 'login', 'add', or 'retrieve'.")

