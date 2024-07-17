#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <stdio.h>
#include "libdigitalcontent.cpp"
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <linux/reboot.h>
#include <sys/reboot.h>

int main(int argc, char* argv[]){
    if (argc == 1){
        printf("Please type -h for more information\n");
        exit(1);
    }

    if (strcmp(argv[1],"-l") == 0){
        int hours = std::stoi(argv[2]);
        if (hours > 24 || hours < 0){
            printf("Invalid number\n");
            exit(2);
        }

        while (1) {
            sleep(5);
            if (hours < getUptime()) {
                system("poweroff");
                exit(0);
            }
        }

    } else if (strcmp(argv[1],"-h") == 0) {
        printf("deamon [options]:\n\n[-l + [hours limit]]: Set a uptime limit\n[-h]: For more information\n");
    } else {
        printf("Invalid argument type -h for more information\n");
        exit(1);
    }
}
