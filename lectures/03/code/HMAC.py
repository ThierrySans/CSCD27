#!/usr/local/bin/python3
from Crypto.Hash import HMAC

key = b'secret'
plaintext = b'Attack at dawn'

h = HMAC.new(key)
h.update(plaintext)
print(h.hexdigest())