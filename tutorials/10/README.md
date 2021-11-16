---
layout: default
permalink: /tutorials/10/
---

## Stack Protection

In this tutorial, you are asked to explain all stack protection mechanisms and identify them in the various assembly dumps of the `auth.c` example developed in the week 9 lecture.  

### Fortified Source Functions

1. What are Fortified Source Functions and how do they work? 
2. How to enable it on Linux? 
3. In `auth-fortify-enable.x86`, can you identify the "fortified" called to `strcpy`? 

### Stack Canaries

4. What are stack canaries and how do they work? 
5. How to enable it on Linux? 
6. In `auth-canary-enable.x86`, can you identify where the canary is set and verifies in the function `pwd`?

### Non Executable Stack

7. What is a non executable stack and how does it work? 
8. How to enable it on Linux? 
9. There is actually no difference at all between `auth-all-disable.x86` and `auth-all-disable.x86`, why?

### ASLR - Address Space Layout Randomization
    
10. What is ASLR and how does it work? 
11. How to enable it on Linux? 

### PIC/PIE - Position Independent Code

12. What is a position independent code and how does it work?
13. How to enable it on Linux?
14. In `auth-pie-enable.x86`, can you identify where/how the binary gets the offset to calculate the absolute address of the function `pwd`?