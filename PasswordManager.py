import getpass
import hashlib
from cryptography.fernet import Fernet, InvalidToken
import string
import random

class PwMgr:
    def Encrypt(password:str) -> str :
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        salt = PwMgr.rand_salt(random.randint(1, 100))
        salted_password = hashlib.sha256((password + salt).encode()).hexdigest()
        key = Fernet.generate_key()
        print("key:\t\t\t", key.decode('utf-8'))
        cipher_suite = Fernet(key)
        encrypted_password = cipher_suite.encrypt(password.encode()).decode()
        return encrypted_password
    
    def Decrypt(sha_password:str, key:str) -> str:
        try:
            cipher_suite = Fernet(key)
        except ValueError:
            print(f"[ValueError] Key len != 32")
            return None
        try:
            decrypted_password = cipher_suite.decrypt(sha_password.encode()).decode()
        except InvalidToken:
            print("token no valid")
            return None
        return decrypted_password

    def rand_salt(word_len:int) -> str:
        lowercase_letters = string.ascii_lowercase
        word = ''
        while len(word) != word_len:
            word += random.choice(lowercase_letters)
        return word
    

if __name__ == "__main__":
    password = input('incert password:\t ')
    password = PwMgr.Encrypt(password)
    print('encrypt password:\t', password)
    encrypt_password = input('incert encrypt password: ')
    key = input('incert key:\t\t ')
    password = PwMgr.Decrypt(encrypt_password, key)
    print('password\t\t', password)
