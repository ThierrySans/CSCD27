#!/usr/local/bin/python3
from Crypto.Cipher import XOR

key = b'secret'
plaintext = b'Attack at dawn'

# encryption
cipher = XOR.new(key)
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

# decryption
cipher = XOR.new(key)
d = cipher.decrypt(ciphertext)
print(d)
