---
layout: default
permalink: /tutorials/05/
---

# Asymmetric Cryptography

1. Alice wishes to send a signed and confidential message to Bob using public-key cryptography, such as a GPG implementation. Which of the following is correct: (choose 1)

- Alice signs with Bob's public key, and encrypts with her private key.
- Alice signs with her private key and encrypts with Bob's public key.
- Alice signs with her private key and encrypts with Bob's private key.
- Alice signs with Bob's private key and encrypts with Bob's public key.
- Alice signs with her private key and encrypts with her private key.

## Public-key protocol

Take a look at the simplified version of the *Needham-Shroeder* public-key protocol seen in class. This protocol tries to achieve two goals: 1) making sure that one is talking to the right person (authentication) and 2) exchanging a symmetric session key. 

2. Why is Alice sending the nonce *Na* to Bob? If she does not, can you show how an attacker could compromised either of both goals? 

3. Why is Bob sending the none *Nb* to Alice? If he does not, can you show how an attacker could compromised either of both goals? 

4. Despite the double-challenge protocol, there is man-in-the-middle attack on the Needham-Shroeder protocol. Describe that attack and its fix. 

## Trust models

5. In GPG, what are the two ways to trust a GPG key? 

6. Describe how a man-in-the-middle attack could succeed on GPG?

7. In TLS/SSL, how does your browser trust a certificate supplied by a website? 

8. Describe how a man-in-the-middle attack could succeed on TLS/SSL?
