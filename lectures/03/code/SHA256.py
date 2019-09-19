#!/usr/local/bin/python3
from Crypto.Hash import SHA256

plaintext = b'Attack at dawn'

h = SHA256.new(plaintext)
print(h.hexdigest())
