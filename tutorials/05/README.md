---
layout: default
permalink: /tutorials/05/
---

# Cryptography Protocols

 Here some basic functions in our toolbox:
 
 Authenticated Encryption:
   - `k = genKey()` generate a symmetric key
   - `c = Enc(k, m)` encrypts a message `m` with the key `k` assuming `c` includes the ciphertext, the nonce and the MAC tag.
   - `m = Dec(k, c)` decrypts the payload `c` using `k` to get the plaintext `m` back. It raises an error if the MAC tag is not valid
 
Authenticated Encryption:
 - `(sKem, pKem) = genKem()` returns a pair (private and public) of EC keys for key exchange
 - `k=ECDH(sKem1, pKem2)=ECDH(sKem2, pKem1)` generates a key `k` by combining two key exchange pairs 
 
Digital Signature:
  - `(sSig, pSig) = genSig()` returns a pair (private and public) of EC keys for signature
  - `s = Sig(sSig, m)` generate the signature `s` by signing the message `m` with the private key `sSig`
  - `Ver(pSig, s, m)` verify the signature `s` correspond to the message `m` signed with the private key corresponding to `pSig`. 
  
## Synchronous Protocol: TLS 1.3 and the Public Key Infrastructure

TLS 1.3 has only two rounds: 

- *A* -> *B*: *pKemA*
- ​*B* -> *A*: *pKemB*, *Enc(k, CertB+ Sig(pKemA || pKemB || CertB))*

1. What are *pKemA* and *pKemB*? What are they used for? Are they long term of short term keys?
2. Explain what Alice must do and check after receiving 
3. How does Alice's browser trust a certificate supplied by Bob's website? What does she need to verify that certificate?
​4. Why Mallory cannot do a replay attack on Bob's response? 
5. Explain why TLS  ensures Perfect-Forward Secrecy?
6. Describe how a man-in-the-middle attack could succeed on TLS/SSL?
​7. In this version of the protocol, why does not Alice sign any message so that Bob can check her identity?

## Asynchronous Protocol: GPG

GPG uses two types of EC keys:
- a signature key `Sig` to sign messages
- a key exchange key `Kem` to exchange a symmetric encryption key and encrypt message

Assume that Alice is sending a GPG message to Bob:
- Alice has the GPG public key `(pSignA, pKemA)` and the corresponding GPG private Key `(sSignA, sKemA)`
- Bob has the GPG public key `(pSignB, pKemB)` and the corresponding GPG private Key `(sSignB, sKemB)`

1. Explain how Alice can sign her message `m` using GPG
2. Explain how Bob can verify that the message comes from Alice?
3. Explain how Alice can encrypt her message `m` using GPG
4. Explain how Bob can decrypt the message from Alice
5. Explain why GPG does not protect against replay attack.
6. Explain why GPG does not ensure Perfect-Forward Secrecy.