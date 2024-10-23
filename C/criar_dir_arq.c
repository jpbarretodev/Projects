#include <stdio.h>
//#include <windows.h>
#include <stdlib.h>
#include <string.h>

char *cria_comando(char *comando_terminal, char *nome_diretorio) {
  static char comando[100];
  snprintf(comando, sizeof(comando), "%s %s", comando_terminal, nome_diretorio);
  return comando;
}


int main() {
  char nome_drt[100];
  char nome_arquivo[100];
  char mensagem[100];

  printf("Digite um diretorio: ");
  scanf("%99s", nome_drt);
  char *comando_completo = cria_comando("mkdir", nome_drt);
  printf("shell('%s')", comando_completo);
 
 
  printf("Digite o nome da mensagem: ");
  scanf("%99s", mensagem);
 
  FILE *file = fopen(nome_arquivo, "w");
 
  if(file) {
      fprintf(file, mensagem, mensagem);
      fclose(file);
  } else {
      printf("Falha ao criar o arquivo");
  }
 
  return 0;
}
