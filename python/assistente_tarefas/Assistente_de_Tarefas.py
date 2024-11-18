#incluir biblioteca caso necessidade
import json
pass

#globais
objetos = []

#iniciar a classe principal
class Tarefa:

    def __init__(self, nome, tempo):
        self.nome = nome
        self.tempo = int(tempo)

    def adicionar_tarefa(self):
        try:
            objetos.append(self)
            return print("\nTarefa adicionada com sucesso!\n")
        except:
            return print("Não foi possível adicionar a tarefa\n")

    @staticmethod
    def objeto_unico(index):
        objeto_unic = objetos[index]
        return objeto_unic

    @staticmethod
    def visualizar_tarefa():
        if len(objetos) > 0:
            for i, objeto in enumerate(objetos):
                print(f"\n{i+1} - {objeto.nome}: {objeto.tempo} horas")

    @staticmethod
    def excluir_tarefa():
        print("Selecione a tarefa que deseja excluir: ")
        Tarefa.visualizar_tarefa()
        escolha = int(input("Selecione o número da tarefa que deseja excluir.\nEscolha: "))
        if escolha != 0 and escolha <= len(objetos):
            objetos.pop(escolha-1)
            return print("Tarefa apagada com sucesso\n")
        else:
            return print("Falha ao excluir objeto.")
        
    @staticmethod
    def editar_tarefa():
        print("Selecione a tarefa que deseja editar:\n")
        Tarefa.visualizar_tarefa()
        verificacao = int(input("Escolha o número da tarefa: "))
        if verificacao > 0 and verificacao <= len(objetos):
            escolha = int(input("O que você deseja alterar?\n1 - Nome\n2 - Tempo\nEscolha: "))
            while escolha != 1 and escolha != 2:
                escolha = int(input("Valor incorreto! Insira 1 para alterar o nome ou 2 para alterar o tempo\nEscolha: "))
            else:
                objeto_unico = Tarefa.objeto_unico(verificacao-1)
                if escolha == 1:
                    objeto_unico.nome = input("Insira o novo nome: ")
                    return print("O nome da tarefa foi alterado com sucesso!\n")
                else:
                    objeto_unico.tempo = int(input("Insira o novo tempo para a tarefa: "))
                    return print("O tempo da tarefa foi alterado com sucesso!\n")
                
    @staticmethod
    def verificacao_lista():
        if len(objetos) == 0:
            return False
        else:
            return True

class Metodos: #classe criada para organizar as funções que serão usadas

    @staticmethod
    def primeira_acesso(verificacao):       #faz a verificação da lista para o primeiro acesso 
        if verificacao == False:
            escolha = int(input("Você não possui nenhuma tarefa\n1 - Adicionar tarefa\n2 - Restaurar tarefas\n0 - Fechar programa\nEscolha: "))
            while escolha not in [0, 1, 2]:
                escolha = int(input("Opção inválida. Por favor, insira novamente.\nEscolha: "))
            else:
                if escolha == 0:
                    return 0
                elif escolha == 1:
                    nome, tempo = input("insira o nome da tarefa: "), int(input("Insira o tempo para realizar a tarefa: "))
                    Tarefa.adicionar_tarefa(Tarefa(nome, tempo))
                elif escolha == 2:
                    Metodos.restaurar()
    
        else:
            funcionalidade = int(input("\nInsira a opção desejada:\n1 - Adicionar tarefa\n2 - visualizar tarefas\n3 - Excluir tarefa\n4 - Editar tarefa\n5 - Salvar tarefas\n0 - Encerrar programa\nEscolha: "))
            while funcionalidade < 0 and funcionalidade > 4:
                funcionalidade = int(input("\nOpção inválida. Insira novamente\nEscolha: "))
            else:
                return funcionalidade           #retorna a escolha da funcionalidade pelo usuário

    @staticmethod
    def salvar():
        for i in range(len(objetos)):
            dicio = {}
            objeto_tarefa  = Tarefa.objeto_unico(i)
            dicio[f"{objeto_tarefa.nome}"] = objeto_tarefa.tempo
            #print(dicio)
            with open("Projects/Python/assistente_tarefas/tarefas.json", "w") as arq:
                json.dump(dicio, arq)

    @staticmethod
    def restaurar():
        with open("Projects/Python/assistente_tarefas/tarefas.json") as arq:
            arq = json.load(arq)
        for i, j in arq.items():
            Tarefa.adicionar_tarefa(Tarefa(i, j))
        pass
            
def main():

    while True:
        funcionalidade_escolhida = Metodos.primeira_acesso(Tarefa.verificacao_lista())
        if funcionalidade_escolhida == 1:
            nome = input("Insira o nome da tarefa: ")
            tempo = int(input("Insira o tempo para concluir a tarefa: "))
            Tarefa.adicionar_tarefa(Tarefa(nome, tempo))
        elif funcionalidade_escolhida == 2:
            Tarefa.visualizar_tarefa()
        elif funcionalidade_escolhida == 3:
            Tarefa.excluir_tarefa()
        elif funcionalidade_escolhida == 4:
            Tarefa.editar_tarefa()
        elif funcionalidade_escolhida == 5:
            Metodos.salvar()
        elif funcionalidade_escolhida == 6:
            Metodos.restaurar()
        elif funcionalidade_escolhida == 0:
            print("Programa Encerrado")
            break
        else:
            pass

print("="*21, "\nAssistente de tarefas")
print("="*21)
main()