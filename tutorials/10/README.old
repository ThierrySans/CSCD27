# CSCD27 Discussion 9

## Some common registers

source: [*Dhaval Kapil - Buffer Overflow Exploit*](https://dhavalkapil.com/blogs/Buffer-Overflow-Exploit/)

1. **%eip: The Instruction pointer register.** It stores the address of the next instruction to be executed. After every instruction execution it’s value is incremented depending upon the size of an instrution.
2. **%esp: The Stack pointer register.** It stores the address of the top of the stack. This is the address of the last element on the stack. The stack grows downward in memory(from higher address values to lower address values). So the %esp points to the value in stack at the lowest memory address.
3. **%ebp: The Base pointer register.** The %ebp register usually set to %esp at the start of the function. This is done to keep tab of function parameters and local variables. Local variables are accessed by subtracting offsets from %ebp and function parameters are accessed by adding offsets to it as you shall see in the next section.
4. **%eax, %ebx, ecx and edx: General purposes registers.**.

## Memory Layout of a C program

source: [*Dhaval Kapil - Buffer Overflow Exploit*](https://dhavalkapil.com/blogs/Buffer-Overflow-Exploit/)

![Memory](http://i.stack.imgur.com/1Yz9K.gif "Memory")

1. **Command line arguments and environment variables:** The arguments passed to a program before running and the environment variables are stored in this section.
2. **Stack:** This is the place where all the function parameters, return addresses and the local variables of the function are stored. It’s a LIFO structure. It grows downward in memory(from higher address space to lower address space) as new function calls are made. We will examine the stack in more detail later.
3. **Heap:** All the dynamically allocated memory resides here. Whenever we use malloc to get memory dynamically, it is allocated from the heap. The heap grows upwards in memory(from lower to higher memory addresses) as more and more memory is required.
4. **Uninitialized data(Bss Segment):** All the uninitialized data is stored here. This consists of all global and static variables which are not initialized by the programmer. The kernel initializes them to arithmetic 0 by default.
5. **Initialized data(Data Segment):** All the initialized data is stored here. This consists of all global and static variables which are initialized by the programmer.
6. **Text:** This is the section where the executable code is stored. The loader loads instructions from here and executes them. It is often read only.

## Memory and Addressing Modes

source: [*David Evans - x86 Assembly Guide*](http://www.cs.virginia.edu/~evans/cs216/guides/x86.html)

### Declaring Static Data Regions

Not relevant here.

### Addressing Memory

Modern x86-compatible processors are capable of addressing up to 2^32 bytes of memory: memory addresses are 32-bits wide. The addressing modes can be used with many x86 instructions (describe in the next section). Here we illustrate some examples using the mov instruction that moves data between registers and memory. This instruction has two operands: the first is the destination and the second specifies the source.

Some examples of mov instructions using address computations are:

- `mov eax, [ebx]` move the 4 bytes in memory at the address contained in EBX into EAX
- `mov [var], ebx` move the contents of EBX into the 4 bytes at memory address var. (Note, var is a 32-bit constant).
- `mov eax, [esi-4]` move 4 bytes at memory address ESI + (-4) into EAX
- `mov [esi+eax], cl` move the contents of CL into the byte at address ESI+EAX
- `mov edx, [esi+4*ebx]` move the 4 bytes of data at address ESI+4*EBX into EDX

### Size Directives

In general, the intended size of the of the data item at a given memory address can be inferred from the assembly code instruction in which it is referenced. For example, in all of the above instructions, the size of the memory regions could be inferred from the size of the register operand. When we were loading a 32-bit register, the assembler could infer that the region of memory we were referring to was 4 bytes wide. When we were storing the value of a one byte register to memory, the assembler could infer that we wanted the address to refer to a single byte in memory.

However, in some cases the size of a referred-to memory region is ambiguous. Consider the instruction `mov [ebx], 2`. Should this instruction move the value 2 into the single byte at address EBX? Perhaps it should move the 32-bit integer representation of 2 into the 4-bytes starting at address EBX. Since either is a valid possible interpretation, the assembler must be explicitly directed as to which is correct. The size directives BYTE PTR, WORD PTR, and DWORD PTR serve this purpose, indicating sizes of 1, 2, and 4 bytes respectively.

For example:

- `mov BYTE PTR [ebx], 2` move 2 into the single byte at the address stored in EBX.
- `mov WORD PTR [ebx], 2` move the 16-bit integer representation of 2 into the 2 bytes starting at the address in EBX.
- `mov DWORD PTR [ebx], 2` move the 32-bit integer representation of 2 into the 4 bytes starting at the address in EBX.

## Instructions

source: [*David Evans - x86 Assembly Guide*](http://www.cs.virginia.edu/~evans/cs216/guides/x86.html)

## Calling Convention

source: [*David Evans - x86 Assembly Guide*](http://www.cs.virginia.edu/~evans/cs216/guides/x86.html)

The calling convention is a protocol about how to call and return from functions. The C calling convention is based heavily on the use of the hardware-supported stack. It is based on the push, pop, call, and ret instructions. Function parameters are passed on the stack. Registers are saved on the stack, and local variables used by functions are placed in memory on the stack.

The calling convention is broken into two sets of rules. The first set of rules is employed by the caller of the function, and the second set of rules is observed by the writer of the function (the callee).

![Stack during Function Call ](http://www.cs.virginia.edu/~evans/cs216/guides/stack-convention.png "Stack during Function Call")

A good way to visualize the operation of the calling convention is to draw the contents of the nearby region of the stack during function execution. The image above depicts the contents of the stack during the execution of a function with three parameters and three local variables. The cells depicted in the stack are 32-bit wide memory locations, thus the memory addresses of the cells are 4 bytes apart. The first parameter resides at an offset of 8 bytes from the base pointer. Above the parameters on the stack (and below the base pointer), the call instruction placed the return address, thus leading to an extra 4 bytes of offset from the base pointer to the first parameter. When the ret instruction is used to return from the function, it will jump to the return address stored on the stack.

### Caller Rules

To make a subrouting call, the caller should:

1. Before calling a function, the caller should save the contents of certain registers that are designated caller-saved. The caller-saved registers are EAX, ECX, EDX. Since the called function is allowed to modify these registers, if the caller relies on their values after the function returns, the caller must push the values in these registers onto the stack (so they can be restore after the function returns.
2. To pass parameters to the function, push them onto the stack before the call. The parameters should be pushed in inverted order (i.e. last parameter first). Since the stack grows down, the first parameter will be stored at the lowest address (this inversion of parameters was historically used to allow functions to be passed a variable number of parameters).
3. To call the function, use the call instruction. This instruction places the return address on top of the parameters on the stack, and branches to the function code. This invokes the function, which should follow the callee rules below.

After the function returns (immediately following the call instruction), the caller can expect to find the return value of the function in the register EAX. To restore the machine state, the caller should:

4. Remove the parameters from stack. This restores the stack to its state before the call was performed.
5. Restore the contents of caller-saved registers (EAX, ECX, EDX) by popping them off of the stack. The caller can assume that no other registers were modified by the function.

### Callee Rules

The definition of the subroutine should adhere to the following rules at the beginning of the subroutine:

1. Push the value of EBP onto the stack, and then copy the value of ESP into EBP using the following instructions:

    ```
    push ebp
    mov  ebp, esp
    ```

    This initial action maintains the base pointer, EBP. The base pointer is used by convention as a point of reference for finding parameters and local variables on the stack. When a subroutine is executing, the base pointer holds a copy of the stack pointer value from when the subroutine started executing. Parameters and local variables will always be located at known, constant offsets away from the base pointer value. We push the old base pointer value at the beginning of the subroutine so that we can later restore the appropriate base pointer value for the caller when the subroutine returns. Remember, the caller is not expecting the subroutine to change the value of the base pointer. We then move the stack pointer into EBP to obtain our point of reference for accessing parameters and local variables.
2. Next, allocate local variables by making space on the stack. Recall, the stack grows down, so to make space on the top of the stack, the stack pointer should be decremented. The amount by which the stack pointer is decremented depends on the number and size of local variables needed. For example, if 3 local integers (4 bytes each) were required, the stack pointer would need to be decremented by 12 to make space for these local variables (i.e., sub esp, 12). As with parameters, local variables will be located at known offsets from the base pointer.
3. Next, save the values of the callee-saved registers that will be used by the function. To save registers, push them onto the stack. The callee-saved registers are EBX, EDI, and ESI (ESP and EBP will also be preserved by the calling convention, but need not be pushed on the stack during this step).

After these three actions are performed, the body of the subroutine may proceed. When the subroutine is returns, it must follow these steps:

1. Leave the return value in EAX.
2. Restore the old values of any callee-saved registers (EDI and ESI) that were modified. The register contents are restored by popping them from the stack. The registers should be popped in the inverse order that they were pushed.
3. Deallocate local variables. The obvious way to do this might be to add the appropriate value to the stack pointer (since the space was allocated by subtracting the needed amount from the stack pointer). In practice, a less error-prone way to deallocate the variables is to move the value in the base pointer into the stack pointer: mov esp, ebp. This works because the base pointer always contains the value that the stack pointer contained immediately prior to the allocation of the local variables.
4. Immediately before returning, restore the caller's base pointer value by popping EBP off the stack. Recall that the first thing we did on entry to the subroutine was to push the base pointer to save its old value.
5. Finally, return to the caller by executing a ret instruction. This instruction will find and remove the appropriate return address from the stack.

## Credits

This tutorial is built from the excellent materials authored by *David Evans* and *Dhaval Kapil*:
- [*David Evans - x86 Assembly Guide*](http://www.cs.virginia.edu/~evans/cs216/guides/x86.html)
- [*Dhaval Kapil - Buffer Overflow Exploit*](https://dhavalkapil.com/blogs/Buffer-Overflow-Exploit/)
