#include <stdio.h>
#include <string.h>

char *gerar_comando(char *comando, char *comando2) {
    static char comando_completo[100];
    snprintf(comando_completo, sizeof(comando_completo), "%s %s", comando, comando2);
    return comando_completo;
}

char *criar_diretorio(char *nome) {
    return gerar_comando("mkdir", nome);
}

int criar_arquivo(char *nome) {
    char nome_extensao[100];
    snprintf(nome_extensao, sizeof(nome_extensao), "%s.txt", nome);
    FILE *arq;
    arq = fopen(nome_extensao, "w");
    if(arq == NULL) {
        return 1;
    } else {
        fclose(arq);
        return 0;
    }
}

int escrever_arquivo(char *nome_arquivo, char *frase) {
    char frase_extensao[100];
    snprintf(frase_extensao, sizeof(frase_extensao), "%s.txt", nome_arquivo);
    FILE *arq;
    arq = fopen(frase_extensao, "w");
    fprintf(arq, "%s", frase);
    fclose(arq);
    return 0;
}

int main(void) {
    char nome[100], frase[100];
    printf("Digite o nome para criar o arquivo: ");
    scanf("%99s", nome);
    if(!criar_arquivo(nome)) {
        printf("Arquivo criado\n");
    } else {
        printf("Arquivo nao criado\n");
    }
    printf("Escreva uma frase para colocar no arquivo: ");
    scanf("%99s", frase);
    if(!escrever_arquivo(nome, frase)) {
        printf("Dado armazenado\n");
    } else {
        printf("Falha ao armazenar o dado\n");
    }
}