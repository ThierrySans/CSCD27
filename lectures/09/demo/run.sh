#!/bin/bash

gcc /shared/test.c -o /shared/test -fno-stack-protector -m32
objdump -d -M intel /shared/test > /shared/test.x86 