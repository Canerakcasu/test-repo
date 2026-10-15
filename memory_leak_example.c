#include <stdlib.h>
#include <stdio.h>

void process_items(int count) {
    char *buffer = malloc(count * sizeof(char));
    if (buffer == NULL) {
        return;
    }

    for (int i = 0; i < count; i++) {
        buffer[i] = 'A';
    }

    /* Missing free(buffer) */
    printf("Processed %d items\n", count);
}

int main(void) {
    process_items(1000000);
    return 0;
}
