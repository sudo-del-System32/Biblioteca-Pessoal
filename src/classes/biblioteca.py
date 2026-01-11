from typing import List
from src.classes.livro import Livro

#Fazer o crud

class Biblioteca:

    def __init__(self, livros : List[Livro], qntLivros : int):
        self.livros : List[Livro] = livros
        self.qntLivros : int = qntLivros

    