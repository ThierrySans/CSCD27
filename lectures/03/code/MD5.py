#!/usr/local/bin/python3
from Crypto.Hash import MD5

plaintext = b'Attack at dawn'

h = MD5.new(plaintext)
print (h.hexdigest())
