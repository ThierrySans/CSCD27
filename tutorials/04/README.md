---
layout: default
permalink: /tutorials/04/
---

# Symmetric Cryptography

## Stream Cipher

1. We implement a basic stream cipher that combines (xor) a plaintext message (m) with a key (k) of the same length.

- How is the message encrypted and decrypted? Write down the equations.
- Considering a known-plaintext attack (1 instance), can you recover the key? If so, write down the equations.
- Considering a ciphertext-only attack (2 instances), what can you recover? If so, write down the equations and name the attack.

2. We use RC4 that uses a pseudo-random number generator RNG(s), s being the seed.

- How is the message encrypted and decrypted? Write down the equations.
- Considering the same known-plaintext attack as in question 1, can you recover the key?
- Considering the same ciphertext-only attack as in question 1, what can you recover?

3. What recommendation could you give to a software engineer who wants to use a stream cipher?

## Block Cipher (and Block Cipher modes)

4. We use AES 128 bits to encode a 128 bits message.

- Considering the same known-plaintext attack as considered previously, can you recover the key?
- Considering the same ciphertext-only attack as considered previously, what can you recover?

We use AES 128 bits to encrypt the following message (32 characters):

```
On Thursday, we attack Mallory!
```

Let's consider a chosen-plaintext attack where the attacker (Mallory) has chosen by luck the following message (16 characters):

```
 attack Mallory!
```

5. Considering that we use AES in ECB mode (Electronic Code Book), can the attacker ...

- recover the key?
- recover the first half of the message?
- recover the second half of the message?
- modify the message in an intelligible way using another chosen-plaintext?

6. Same questions but considering the use of the CBC mode (Cipher Block Chaining)

## Stream Cipher vs Block Cipher

7. What are the pros and cons of using Block cipher vs Stream cipher?

## Cryptographic hash function

8. List the 3 properties that a cryptographic hash function must exhibit to be considered secure (if you don't remember the name, give a brief description of the property):

9. Which hash property/ies does the birthday attack target?

10. When using a symmetric encryption algorithm with an n-bit key, an attacker can find the key in \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ tries in average. When using a secure-hash function with n-bit input and m-bit output, an attacker can find a collision in \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ in average.


## Symmetric Protocols

Take a look at the *Needham-Shroeder* symmetric protocol seen in class.

11. Why is Alice sending the nonce *Na* to the KDC? If she does not, can you show how an attacker could compromised the freshness of the session key *Kab*? Write down precisely the message exchanges between the different parties. 