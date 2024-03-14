#include <stdio.h>
#include <string.h>
#define BUFFER_SIZE 256 

void accessDenied(){
    printf("Access denied!\n");
}
void accessGranted(){
    printf("Access granted!\n");
}

int pwd(char *arg){
    char password[BUFFER_SIZE]; 
    strcpy(password, arg);
    return strcmp(password, "S3cF41l");
}

int main(int argc, char **argv){
    if (!pwd(argv[1])){
        accessGranted();
        return 0;
    }else{
        accessDenied();
        return 1; 
    }
}