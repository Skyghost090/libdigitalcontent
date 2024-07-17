#include <cstddef>
#include <stdio.h>
#include <string>
#include <sys/sysinfo.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <bits/stdc++.h>

extern "C" {
    int getUptime(){
        struct sysinfo info;
        sysinfo(&info);
        long uptime_seconds = info.uptime;
        int hours = (uptime_seconds % 86400) / 3600;
        return hours;
    }

    void setTime(int timeLimit){
        uid_t uid = getuid();
        if (uid != 0) {
            printf("libdigitalcontent-config only run a root\n");
            exit(6);
        }

        if (timeLimit > 24 || timeLimit < 0){
            printf("libdigitalcontent-config: timeLimit is from 0 to 24\n");
            exit(3);
        }

        chdir("/etc/systemd/system/");
        FILE *file;
        file = fopen("libdigitalcontent.service", "w+");

        fprintf(file,"[Unit]\nDescription=A digital health libary\nAfter=network.target\nStartLimitIntervalSec=0\n[Service]\nType=simple\nRestart=always\nRestartSec=1\nUser=root\nExecStart=/usr/share/libdigitalcontent/deamon -l %i\n[Install]\nWantedBy=multi-user.target\n", timeLimit);
        fclose(file);
    }

}
