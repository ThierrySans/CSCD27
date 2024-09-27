---
layout: default
permalink: /tutorials/05/
---

# Symmetric Key Exchange

Let's assume that n participants wants to talk to each other over the network. 

In the first scenario, we distribute (over a physical channel) keys to each participants so that each pair of two participants have a unique shared key to talk to each other (naive key distribution in the course slides).

1. How many keys each participant will receive individually?
2. How many keys will be distributed in total?

In the second scenario, we use a Key Distribution Center that will distribute session keys to participants when they need to communicate between each other. In this setup, we distribute the

3. How many keys will be distributed to the Key Distribution Center? 
4. How many keys each participant will receive individually?
5. How many keys will be distributed in total? 

# Perfect Forward Secrecy

6. Explain why the Key Distribution Center example given above does not ensure Perfect-Forward Secrecy?
7. Alice and Bob are using GPG to exchange encrypted and signed message. Explain why GPG does not ensure Perfect-Forward Secrecy?
8. Explain how Diffie-Hellman ensures Perfect-Forward Secrecy?

# TLS 1.3 and the Public Key Infrastructure

TLS 1.3 has only two rounds: 

- A -> B: $nA$, $ecdhA$
- ​B -> A: $nB$, $ecdhB$, $[certB, sign(H(nA || nB || ecdhA || ecdhB || certB))]k$

9. What are $ecdhA$ and $ecdhB$?
10. When Alice's receives the message from Bob, what does she need to compute and verify? 
11. Why Mallory cannot do a replay attack on Bob's response? 
12. In TLS/SSL, how does Alice's browser trust a certificate supplied by Bob's website? 
13. Describe how a man-in-the-middle attack could succeed on TLS/SSL?
​