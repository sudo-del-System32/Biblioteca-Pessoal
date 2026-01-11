import datetime
from typing import List, Optional
from src.classes.livro import Livro
from src.classes.biblioteca import Biblioteca



def main():
    x = Livro(12,"b","c","d", False)
    y = x.informacoesLivro()
    print(y)
    x.alugarLivro(23)
    print(y)
    x.devolverLivro()
    print(y)
    x.alugarLivro(23)
    x.atualizarInfo('dataAlugado', datetime.date(2012, 10, 1))
    print(y)


if __name__ == "__main__":
    main()
