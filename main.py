import datetime
from typing import List, Optional
from src.classes.livro import Livro
from src.classes.biblioteca import Biblioteca



def main():
    biblioteca = Biblioteca.carregarDados()

    if not biblioteca.livros:
        x = Livro(12,"b","c","d", False)
        biblioteca.adicionarLivro(x)
    else:
        x = biblioteca.livros[0]
    
    for livro in biblioteca.livros:
        print(livro.salvarDadosDict())
    
    y = x.informacoesLivro()
    print(y)
    x.alugarLivro(23)
    print(y)
    x.devolverLivro()
    print(y)
    x.alugarLivro(23)
    x.atualizarInfo('dataAlugado', datetime.date(2012, 10, 1))
    print(y)

    biblioteca.salvarDados()



if __name__ == "__main__":
    main()
