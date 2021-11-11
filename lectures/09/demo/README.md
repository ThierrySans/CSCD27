## Running branching exploit

docker run --rm -v $(pwd):/shared --privileged --workdir /shared -it thierrysans/vulnerable bash 

$ ./auth-all-disable $(python3 branching-exploit.py)

## Running shellcode exploit

docker run --rm -v $(pwd):/shared --privileged --workdir /shared -it thierrysans/vulnerable bash 

$ ./auth-all-disable $(python3 branching-shellcode.py)

## Stack trace

$ dmesg | grep "auth" | tail -n 1


## Running GDB

docker run --rm -v $(pwd):/shared --privileged --workdir /shared -it thierrysans/vulnerable bash     

$ gdb -q auth-all-disable

(gdb) run $(python3 -c 'print("A"*272)')

(gdb) print $ebp

(gdb) print $ebp - 0x108

(gdb) print $ebp - 0x108 + 0x40

