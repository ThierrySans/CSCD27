---
layout: default
permalink: /notes/symmetric-encryption/
---

## Building a secure channel over an insecure medium

Alice and Bob wants to exchange messages over the internet. Unfortunately, they are not the only one on the network and the internet is not secure by design. Mallory, an adversary also using the internet, is somehow able to eavesdrop or tamper with the messages send between Alice and Bob.   

If Alice and Bob want to keep on communicating on the internet, they will need to implement a *secure channel* over that insecure medium. The idea of a secure channel is that Alice and Bob will be able to send messages back and forth to each other while ensuring that:

1. no one else could eavesdrop these message (confidentiality), and
2. no one else could tamper or fabricate any of these messages (integrity)

A good example of that is, when you use browse a website, your browser shows a green lock next to the URL search bar. This green locks means that your browser (Alice here) communicates with the web server (Bob here) securely. It ensures that all requests and responses are encrypted and no one routing those messages over the internet can read them. It also guarantees that the website that you browse is the one it claims to be. 

## The cryptography toolbox

To build this secure channel, Alice and Bob will use several cryptographic tools: 

- symmetric and asymmetric encryption schemes to encrypt messages
- MAC (Message Authentication Code) and digital signatures to authenticate messages
- Diffie-Hellman protocol to exchange shared secrets

## What is encryption? 

Encryption is about encoding an intelligible message called a **plaintext** into an unintelligible one called the **ciphertext**. Decryption is the reverse operation that turns a ciphertext back into its original plaintext form. 

Encryption and decryption are based on an algorithm. A naive approach is to make those algorithm secrets to avoid having an adversary decrypting the messages. That approach is commonly called **security through obscurity** and it is strongly recommend not to base the entire security on the fact that the algorithm is secret. 

Instead, it is safer to assume that the adversary knows the cryptographic algorithm and have them use a secret variable that we call a cryptographic key.  

## The *Kerckhoffs's principle*

> "A cryptosystem should be secure even if everything about the system, except the key, is public knowledge"  Auguste Kerckhoffs

## Symmetric vs Asymmetric Encryption

In symmetric encryption, the same key is used to both encrypt and decrypt the messages.The key is a shared secret between the different parties in the confidence. 

In asymmetric encryption, there are two keys: one public key and one secret key.

In practice, we have cryptographic algorithms that are standards such as *AES* (symmetric encryption) and *RSA* (asymmetric encryption) for which the algorithm is public and have open-source implementation.

## The simplest but yet unsecured symmetric cipher:  *XOR cipher*

The XOR cipher is a modern version of the [Vigenere cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). Encrypting a plaintext message *p* is realized by XOR-ing it with a keystream made by concatenating the key *k* to match the plaintext length:

*E(k, p) = k &oplus; p*

Decrypting a ciphertext *c* is realized with the same operation:

*D(k, c) = k &oplus; c*

Since:

*D(k, E(k, p)) = k &oplus; (k &oplus; p) =  (k &oplus; k) &oplus; p = 0 &oplus; p = m*

Yet, the XOR cipher is completely unsecured for two main reasons:

