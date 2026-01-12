import datetime
from typing import List, Optional
from src.classes.livro import Livro
from src.classes.biblioteca import Biblioteca
from src.menu.menu import Menu



def main():
    biblioteca = Biblioteca.carregarDados()

    if not biblioteca.livros:
        biblioteca.adicionarLivro(Livro(biblioteca.qntLivros + 1, "Crime e Castigo", "Romance", "Fiódor Dostoiévski", False))
        biblioteca.adicionarLivro(Livro(biblioteca.qntLivros + 1, "A Mansão Hollow", "Romance policial", "A Mansão Hollow", False))
        biblioteca.adicionarLivro(Livro(biblioteca.qntLivros + 1, "Gaston Leroux", "Romance francês de ficção gótica,", "Gaston Leroux", False))
        biblioteca.adicionarLivro(Livro(biblioteca.qntLivros + 1, "Anne de Green Gables", "Romance canadense", "Montgomery, L. M. (Lucy Maud)", False))
        biblioteca.adicionarLivro(Livro(biblioteca.qntLivros + 1, "O Pequeno Príncipe", "Literatura Infanto-Juvenil, Novela", "O Pequeno Príncipe", False))
    else:
        x = biblioteca.livros[0]
        
    menu = Menu(biblioteca=biblioteca)
    menu.executar()

    biblioteca.salvarDados()



if __name__ == "__main__":
    main()
