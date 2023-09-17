#include <stdio.h>

int puts(const char *str) {
    FILE *file;
    char ch;
    file = fopen("./flag.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }
    fclose(file);
    return 0;
}

unsigned int sleep(unsigned int seconds) {
    printf("don't sleep MDFK");
    return 0;
}