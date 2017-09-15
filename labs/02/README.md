---
layout: default
permalink: /labs/02/
---

# Introduction to Docker

Throughout the semester, we are going to attack and defend vulnerable systems. For scalability and security issues, we cannot perform these attacks on real computer systems. Instead, we are going to use *Docker* to run lightweight virtual machines locally (either on the lab machines or on your own computer).

*Docker* is installed on the linux lab but you can also [install it on your own computer](https://docs.docker.com/engine/installation/). For now, we are going to go through basic definitions and commands to get you started. Indeed, we encourage to [learn more about docker](https://docs.docker.com/get-started/).

Here are some basic definitions taken from the [Get Started](https://docs.docker.com/get-started/) page on the *Docker* website.

> - an **image** is a lightweight, stand-alone, executable package that includes everything needed to run a piece of software, including the code, a runtime, libraries, environment variables, and config files.

> - a **container** is a runtime instance of an image—what the image becomes in memory when actually executed. It runs completely isolated from the host environment by default, only accessing host files and ports if configured to do so.

**important:** Before we start, it is important to know two things while working with Docker **on the linux lab machines** (these recommendations do not apply on when you work on your own computer).

1. Do *not* SSH into a lab machine if you are going to use *Docker*. Since there is only one *docker* daemon, it will conflict if two people both use the docker daemon on the same machine. Therefore, always work in front of the lab machine rather than remotely.  

2. The docker daemon can only access files that are in your `cscd27f17_space` directory. You might get a `permission denied` message if you try to access files elsewhere with *Docker*. Therefore, always work with *Docker* from that directory. 

Let us start with the `hello-world` example for *Docker*. The following command downloads the image `hello-world` (the first time only) and then run a container from that image. This container shows a message and then stop. 

```
$ docker run hello-world
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

You can see all containers active on your machine with the command: 
    
```
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                    PORTS               NAMES
12cd26805db7        hello-world         "/hello"            3 seconds ago       Exited (0) 1 second ago                       unruffled_newton
```
    
Although a container has stopped (`Exited` status), it remains active on your system until you explicitly remove it using either its name or container ID. 

```
$ docker rm 12cd26805db7
```

You can also remove all containers with one command: 

```
$ docker rm $(docker ps -a -q)
```

By default, *Docker* does not share files between your computer and the containers unless you explicitly configure it so. For instance, let us create a python file `hello.py` on our machine and let us execute this file using a container that has the `python3` interpreted (for instance we can use the [official *Docker* image for python](https://hub.docker.com/_/python/)).

```
$ echo "print(\"hello world\")" > hello.py
$ docker run -v $(pwd):/shared python python3 /shared/hello.py
hello world
```
    
# The Caesar Cipher

As a small exercise, we are going to implement our first cryptographic scheme based on one of the earliest cipher called the *Caesar Cipher*.

## Implement the Caesar Cipher

After reading and understanding the [Caesar Cipher](https://learncryptography.com/classical-encryption/caesar-cipher), copy the [starter code from the course repository on github](https://github.com/ThierrySans/CSCD27/tree/master/labs/02/src/) and complete the file `caesar26.py` to encrypt/decrypt message files that contain messages with lowercase english letters only `[a-z]` (no space nor punctuation). you can test your work with *Docker* as follows: 

- encrypt a file (called `plaintext.txt` for instance)
    
  `$ docker run -v $(pwd):/shared python python3 /shared/main.py --encrypt --key 4 /shared/plaintext.txt`

- decrypt a file (called `ciphertext.txt` for instance)
    
  `$docker run -v $(pwd):/shared python python3 /shared/main.py --decrypt --key 4 /shared/ciphertext.txt`

## Submit your solution [coming soon sometimes this week]

Make sure that your program works with *Docker*, it will be tested that way. Then, submit your solution to the *SecLab* application. 