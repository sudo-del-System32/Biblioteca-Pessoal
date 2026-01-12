import datetime
from typing import List, Optional


class Livro:

    def __init__(self, id : int, nomeLivro : str, genero : str, autor : str, alugado : bool):
        self.id : int = id
        self.nomeLivro : str = nomeLivro
        self.genero : str = genero
        self.autor : str = autor

        self.dataRegistro : datetime.date = datetime.datetime.date(datetime.datetime.today())

        self.alugado : bool = alugado

        if(alugado):
            self.alugarLivro()
        else:
            self.dataAlugado : datetime.date  = None
            self.dataRetorno : datetime.date  = None



    def informacoesLivro(self):
        return (self.__dict__)

    def alugarLivro(self, diasAteRetorno : int = -1):
        self.dataAlugado = datetime.datetime.date(datetime.datetime.today())
        
        if(diasAteRetorno != -1):
            self.dataRetorno = datetime.timedelta(days=diasAteRetorno) + self.dataAlugado
        else:
            self.dataRetorno = None

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
    
    
    def salvarDadosDict(self):
        return {
            "id": self.id,
            "nomeLivro": self.nomeLivro,
            "genero": self.genero,
            "autor": self.autor,
            "dataRegistro": self.dataRegistro.isoformat(),
            "dataAlugado": self.dataAlugado.isoformat() if self.dataAlugado else None,
            "dataRetorno": self.dataRetorno.isoformat() if self.dataRetorno else None,
            "alugado": self.alugado
        }
    
    @staticmethod
    def carregarDadosDict(dados: dict):
        livro = Livro(
            dados["id"],
            dados["nomeLivro"],
            dados["genero"],
            dados["autor"],
            dados["alugado"]
        )

        livro.dataRegistro = datetime.date.fromisoformat(dados["dataRegistro"])
        livro.dataAlugado = (
            datetime.date.fromisoformat(dados["dataAlugado"])
            if dados["dataAlugado"] else None
        )
        livro.dataRetorno = (
            datetime.date.fromisoformat(dados["dataRetorno"])
            if dados["dataRetorno"] else None
        )

        return livro


