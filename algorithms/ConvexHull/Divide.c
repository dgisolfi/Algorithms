#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// #include "<point.h>"

int getPoints() {
    FILE * fp;
    char line[256];
    int i = 0;
    int digit = 0;

    fp = fopen("./ConvexHull/points.txt","r");
    if(fp == NULL){
        printf("Cannot Open File");
    }
    fgets(line,sizeof(line),fp);
    digit = atoi(line);
    printf("digit = %d\n",digit);
    char *rest[digit];
    while(!feof(fp)) {
        while (i < digit) {
            fgets(line,sizeof(line),fp);
            fgets(line,sizeof(line),fp);
            char arr[sizeof(line)+1];
            strcpy(arr,line);
            rest[i] = arr;
            printf("restaurant = %s",rest[i]);
            i++;
        }
    }
    return 0;
};


int main() {
      
    getPoints();
    return 0;
};