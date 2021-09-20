---
layout: default
permalink: /tutorials/03/
---

# Classical Cryptography

## Cryptosystems

Alice wants to send a message to Bob. Each message is composed of 26 characters (no space, no punctuation). To encrypt each message, Alice is considering two ciphers:

- cipher 1: a monoalphabetic cipher that substitutes each letter of the alphabet by another one (a.k.a substitution cipher) . 
- cipher 2: a polyalphabetic cipher that combines the plaintext with a key (a.k.a Vigenere's cipher). The key length is fixed to 15 characters exactly. 

1. After calculating the entropy of both ciphers. Which one is the most resistant to a brute force attack?

2. Which one is the most resistant to a ciphertext only attack? 

3. How would you attack both of these ciphers using a plaintext attack? 

## Frequency analysis

In this discussion, we will preview the first sophisticated approach to cryptanalysis, described by Al-Kindi, born in Basra in what is now Iraq, in 801.

![al-kindi](media/al-kindi.jpg)

The first graph below shows the letter frequencies for an article that appeared in the Toronto Star. The graph was produced by generating a frequency count of alphabetic characters using a Python program, and then displaying that data using an MS-Excel chart.

![original](media/original.png)

The second graph below shows the letter frequencies for a Caesar (shift) cipher encoding of that same article. Caesar certainly simplifies the cryptanalyst's job!

![caesar](media/caesar.png)

In class we will see that Caesar and its more sophisticated cousin, monoalphabetic cipher, are both vulnerable to frequency 
cryptanalysis. 

3. Based on your understanding of the Caesar cipher, can you guess the key that was used to produce the second graph. 

Vigenere, a polyalphabetic cipher, should be less vulnerable to this attack. Yet, the third graph below shows a graph of letter-frequency for a Vigenere-encoding of the same newspaper article whose letter frequency is displayed above.

![vigenere](media/vigenere.png)

4. Based on your understanding of the Vigenere cipher, can you guess the length of the key?

5. What role does a Vigenere password play in frequency profile of the ciphertext?

6. What would the ideal histogram look like, from the point of view of making cryptanalysis as difficult as possible?

## Scale of key robustness

7. Imagine a ciphertext encrypted with a 128 bits key and let's presume we have a very powerful computer that can brute force 10^12 keys per second.

    - How many keys in total?
    - How many keys per year can we compute?
    - How long would it take to compute all keys?
    - How many computers would you need to crack all keys within a day?

8. Same question with 256 bits? 