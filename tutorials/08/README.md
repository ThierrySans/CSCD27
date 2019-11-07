---
layout: default
permalink: /tutorials/08/
---

# Passwords

A website requires its users to have passwords with a length of exactly 8 characters long and made of alpha-numeric characters.

1. How many passwords are possible?

2. What is the password entropy (n-bit security)?

## Cracking passwords from the login page

Assuming that we use a password cracking tool that tries different login/password using the login page. We roughly estimates that:

- the login page returns a response in 100ms
- the cracking tool can spawn 100 threads sending such requests

3. How long would it take to:

    - brute-force the password for 1 user
    - brute force the password for n users

## Cracking unsalted hash passwords

Assuming that we hack into their server and download their (lame) database of unsalted passwords. We roughly estimates that:

- computing a hash takes 10^(-9) seconds
- a table lookup takes 10^(-3) seconds (regardless the size of the table)
- testing whether two hashes are equal takes no time 

4. For all types of attack, how long would it take to:

    - brute-force 1 password for m users
    - brute-force m passwords for 1 user
    - brute force m passwords for n users

5. If we use rainbow tables, how long would it take to:

    - crack the password of 1 user
    - crack the password of n users

## Cracking salted hash passwords

Assuming now that the passwords are salted (each user has a different salt). 

6. For all types of attack, how long would it take to:

    - brute-force 1 password for m users
    - brute-force m passwords for 1 user
    - brute force m passwords for n users
    
7. How about using rainbow tables on salted passwords?     


