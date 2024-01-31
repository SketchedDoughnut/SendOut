from cryptography.fernet import Fernet # Code import end to run bot program
import os

#Encrypt test file and print it
key = Fernet.generate_key()
fernet = Fernet(key)
f = open('/workspaces/SendOut/Online Bot/Master/log.txt', 'rb')
original = f.read()
f.close()
encrypted = fernet.encrypt(original)
decrypted = fernet.decrypt(encrypted)
print(original)
print(encrypted)
print(decrypted)
os.system(f'python test.py')
