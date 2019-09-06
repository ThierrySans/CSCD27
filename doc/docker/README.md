---
layout: default
permalink: /doc/docker/
---

# Introduction to Docker

Throughout the semester, we are going to attack and defend vulnerable systems. For scalability and security issues, we cannot perform these attacks on real computer systems. Instead, we are going to use *Docker* to run lightweight virtual machines locally (either on the lab machines or on your own computer).

*Docker* is installed on the linux lab but you can also [install it on your own computer](https://docs.docker.com/engine/installation/). For now, we are going to go through basic definitions and commands to get you started. Indeed, we encourage to [learn more about docker](https://docs.docker.com/get-started/).

Here are some basic definitions taken from the [Get Started](https://docs.docker.com/get-started/) page on the *Docker* website.

> - an **image** is a lightweight, stand-alone, executable package that includes everything needed to run a piece of software, including the code, a runtime, libraries, environment variables, and config files.

> - a **container** is a runtime instance of an image—what the image becomes in memory when actually executed. It runs completely isolated from the host environment by default, only accessing host files and ports if configured to do so.

**important:** Before we start, it is important to know two things while working with Docker **on the linux lab machines** (these recommendations do not apply on when you work on your own computer).

1. Do *not* SSH into a lab machine if you are going to use *Docker*. Since there is only one *docker* daemon, it will conflict if two people both use the docker daemon on the same machine. Therefore, always work in front of the lab machine rather than remotely.  

2. The docker daemon can only access files that are in your `/courses/courses/cscd27f19/{utorid}` directory. You might get a `permission denied` message if you try to access files elsewhere with *Docker*. Therefore, always work with *Docker* from that directory. Make sure that all files that docker will use must be in that directory with read permissions to group and others (og+r). If you have directories, all of these directories must be traversable (og+x)

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

Here is a small Docker cheat sheet:

- Run command in a container (ubuntu image)
  ```
  $ docker run ubuntu cat /etc/lsb-release
  ```

- Run interactive shell (ubuntu image)
  ```
  $ docker run -it ubuntu bash
  ```

- Get container status
  ```
  $ docker ps -a
  ```

- Run command in a named container (ubuntu image)
  ```
  $ docker run --name mycontainer ubuntu cat /etc/lsb-release
  ```

- Run container with shared directory
  ```
  $ docker run -v $(pwd):/shared ubuntu ls /shared
  ```

- Run with the current working path 
  ```
  $ docker run -v $(pwd):/shared -w /shared ubuntu ls
  ```

- Stop a container 
  ```
  $ docker stop container_name
  ```

- Delete a container
  `$ docker rm container_name`

- Stop all containers
  ```
  $ docker stop $(docker ps -a -q)
  ```

- Delete all containers
  ```
  $ docker rm $(docker ps -a -q)
  ```

- Delete all images
  ```
  $ docker rmi $(docker images -q)
  ```

- Full cleanup
  ```
  $ docker system prune -a
  ```

- Show env variables:
  ```
  $ docker inspect -f "{{ "{{ .Config.Env "}}}}" container_name
  ```

- Show stats (with container name)
  ```
  $ docker stats $(docker ps | awk '{if(NR>1) print $NF}')
  ```

- Create an image from a Dockerfile (assuming in the same directory)
  ```
  $ docker build -t . Image_name
  ```

- Get IP addresses 
  ```
  $ docker ps -q | xargs docker inspect --format '{{ "{{ .Id "}}}} - {{ "{{ .Name " }}}} - {{ "{{ .NetworkSettings.IPAddress " }}}}'
  ```

