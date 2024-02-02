---
layout: default
permalink: /tutorials/05/
---

The goal of this tutorial is to fully understand the challenge `mini-tls-13`. 

# Authenticated Encryption

Let us assume that Alice and Bob have exchange a session *k*. Alice sends a message *m* to Bob encrypted with the key *k* AES with an Authenticated Encryption mode (encrypt-then-mac method). 

1. How does Alice encrypts *m* with the key *k*? 

2. What does she sent over to Bob? 

3. How does bob decrypt that ciphertext while making sure that Mallory has not tampered with the message? 

# Asymmetric Cryptography

Let us assume that Alice has a asymmetric key pair *(ksA, KpA)* and Bob has an asymmetric key pair (ksB, KpB) and thet they each others public key. To simplify the exercise, let us assumed that we can use these asymmetric keys to encrypt and decrypt any message of any length easily (though this is not true in practice). 

4. Alice wishes to send a signed but not encrypted message to Bob, how does she generates the signature *s* and what does she send over to Bob? 

5. How does Bob verifies the signature? 

6. Alice wishes to send an encrypted and signed message to Bob, how does she "sign-then-encrypt" the message and what does she send over to Bob? 

7. How does Bob extract the message and verifies the signature? 

## Key exchange

In practice, it is too slow to use public-key cryptography on large messages. One solution is to use public-key cryptography to exchange a public key but it is usually not recommend. 

8. Why is it better to exchange a session key using the Diffie-Hellman protocol rather than using public cryptography directly? 

## Public Key Infrastructure Trust model

9. In TLS/SSL, how does Alice's browser trust a certificate supplied by Bob's website? 

10. Describe how a man-in-the-middle attack could succeed on TLS/SSL?
