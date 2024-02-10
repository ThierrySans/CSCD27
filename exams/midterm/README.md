---
layout: default
permalink: /exams/midterm/
---

# CSCD27 Midterm


## Introduction

There is an ATM machine inside the building of University of Fail. Since no one is in the building during the pandemic, Mallory sneaks into the building and takes a closer look at it. The ATM machine is connected to an Ethernet socket in the wall. She unplugs the ATM's Ethernet cable and plugs it into her laptop. Then using an another Ethernet adapter on her laptop, she plugs her computer back into the Ethernet socket in the wall. After setting up her iptables rules, Mallory can now eavesdrop all network packets sent in and out of the ATM machine. Mallory noticed that every hours, the ATM sends some data to a server named atm.bank-of-fail.com

In this midterm, you are asked to considers Mallory options to hack the communication between the ATM and Bank server. 

For each of the following questions below: 

- if you believe that the attack is not possible, explain why exactly.  
- if you believe that the attack is possible, explain 1) how the attack is performed and 2) what Mallory will gain from the attack.  

You will only receives marks if your answer is fully justified. If you believe the attack is possible, you are not asked to write any code or command but you should detail every step of the attack carefully. 

You are allowed to make reasonable assumptions for anything that is not specified in this handout. Please clearly write down all assumptions that you make and justify why that assumption is reasonable to consider.

## Part 1

In its first version, the protocol used by the ATM and the server looks rather ad-hoc but Mallory has found some information online. Every hour, the ATM reports all transactions made by customers in the last 60 minutes. Each report contains the following information:

- an ATM ID (32 bytes)
- the report counter (32 bytes)
- the encrypted transaction records (each record is 64 bytes)
- a Message Authentication Code (MAC) (64 bytes) 
- The transaction records are encrypted using AES in CBC modeLinks to an external site., a shared key and an IV. The IV is fixed and Mallory knows its value from the protocol documentation she found. However, she does not know the shared key but the same key is used for encrypting every report. 

Each plaintext transaction record is divided into 2 pieces: 

- the customer account number (16 bytes) 
- the amount withdrawn (16 bytes)
- The MAC is calculated on the message: ATM ID + report counter + encrypted transaction records. This MAC is based on the HMAC standardLinks to an external site. (using SHA256 hash functionLinks to an external site.) and the same shared key (the one used for encrypting the transaction records).

When the server receives a report, the report will be accepted if and only if:

- the report counter has been incremented from the previous report sent by the same ATM machine (we assume the server keeps track of the different record counter for each ATM ID) 
- the MAC matches 

If these two conditions are met, the server will decrypt the transaction records and store them into the database without checking whether the customer number and the amount withdraw are valid.  

Questions:

1. Mallory believes that she can brute-force the shared key? 
2. Mallory believes that she can blindly modify the transaction records and they will still be accepted by the server? 
3. Mallory believes that she can perform a key reused attack?
4. Mallory believe that she can perform a hash-length extension attack?
5. Mallory believes that she can perform a replay attack?

## Part 2

One day, Mallory noticed that the ATM is now implementing a new protocol to transmit the hourly reports. The ATM sends each report to the server using HTTPS. The server uses TLS in version 1.3 and downgrading the protocol to use TLS 1.2 is not possible. The server uses a certificate signed by a trusted Certificate Authority. The ATM machine uses the command `curl` to send the report as a JSON data structure in the body of a POST request: 

```
curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"id": ... , "counter": ..., "record": [...], "mac": ...}' \
     https://atm.bank-of-fail.com/
```
  
FYI, the dots inside the JSON data structure are just fillers, the values are not important for the sake of the example.

FYI, the command curl has a –no-check-certificate option to ignore invalid certificates but that option is not used here. 

Questions:

1. Mallory believes that she can setup a fake server?
2. Mallory believes that she can perform a man-in-the-middle attack? 
3. Mallory believes that she can upload arbitrary data to the server? 

## Part 3

Mallory is now at home and she wants to hack into other ATM machines but without necessarily having a physical access to each of them. She has been able to get all IP adresses of each ATM managed by bank of fail. 

Questions:

1. Mallory believes that she can do an ARP-spoofing attack?
2. Mallory believes that she can do a DNS-spoofing attack?

## Bonus 

There are no bad answers to the questions below. You will get points if the instructors believes you genuinely made some efforts to provide an answer. Keep in mind that quantity does not beat quality.

Questions:

1. What are the strongest features of this course and of my teaching? In other words, what contributes most to your learning?
2. What specific suggestions do you have for changes that I can make to improve the course or how it is taught?


