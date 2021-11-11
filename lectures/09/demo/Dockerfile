FROM ubuntu:20.04

RUN apt-get update && DEBIAN_FRONTEND="noninteractive" TZ="America/Toronto" apt-get install gdb gcc-multilib binutils python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential gdb nasm hardening-check -y

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade pwntools
