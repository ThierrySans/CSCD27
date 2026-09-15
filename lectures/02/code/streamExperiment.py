from Crypto.Cipher import Salsa20

key = b'secret'
nonce = b'nonce'
key = (key * 6)[:32]
nonce = (nonce * 2)[:8]

def xor(byte_string1, byte_string2):
    return bytes([a ^ b for a, b in zip(byte_string1, byte_string2)])

def encrypt(plaintext):
    cipher = Salsa20.new(key, nonce)
    return cipher.encrypt(plaintext)

def decrypt(ciphertext):
    cipher = Salsa20.new(key, nonce)
    return cipher.decrypt(ciphertext)

plaintext = b'Attack at dawn'
ciphertext = encrypt(plaintext)
print(ciphertext)

print(xor(ciphertext, xor(plaintext, ciphertext)))

plaintext2 = b'Attack at dusk'
ciphertext2 = encrypt(plaintext2)
print(ciphertext2)

print(xor(plaintext, plaintext2))
print(xor(ciphertext, ciphertext2))

print(xor(plaintext, xor(ciphertext, ciphertext2)))