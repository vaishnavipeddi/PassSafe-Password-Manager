from Crypto.Cipher import AES
import base64

class Encryptor:
    def __init__(self, key):
        self.key = key.zfill(32)  

    def encrypt(self, plaintext):
        cipher = AES.new(self.key.encode(), AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
        return base64.b64encode(cipher.nonce + ciphertext).decode()

    def decrypt(self, encrypted_data):
        data = base64.b64decode(encrypted_data)
        nonce = data[:16]
        ciphertext = data[16:]
        cipher = AES.new(self.key.encode(), AES.MODE_EAX, nonce=nonce)
        return cipher.decrypt(ciphertext).decode()
