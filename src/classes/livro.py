import datetime
from typing import List, Optional


class Livro:

    def __init__(self, id : int, nomeLivro : str, genero : str, autor : str, alugado : bool):
        self.id : int = id
        self.nomeLivro : str = nomeLivro
        self.genero : str = genero
        self.autor : str = autor

        self.dataRegistro : datetime.date = datetime.datetime.date(datetime.datetime.today())
        self.dataAlugado : datetime.date  = None
        self.dataRetorno : datetime.date  = None
        
        self.alugado : bool = alugado

    def informacoesLivro(self):
        return (self.__dict__)

    def alugarLivro(self, diasAteRetorno : int):
        self.dataAlugado = datetime.datetime.date(datetime.datetime.today())
        self.dataRetorno = datetime.timedelta(days=diasAteRetorno) + self.dataAlugado
        self.alugado = True
        return
    
    def devolverLivro(self):
        self.dataAlugado = None
        self.dataRetorno = None
        self.alugado = False
        return
    
    def atualizarInfo(self, atributo, dadoAtualizado):
        
        match atributo:

            case 'id':
                self.id = dadoAtualizado
                

            case 'nomeLivro':
                self.nomeLivro = dadoAtualizado
                

            case 'genero':
                self.genero = dadoAtualizado


            case 'autor':
                self.autor = dadoAtualizado


            case 'dataRegistro':
                self.dataRegistro = dadoAtualizado


            case 'dataAlugado':
                tdelta = self.dataRetorno - self.dataAlugado
                self.dataAlugado = dadoAtualizado
                self.dataRetorno = dadoAtualizado + tdelta 


            case 'alugado':
                self.genero = dadoAtualizado
                
        return

