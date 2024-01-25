#!/usr/local/bin/python3
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter

key = b'secret'
plaintext = b'Attack at dawn'

# AES blocks are 16 bytes
BS = 16
# the key must be stretched
key = (key * 3)[:16]

def _str_to_bytes(data):
    u_type = type(b''.decode('utf8'))
    if isinstance(data, u_type):
        return data.encode('utf8')
    return data

# the plaintext must be padded
def _pad(s):
        return s + (BS - len(s) % BS) * _str_to_bytes(chr(BS - len(s) % BS))
# and the ciphertext unpadded
def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


### AES ECB mode

# encryption
p = _pad(plaintext)
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(p)
print(ciphertext)

# decryption
cipher = AES.new(key, AES.MODE_ECB)
d = _unpad(cipher.decrypt(ciphertext))
print(d)

### AES CBC mode

# encryption
p = _pad(plaintext)
iv = Random.new().read(AES.block_size);
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = (iv + cipher.encrypt(p))
print(ciphertext)

# decryption
iv = ciphertext[:16]
c = ciphertext[16:]
cipher = AES.new(key, AES.MODE_CBC,iv)
d = _unpad(cipher.decrypt(c))
print(d)

### AES CTR mode

# encryption
p = _pad(plaintext)
ctr = Counter.new(128)
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
ciphertext = cipher.encrypt(p)
print(ciphertext)

# decryption
ctr = Counter.new(128)
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
d = _unpad(cipher.decrypt(ciphertext))
print(d)
