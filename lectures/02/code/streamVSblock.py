#!/usr/local/bin/python3

########## Stream Cipher ##########

from Crypto.Cipher import Salsa20

key = b'secret'
nonce = b'nonce'

# the key and nonce must be stretched
key = (key * 6)[:32]
nonce = (nonce * 2)[:8]

plaintext = b'Attack at dawn'
cipher = Salsa20.new(key, nonce)
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

plaintext = b'Attack at dusk'
cipher = Salsa20.new(key, nonce)
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

######## Block Cipher ###########

from Crypto.Cipher import AES

key = b'secret'
# the key must be stretched to 128 bits
key = (key * 3)[:16]

def _str_to_bytes(data):
    u_type = type(b''.decode('utf8'))
    if isinstance(data, u_type):
        return data.encode('utf8')
    return data

BS = 16
# the plaintext must be padded
def _pad(s):
        return s + (BS - len(s) % BS) * _str_to_bytes(chr(BS - len(s) % BS))
# and the ciphertext unpadded
def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

plaintext = b'Attack at dawn'
p = _pad(plaintext)
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(p)
print(ciphertext)

plaintext = b'Attack at dusk'
p = _pad(plaintext)
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(p)
print(ciphertext)