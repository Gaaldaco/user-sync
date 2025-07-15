import os
from cryptography.fernet import Fernet

fernet_key = os.getenv("FERNET_KEY", Fernet.generate_key())
fernet = Fernet(fernet_key)

def encrypt_data(data: str) -> str:
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(data: str) -> str:
    return fernet.decrypt(data.encode()).decode()
