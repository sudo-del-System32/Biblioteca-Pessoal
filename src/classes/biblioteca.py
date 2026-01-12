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
        self.qntLivros += 1
    
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
    

    def listar_livros(self):
        for livro in self.livros:
            print("Id: {}".format(livro.id))
            print("Nome: {}".format(livro.nomeLivro))
            print("Genero: {}".format(livro.genero))
            print("Data de registro: {}".format(livro.autor))
            
            if(livro.alugado):
                print("Data que foi alugado: {}/{}/{}".format(livro.dataRegistro.day, livro.dataRegistro.month, livro.dataRegistro.year)) 
                print("Data que sera devolvido: {}/{}/{}".format(livro.dataRegistro.day, livro.dataRegistro.month, livro.dataRegistro.year))
            else:
                print("O livro ainda esta na biblioteca!")
            print("")

    def alugar_livro(self, id, dias):
        for livro in self.livros:
            if livro.id == id and livro.alugado == False:
                livro.alugarLivro(dias)
                return True

        return False
    
    def devolver_livro(self, id):
        for livro in self.livros:
            if livro.id == id:
                livro.devolverLivro()
                return True
        return False
    
    def editar_livro(self, id_livro, atributo, novo):
        for livro in self.livros:
            if livro.id == id_livro:
                livro.atualizarInfo(atributo=atributo, dadoAtualizado=novo)
                return True
        return False
    
    def remover_livro(self, id_livro):
        for livro in self.livros:
            if livro.id == id_livro:
                self.contagem_corrigir(livro.id)
                self.livros.remove(livro)
                return True
        return False

    def contagem_corrigir(self, id_livro_removido : int):
        for i in range(id_livro_removido - 1, self.qntLivros, 1):
            self.livros[i].id = i