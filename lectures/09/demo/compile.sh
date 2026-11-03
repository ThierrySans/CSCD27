#!/bin/bash

# build the docker image

docker build -t thierrysans/vulnerable  .

# disable ASLR

docker run --rm --privileged ubuntu bash -c "echo 0 > /proc/sys/kernel/randomize_va_space"

# compile with all protection disabled

docker run --rm -v $(pwd):/shared thierrysans/vulnerable gcc /shared/auth.c -o /shared/auth-all-disable  -m32 -fcf-protection=branch -mmanual-endbr -fno-stack-protector -no-pie -fno-pic -z execstack

docker run --rm -v $(pwd):/shared thierrysans/vulnerable objdump -d -M intel /shared/auth-all-disable > auth-all-disable.x86

# compile with compiled fortify functions 

docker run --rm -v $(pwd):/shared thierrysans/vulnerable gcc /shared/auth.c -o /shared/auth-fortify-enable  -m32 -fcf-protection=branch -mmanual-endbr -fno-stack-protector -no-pie -fno-pic -z execstack -O2 -D_FORTIFY_SOURCE=2 

docker run --rm -v $(pwd):/shared thierrysans/vulnerable objdump -d -M intel /shared/auth-fortify-enable > auth-fortify-enable.x86

# compile with NX enabled

docker run --rm -v $(pwd):/shared thierrysans/vulnerable gcc /shared/auth.c -o /shared/auth-nex-enable  -m32 -fcf-protection=branch -mmanual-endbr -fno-stack-protector -no-pie -fno-pic

docker run --rm -v $(pwd):/shared thierrysans/vulnerable objdump -d -M intel /shared/auth-nex-enable > auth-nex-enable.x86

# compile with canary anabled

docker run --rm -v $(pwd):/shared thierrysans/vulnerable gcc /shared/auth.c -o /shared/auth-canary-enable  -m32 -fcf-protection=branch -mmanual-endbr -no-pie -fno-pic

docker run --rm -v $(pwd):/shared thierrysans/vulnerable objdump -d -M intel /shared/auth-canary-enable > auth-canary-enable.x86

# compile with PIE enabled

docker run --rm -v $(pwd):/shared thierrysans/vulnerable gcc /shared/auth.c -o /shared/auth-pie-enable  -m32 -fcf-protection=branch -mmanual-endbr -fno-stack-protector

docker run --rm -v $(pwd):/shared thierrysans/vulnerable objdump -d -M intel /shared/auth-pie-enable > auth-pie-enable.x86