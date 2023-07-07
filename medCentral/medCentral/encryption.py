from cryptography.fernet import Fernet
from django.conf import settings

class EncryptionManager:
    @staticmethod
    def encrypt(data):
        key = settings.ENCRYPTION_KEY.encode()
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(data.encode())
        return cipher_text

    @staticmethod
    def decrypt(data):
        key = settings.ENCRYPTION_KEY.encode()
        cipher_suite = Fernet(key)
        plain_text = cipher_suite.decrypt(data.encode())
        return plain_text.decode()
