# Symmetric Cryptography

## Stream Cipher

Mallory has been able to hijack the communication made by the ATM machine inside the building of *University of Fail*. She notices that, every time somebody performs a transaction, the ATM sends some data to a server named `atm.bank-of-fail.com`. 

Mallory has found some information online about the communication protocol version 1.0 used by the bank. Each transaction contains the following information:

- an ATM ID (16 bytes)
- customer's bank account (16 bytes)
- the transaction ID (8 bytes)
- the transaction date and time (8 bytes)
- the transaction amount (4 bytes)

Unfortunately, Mallory is not able to read those transactions since they are [XOR-encrypted](https://pycryptodome.readthedocs.io/en/latest/src/util/util.html#crypto-util-strxor-module) using a 128 bits secret key shared between the ATM and the bank. 

1. Could Mallory brute-force the shared key? 

2. Mallory goes to the ATM machine to withdraw some money. Then she gets a receipts from the ATM with the transaction ID and the date and time. Now, she knows all values of the plaintext except the ATM ID. Could she crack the key with this information? 

3. The bank is now using a proper stream cipher `Ek(m) = Dk(m) = m + RNG(k || seed)` with another 128 bits key and the ATM ID used as nonce (that Mallory still does not know). Could Mallory crack the key using the same approach as question 2? 

4. Instead of using the ATM ID, the bank is now using the transaction ID (repeated twice) as nonce (but still using the same key). The transaction ID is unique to each transaction. Could Mallory crack the key using the same approach as question 3?

## Block Cipher (and Block Cipher modes)

The bank is now using [AES in ECB (Electronic Code Book) mode](https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#ecb-mode) with an 256 bits key.

1. Could Mallory brute-force the shared key? 

2. Could Mallory use a known-plaintext attack? 

3. When analyzing different ciphertexts, Mallory finds out some intersting correlations. Could you explain each of them?

    - each ciphertext is 64 bytes but the plaintext is supposed to be 52 bytes, why? 
    - all ciphertexts have the same first 16 bytes [0..14], why?
    - some (but not all) ciphertexts have the same second set of 16 bytes [15..31], why?
    - there are no two ciphertexts that have the same third set of 16 bytes [32..47]
    - some (but not all) ciphertexts have the same last set of 16 bytes [48..64], why?

4. Now, the bank is using [AES in CBC mode (Cipher Block Chaining)](https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode) mode with the same nonce for each transaction. Would Mallory be able to do the same observation as in 3?

