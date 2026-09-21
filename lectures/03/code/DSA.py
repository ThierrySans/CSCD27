#!/usr/local/bin/python3

plaintext = b'Attack at dawn'

from Crypto.PublicKey import RSA

# generate pair of keys (and export them)
rsa_key = RSA.generate(2048)
privkey = rsa_key.exportKey(pkcs=8)
pubkey = rsa_key.publickey().export_key()

from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

# signature
k = RSA.importKey(privkey)
signer = PKCS1_v1_5.new(k)
digest = SHA256.new(plaintext)
s = signer.sign(digest)

print(s)

# verification
k = RSA.importKey(pubkey)
signer = PKCS1_v1_5.new(k)
digest = SHA256.new(plaintext)
print(signer.verify(digest,s))
