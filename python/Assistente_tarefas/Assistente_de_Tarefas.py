#incluir biblioteca caso necessidade
pass

objetos = []

#iniciar a classe principal
class Tarefa:

    def __init__(self, nome, tempo):
        self.nome = nome
        self.tempo = int(tempo)

    @staticmethod
    def adicionar_tarefa(nome, tempo):
        objeto = Tarefa(nome, tempo)
        try:
            objetos.append(objeto)
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
                objeto_unico = Tarefa.objeto_unico()
                if escolha == 1:
                    objeto_unico.nome = input("Insira o novo nome: ")
                    return print("O nome da tarefa foi alterado com sucesso!")
                else:
                    objeto_unico.tempo = int(input("Insira o novo tempo para a tarefa: "))
                    return print("O tempo da tarefa foi alterado com sucesso!")

    @staticmethod
    def criar_documento():
        pass

#criar logica para menu principal