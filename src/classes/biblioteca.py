import json
import os
from typing import List
from src.classes.livro import Livro

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
CAMINHO_DADOS = os.path.join(BASE_DIR, "dados", "biblioteca.json")


#Fazer o crud

class Biblioteca:

    # Alterei o construtor para receber apenas a lista de livros, a quantidade de livros é recebida automaticamente pela quantidade de elementos da array de livros.
    def __init__(self, livros : List[Livro] | None = None):
        self.livros = livros if livros else []
        self.qntLivros = len(self.livros)
    
    def adicionarLivro(self, livro: Livro):
        self.livros.append(livro)
    
    def salvarDados(self, caminho=CAMINHO_DADOS):
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(
                [livro.salvarDadosDict() for livro in self.livros],
                arquivo,
                indent=4,
                ensure_ascii=False
            )
    
    @staticmethod
    def carregarDados(caminho=CAMINHO_DADOS):
        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read().strip()
                if not conteudo:
                    return Biblioteca()
                dados = json.loads(conteudo)
                livros = [Livro.carregarDadosDict(d) for d in dados]
                return Biblioteca(livros)
        except FileNotFoundError:
            return Biblioteca()
        except json.JSONDecodeError:
            return Biblioteca()
    