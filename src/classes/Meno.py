import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

class Cores:
    RESET = "\033[0m"
    AZUL = "\033[1;36m"
    VERDE = "\033[1;32m"
    VERMELHO = "\033[1;31m"
    AMARELO = "\033[1;33m"
    CINZA = "\033[1;90m"
    ROXO = "\033[1;35m"       
    LILAS = "\033[38;5;93m"

class Menu:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def mostrar_menu(self):
        limpar_tela()
        print(Cores.AMARELO + "~~~~~~*~~~~~*~~~~~*~~~~~~*~~~~~~" + Cores.RESET)
        print(Cores.LILAS + " ✨📜 BIBLIOTECA ALEXANDRIA 📜✨   " + Cores.RESET)
        print(Cores.AMARELO + "~~~~~~*~~~~~*~~~~~*~~~~~~*~~~~~~\n" + Cores.RESET)

    
        print(Cores.CINZA + " Para os amantes da leitura, escolha a função que desejas" + Cores.RESET)
        print(Cores.CINZA + " Nem mesmo a chama da ignorância pode destruir o acervo criado aqui \n" + Cores.RESET)
        

        print(Cores.VERDE + "[1]" + Cores.RESET + " Cadastrar livro")
        print(Cores.VERDE + "[2]" + Cores.RESET + " Listar livros")
        print(Cores.VERDE + "[3]" + Cores.RESET + " Alugar livro")
        print(Cores.VERDE + "[4]" + Cores.RESET + " Devolver livro")
        print(Cores.VERDE + "[5]" + Cores.RESET + " Editar livro")
        print(Cores.VERDE + "[6]" + Cores.RESET + " Remover livro")
        print(Cores.VERMELHO + "[0]" + Cores.RESET + " Sair\n")

    def executar(self):
        while True:
            self.mostrar_menu()
            opcao = input(Cores.AMARELO + "Escolha uma opção: " + Cores.RESET)

            if opcao == "1":
                print(Cores.AMARELO + "Insira o livro aqui" + Cores.RESET)
                limpar_tela()
                nome = input("Informe o nome do livro: ")
                genero = input("Informe o gênero: ")
                autor = input("Informe o autor: ")
                
                # self.biblioteca.cadastrar_livro(nome, genero, autor)

                print(Cores.VERDE + "\nMais um livro no acervo! Nossa biblioteca enriquece a cada adição" + Cores.RESET)
                input("\nPressione ENTER para continuar!")

            elif opcao == "2":
                limpar_tela()
                print(Cores.AMARELO + "Aqui estão os livros da sua biblioteca:" + Cores.RESET)

                # self.biblioteca.listar_livros()
                input("\nPressione ENTER para continuar!")

            elif opcao == "3":
                limpar_tela()
                print(Cores.AMARELO + "Desejas alugar um livro? Registre aqui!" + Cores.RESET)
                
                id_livro = input("Informe o ID do livro: ")
                dias = input("Quantos dias de empréstimo? ")

                # self.biblioteca.alugar_livro(int(id_livro), int(dias))

                print(Cores.VERDE + "\nProntinho, só não esqueca de cobrar seu retorno!" + Cores.RESET)
                input("\nPressione ENTER para continuar!")

            elif opcao == "4":
                limpar_tela()
                print(Cores.AMARELO + "Retorne um livro ao acervo" + Cores.RESET)

                id_livro = input("Informe o ID do livro a ser devolvido: ")
                # self.biblioteca.devolver_livro(int(id_livro))

                print(Cores.VERDE + "\nSeu acervo agradece! É sagrado manter todo o máximo conhecimento, sem perdas!" + Cores.RESET)
                input("\nPressione ENTER para continuar!")

            elif opcao == "5":
                limpar_tela()
                print(Cores.AMARELO + "Edite detalhes incorretos de um Livro" + Cores.RESET)
                
                id_livro = input("Primeiro, informe o ID do livro: ")

                print("\nO que desejas alterar?")
                print("[1] Nome")
                print("[2] Gênero")
                print("[3] Autor")

                escolha = input("Escolha: ")

                if escolha == "1":
                  novo = input("Novo nome: ")
                  atributo = "nomeLivro"
                elif escolha == "2":
                  novo = input("Novo gênero: ")
                  atributo = "genero"
                elif escolha == "3":
                  novo = input("Novo autor: ")
                  atributo = "autor"
                else:
                  print("Por obséquio, selecione corretamente")
                  continue

                 # self.biblioteca.editar_livro(int(id_livro), atributo, novo)

                print(Cores.VERDE + "\nInformações prontamente atualizadas!" + Cores.RESET)
                input("\nPressione ENTER para continuar!")

            elif opcao == "6":
                limpar_tela()
                print(Cores.AMARELO + "Acidentes acontecem.. Retire um livro da biblioteca" + Cores.RESET)

                id_livro = input("Informe o ID do livro que será retirado: ")
                 # self.biblioteca.remover_livro(int(id_livro))

                print(Cores.VERDE + "\nEspero que a ausência seja recompensada com novos que virão.." + Cores.RESET)
                input("\nPressione ENTER para continuar!")

            elif opcao == "0":
                limpar_tela()
                print(Cores.CINZA + "\nAcabamos por aqui.. mas lembre-se! Conhecimento é poder " + Cores.RESET)
                break
                

            else:
                print(Cores.VERMELHO + "\nGuie-se apenas pelos numeros indicados!" + Cores.RESET)
                input("Pressione ENTER para tentar novamente...")
              

