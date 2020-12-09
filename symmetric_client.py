# symmetric_client.py

import os, requests
from cryptography.fernet import Fernet

SECRET_KEY = os.environ[b"SECRET_KEY"]
my_cipher = Fernet(SECRET_KEY)

def get_secret_message():
    response = requests.get("http://127.0.0.1:5683")

    decrypt_message = my_cipher.decrypt(response.content)
    print(f'The codeword is: {decrypt_message}')

if __name__ = '__main__':
    get_secret_message()
