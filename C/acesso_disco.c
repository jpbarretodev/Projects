#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *gerar_comando(char *comando, char *comando2) {
    char comando_completo[100];
    snprintf(comando_completo, sizeof(comando_completo), "%s %s", comando, comando2);
    system(comando_completo);
    return 0;
}

int criar_diretorio(char *nome) {
    gerar_comando("mkdir", nome);
    return 0;
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

    char nome_dir[100], nome_arq[100], frase[100];
    printf("\nAcessando o disco!\n\nPrimeiro, crie um diretorio!\n\nInsira o nome do diretorio: ");
    scanf("%99s", nome_dir);

    if(!criar_diretorio(nome_dir)) {
        printf("Diretorio criado com sucesso!\nVamos abrir o diretorio sem alterar nada.\n\n");

        if(!gerar_comando("cd", nome_dir)) {
            printf("Diretorio aberto. Agora, vamos criar um arquivo de texto fora deste diretorio!\nDigite o nome do arquivo: ");
            scanf("%99s", nome_arq);

            if(!criar_arquivo(nome_arq)) {
                printf("Arquivo criado! Agora, vamos escrever uma frase para esse arquivo de texto.\nA frase sera: 'ola,mundo!'.\n\nEscreva: ");
                scanf("%99s", frase);

                if(!escrever_arquivo(nome_arq, frase)) {
                    printf("Frase criada, teste ok");
                } else {
                    printf("Nao foi possivel adicionar a frase.");
                }
            } else {
                printf("Nao foi possivel criar o arquivo.");
            }
        } else {
            printf("Nao foi possivel abrir o diretorio.");
        }
    } else {
        printf("Erro ao criar o diretorio");
    }
}