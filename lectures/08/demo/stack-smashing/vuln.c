#include <stdio.h>

void secretFunction(){
    printf("Smashing the Stack for Fun and Profit\n");
}

void echo(){
    char buffer[20];
    printf("Enter some text:\n");
    scanf("%s", buffer);
    printf("You entered: %s\n", buffer);
}

int main(int argc, char **argv){
    echo();
    return 0;
}