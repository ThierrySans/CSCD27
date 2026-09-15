#!/usr/local/bin/python3

plaintext = b'Attack at dawn'

from Crypto.PublicKey import RSA

# generate pair of keys (and export them)
rsa_key = RSA.generate(2048)
privkey = rsa_key.exportKey(pkcs=8)
pubkey = rsa_key.publickey().export_key()

from Crypto.Cipher import PKCS1_v1_5

# encryption
k = RSA.importKey(pubkey)
cipher = PKCS1_v1_5.new(k)
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

# decryption
k = RSA.importKey(privkey)
cipher = PKCS1_v1_5.new(k)
d = cipher.decrypt(ciphertext,"thisisarandomsentinelmessage")
print(d)