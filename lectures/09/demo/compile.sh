#!/bin/bash

# docker build -t thierrysans/vulnerable  .

# docker run --rm --privileged ubuntu bash -c "echo 0 > /proc/sys/kernel/randomize_va_space"
#

docker run --rm -v $(pwd):/shared thierrysans/vulnerable gcc /shared/auth.c -o /shared/auth-all-disable  -m32 -fcf-protection=branch -mmanual-endbr -fno-stack-protector -no-pie -fno-pic -z execstack

docker run --rm -v $(pwd):/shared thierrysans/vulnerable objdump -d -M intel /shared/auth-all-disable > auth-all-disable.x86

docker run --rm -v $(pwd):/shared thierrysans/vulnerable gcc /shared/auth.c -o /shared/auth-nex-enable  -m32 -fcf-protection=branch -mmanual-endbr -fno-stack-protector -no-pie -fno-pic

docker run --rm -v $(pwd):/shared thierrysans/vulnerable objdump -d -M intel /shared/auth-nex-enable > auth-nex-enable.x86

docker run --rm -v $(pwd):/shared thierrysans/vulnerable gcc /shared/auth.c -o /shared/auth-canary-enable  -m32 -fcf-protection=branch -mmanual-endbr -no-pie -fno-pic

docker run --rm -v $(pwd):/shared thierrysans/vulnerable objdump -d -M intel /shared/auth-canary-enable > auth-canary-enable.x86

docker run --rm -v $(pwd):/shared thierrysans/vulnerable gcc /shared/auth.c -o /shared/auth-pic-enable  -m32 -fcf-protection=branch -mmanual-endbr -fno-stack-protector -no-pie

docker run --rm -v $(pwd):/shared thierrysans/vulnerable objdump -d -M intel /shared/auth-pic-enable > auth-pic-enable.x86

docker run --rm -v $(pwd):/shared thierrysans/vulnerable gcc /shared/auth.c -o /shared/auth-pie-enable  -m32 -fcf-protection=branch -mmanual-endbr -fno-stack-protector -fno-pic

docker run --rm -v $(pwd):/shared thierrysans/vulnerable objdump -d -M intel /shared/auth-pie-enable > auth-pie-enable.x86