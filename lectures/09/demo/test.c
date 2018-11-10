#include <stdio.h>
#include <string.h>

int foo2(int *i, char *s){
    printf("%d", *i);
    char buffer[10];
    strcpy(buffer, s);
    printf("%s", buffer);
}

int foo(){
    int i = 8;
    char *s = "hello";
    foo2(&i, s);
}

int main(int argc, char **argv){
    foo();
}