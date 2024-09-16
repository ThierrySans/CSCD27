---
layout: default
permalink: /tutorials/04/
---

# Scale of key robustness

1. Imagine a ciphertext encrypted with a 128 bits key and let's presume we have a very powerful computer that can brute force 10^12 keys per second.

    - How many keys in total?
    - How many keys per year can we compute?
    - How long would it take to compute all keys?
    - How many computers would you need to crack all keys within a day?

2. Same question with 256 bits? 

# Authenticated Encryption

Let us assume that Alice and Bob have exchange a session *k*. Alice sends a message *m* to Bob encrypted with the key *k* AES with an Authenticated Encryption mode (encrypt-then-mac method). 

3. How does Alice encrypts *m* with the key *k*? 

4. What does she sent over to Bob? 

5. How does bob decrypt that ciphertext while making sure that Mallory has not tampered with the message? 

# Asymmetric Cryptography

Let us assume that Alice has a asymmetric key pair *(ksA, KpA)* and Bob has an asymmetric key pair (ksB, KpB) and thet they each others public key. To simplify the exercise, let us assumed that we can use these asymmetric keys to encrypt and decrypt any message of any length easily (though this is not true in practice). 

6. Alice wishes to send a signed but not encrypted message to Bob, how does she generates the signature *s* and what does she send over to Bob? 

7. How does Bob verifies the signature? 

8. Alice wishes to send an encrypted and signed message to Bob, how does she "sign-then-encrypt" the message and what does she send over to Bob? 

9. How does Bob extract the message and verifies the signature? 