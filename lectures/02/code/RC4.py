#!/usr/local/bin/python3
from Crypto.Cipher import ARC4

key = b'secret'
plaintext = b'Attack at dawn'

# encryption
cipher = ARC4.new(key)
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

# decryption
cipher = ARC4.new(key)
d = cipher.decrypt(ciphertext)
print(d)