1. It is vulnerable to a **ciphertext-only attack**. If the attacker knows a long enough ciphertext *(k &oplus; m)* (where *k* is a repeated string sequence), he/she might be able to uncover the key using [frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis) attack as [discussed here](https://crypto.stackexchange.com/questions/35318/cryptanalysis-of-xor-cipher-with-repeated-key-phrase). 

2. It is vulnerable to a **know-plaintext attack**. If the attacker knows at least one plaintext *m* and its corresponding ciphertext *(k &oplus; m)*, he/she will be able to fully recover the key *k*: 
	*c &oplus; p = (k &oplus; p) &oplus; p  = k &oplus; (p &oplus; p) = k &oplus; 0 = k*
	
Despite not being a good cipher, the XOR operator is an essential construct for all cryptography standards. 

## The perfect but yet unpractical symmetric cipher: *one-time pad*

The weakness of the XOR cipher comes from the fact that the key is repeated. However, it would become perfectly secured if, for each message, one could generate a random key of the length of the message. This cipher is called *one-time pad* and it is a perfect cipher since: 

1. it is resistant to a ciphertext-only attack since there is no repeated sequence of characters to perform a frequency analysis. 

2. it is resistant to a know-plaintext attack since even if the attacker is able to recover the random key used for encrypting the know plaintext, that key is not meant to be reused to encrypt another message

Not reusing the same random key twice is essential with *one-time pad*; hence the name. Not only to avoid know-plaintext attack but also to avoid a **key-reused attack** (also called *related-key attack*). If the attacker knows two ciphertexts encrypted with the same key *(k &oplus; m)* and *(k &oplus; m')*, he or she will be able to get *m &oplus; m'*

*(k &oplus; m) &oplus; (k &oplus; m')  = (k &oplus; k) &oplus; (m &oplus; m') = 0 &oplus; (m &oplus; m') = m &oplus; m'*
    
This attack does not reveal the key *k* nor it reveals the messages *m* or *m'* in clear however revealing *m &oplus; m'* does leak some information as shown [here when encrypting two images]([https://cryptosmith.com/2008/05/31/stream-reuse/]). 

Despite being perfect, *one-time* pad is unusable in practice. For each messages, Alice and Bob must agree on a fresh random key of the length of the message they want to exchange. 

## Anatomy of stream ciphers such as *RC4* and *Salsa20*

A pseudo-random generator that can stretch a small key to a larger random sequence to encrypt a message of any arbitrary length. 

Encrypting a plaintext message *p* is obtained by generating a pseudo-random keystream from *k* that matches the plaintext length and

performed by XOR-ing it with a pseudo-randomly generated keystream made from *k* that matches the plaintext length:

*E(k, p) = RNG(k) &oplus; p*

Decrypting a ciphertext *c* is realized with the same operation:

*D(k, c) = RNG(k) &oplus; c*

Since:

*D(k, E(k, p)) =  RNG(k) &oplus; (RNG(k) &oplus; p)=  (RNG(k) &oplus; RNG(k)) &oplus; p = 0 &oplus; p = p*

Using a pseudo-random number generator makes one-time pad practical. Instead of agreeing on key of the length of the message, Alice and Bob have to agree on a smaller key (usually 128 or 256 bits). The security of that technique rely on the fact that it is not possible for the attacker to recover the key even with a large piece of the random sequence is known. Said differently, the function *RNG(k)* is not reversible. 

Stream ciphers, like *one-time pad*, are vulnerable to the key-reuse attack. This means that one cannot use the same key to encrypt two messages otherwise the attacker might be able to recover some pieces of the messages as explain in the previous section.

*(RNG(k) &oplus; m) &oplus; (RNG(k) &oplus; m')  = (RNG(k) &oplus; RNG(k)) &oplus; (m &oplus; m') = 0 &oplus; (m &oplus; m') = m &oplus; m'*

Once again, the key-reused seems to make unpractical the use of stream ciphers. If Alice and Bob wants to exchange several messages, they should either never reset the random sequence message after message (this comes with serious synchronization problems) or use a different key for each message (this comes with the problem of key exchange). 



Alice generates a nonce 

*encrypt(key, nonce, plaintext) = RNG(key+nonce) &oplus; plaintext*

and then sends the ciphertext and the nonce to Bob that can decrypts using the shared key: 

*decrypt(key, nonce, ciphertext) = RNG(key+nonce) &oplus; ciphertext*

One of the earlier stream cipher standard is called *RC4*. It has been used in 

RC4 (now deprecated because [unsecured](https://www.rc4nomore.com/))

This is why it recommended to [](https://pycryptodome.readthedocs.io/en/latest/src/cipher/arc4.html) while new stream ciphers such as [Salsa20](https://pycryptodome.readthedocs.io/en/latest/src/cipher/salsa20.html) have the nonce built-in. 

[cracking the wireless securiy WEP](http://www.isaac.cs.berkeley.edu/isaac/wep-faq.html) 

In a nutshell, WEP encrypts network trafic using [RC4 stream cipher](https://en.wikipedia.org/wiki/RC4). Each packet is encrypted with a key derived from the wireless password and a nonce called *IV* (initialization vector) that was 24-bits only. This means that a given IV has 50% chance of being reused after 4000 packets in average (2^(24/2) based on the [birthday paradox](https://en.wikipedia.org/wiki/Birthday_problem)). This volume of packets is exchanged in matters of seconds with today's wireless technology. This is the reason why WEP is no longer use as it is considered as broken. 

## Anatomy of block ciphers such as *3DES* and *AES*


Block cipher modes of operations

A block cipher used with the CTR mode behaves shows the same properties as a stream cipher in terms of performance but also in terms of being prone to key-reused attack. 


## Conclusion

Stream cipher encrypt bit-by-bit which is perfect for encrypting data stream such as network traffic and videos as opposed to block-cipher that  

These days, AES is used 

We are going to cover 

What encryption does not ganrantee: authenticity

Another problem: key exchange






