#incluir biblioteca caso necessidade
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
            return print("Tarefa adicionada com sucesso")
        except:
            return print("Não foi possível adicionar a tarefa")

    @staticmethod
    def objeto_unico(index):
        objeto_unic = objetos[index]
        return objeto_unic

    @staticmethod
    def visualizar_tarefa():
        if len(objetos) > 0:
            for i, objeto in enumerate(objetos):
                return print(f"{i+1} - {objeto.nome}")

    @staticmethod
    def excluir_tarefa():
        print("Selecione a tarefa que deseja excluir: ")
        Tarefa.visualizar_tarefa()
        escolha = int(input("Selecione o número da tarefa que deseja excluir.\nEscolha: "))
        if escolha != 0 and escolha <= len(objetos):
            objetos.pop(escolha)
            return print("Tarefa apagada com sucesso.")
        else:
            return print("Falha ao excluir objeto!")
        
    @staticmethod
    def editar_tarefa():
        print("Selecione a tarefa que deseja editar:\n")
        Tarefa.visualizar_tarefa()
        verificacao = int(input("Escolha o número da tarefa:\nEscolha: "))
        if verificacao > 0 and verificacao <= len(objetos):
            escolha = int(input("O que você deseja alterar?\n1 - Nome\n2 - Tempo\nEscolha: "))
            while escolha != 1 and escolha != 2:
                escolha = int(input("Valor incorreto! Insira 1 para alterar o nome ou 2 para alterar o tempo\nEscolha: "))
            else:
                objeto_unico = Tarefa.objeto_unico(escolha-1)
                if escolha == 1:
                    objeto_unico.nome = input("Insira o novo nome: ")
                    return print("O nome da tarefa foi alterado com sucesso!")
                else:
                    objeto_unico.tempo = int(input("Insira o novo tempo para a tarefa: "))
                    return print("O tempo da tarefa foi alterado com sucesso!")
    @staticmethod
    def verificacao_lista():
        if len(objetos) == 0:
            return False
        else:
            return True

    @staticmethod
    def criar_documento():
        pass

class Metodos:

    @staticmethod
    def primeira_acesso(verificacao):
        if verificacao == False:
            escolha = int(input("Você não possui nenhuma tarefa\n1 - Adicionar tarefa\n0 - Fechar programa\nEscolha: "))
            while escolha != 1 and escolha != 0:
                escolha = int(input("Opção inválida. Por favor, insira novamente\nEscolha"))
            else:
                if escolha == 0:
                    return print("Programa encerrado")
                elif escolha == 1:
                    nome, tempo = input("insira o nome da tarefa: "), int(input("Insira o tempo para realizar a tarefa: "))
                    Tarefa.adicionar_tarefa(Tarefa(nome, tempo))
        else:
            funcionalidade = int(input("Insira a opção desejada:\n1 - Adicionar tarefa\n2 - visualizar tarefas\n3 - Excluir tarefa\n4 - Editar tarefa\nEscolha: "))
            return funcionalidade

def main(funcionalide):
    pass


main(Metodos.primeira_acesso(Tarefa.verificacao_lista()))