#include <stdio.h>
#include <stdlib.h>

int main() {
    // Crie um ponteiro que indique uma variável do tipo inteiro;
    int *ptr;

    // Defina que esse ponteiro é igual à alocação de memória para guardar oito dados do tipo inteiro;
    ptr = (int *)malloc(8 * sizeof(int));

    if (ptr == NULL) {
        printf("Erro na alocação de memória.\n");
        return 1;
    }

    // Efetue a realocação de memória para um tamanho que guarde doze dados inteiros;
    int *newPtr = (int *)realloc(ptr, 12 * sizeof(int));

    if (newPtr == NULL) {
        printf("Erro na realocação de memória.\n");
        free(ptr);  // Libere o espaço alocado anteriormente
        return 1;
    } else {
        ptr = newPtr;  // Atualize o ponteiro para apontar para a nova área alocada
    }

    // Libere o espaço alocado nas funções anteriores;
    free(ptr);

    return 0;
}