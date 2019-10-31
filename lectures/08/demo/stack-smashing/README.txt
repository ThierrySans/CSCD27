# execute the vulnerable VM

docker run --rm -v $(pwd):/shared --privileged --userns=host -it thierrysans/vulnerable:stack-smashing-branching bash

# compile the program

gcc /shared/vuln.c -o /shared/vuln -fno-stack-protector -m32

# run the payload

python /shared/payload.py | /shared/vuln