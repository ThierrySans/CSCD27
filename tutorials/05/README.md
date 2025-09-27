---
layout: default
permalink: /tutorials/05/
---

# Symmetric Key Exchange

Let's assume that n participants wants to talk to each other over the network. 

In the first scenario, we distribute (over a physical channel) keys to each participants so that each pair of two participants have a unique shared key to talk to each other (naive key distribution in the course slides).

1. How many keys each participant will receive individually?
2. How many keys will be distributed in total?

# Perfect Forward Secrecy

3. Alice and Bob are using GPG to exchange encrypted and signed message. Explain why GPG does not ensure Perfect-Forward Secrecy?
4. Explain how Diffie-Hellman ensures Perfect-Forward Secrecy?

# TLS 1.3 and the Public Key Infrastructure

TLS 1.3 has only two rounds: 

- *A* -> *B*: *ecdhA*
- ​*B* -> *A*: *ecdhB*, *[certB, sign(H(ecdhA || ecdhB || certB))]k*

5. What are *ecdhA* and *ecdhB*?
6. When Alice's receives the message from Bob, what does she need to compute and verify? 
7. Why Mallory cannot do a replay attack on Bob's response? 
8. In TLS/SSL, how does Alice's browser trust a certificate supplied by Bob's website? 
9. Describe how a man-in-the-middle attack could succeed on TLS/SSL?
10. In this version of the protocol, why does not Alice sign any message so that Bob can check her identity?
​