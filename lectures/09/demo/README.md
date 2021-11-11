docker run --rm -v $(pwd):/shared -u mallory --privileged -it thierrysans/vulnerable:stack-smashing-branching bash

gcc /shared/vuln.c -o /shared/vuln  -m32

objdump -d -M intel /shared/vuln


-fno-stack-protector
-no-pie



gcc /shared/helloworld.c -o /shared/helloworld-new  -m32 -no-pie -fno-stack-protector -fno-pic -fcf-protection=branch -mmanual-endbr




https://stackoverflow.com/questions/16023637/difference-between-pic-vs-pie



## Run branching exploit

docker run --rm -v $(pwd):/shared --privileged --workdir /shared -it thierrysans/vulnerable bash 

$ ./auth $(python3 branching-exploit.py)

Debugging

$ dmesg | grep "auth" | tail -n 1


## Running GDB

docker run --rm -v $(pwd):/shared --privileged --workdir /shared -it thierrysans/vulnerable bash     

$ gdb -q auth

(gdb) run $(python3 -c 'print("A"*272)')

(gdb) print $ebp

(gdb) print $ebp - 0x108

(gdb) print $ebp - 0x108 + 0x40

