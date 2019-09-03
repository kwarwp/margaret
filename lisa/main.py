# margaret.lisa.main.py
__author__ = "Carlo E. T. Oliveira carlo@ufrj.br"
from _spy.vitollino.main import Cena
#from stacy.main import fogo
#from natalia.main import sereiamonstro
#IMAGENS = ["CENA", "TESOURO"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/7GZetDn.jpg"
DI["TESOURO"] = "https://i.imgur.com/h8MfuRD.jpg"

class Inca:
    def inicia(self):
        templo = Cena(DI["TEMPLO"])
        tesouro = Cena(DI["TESOURO"])
        templo.direita = tesouro
        tesouro.esquerda = templo
        #tesouro.direita = fogo
        #fogo.esquerda = tesouro
        templo.vai()
        
class Carta:
    def __init__(self):
        self.carta = Cena(DI["TESOURO"])
    def baralho(self):
        return [self.carta]
        
class Jogo:
    def __init__(self):
        self.baralho = Carta().baralho()
        self.templo = Cena(DI["TEMPLO"])
        self.templo.direita = self.baralho[0]
    def inicia(self):
        self.templo.vai()
        

inca = Jogo()  # Inca()

if __name__ == "__main__":
    inca.inicia()
    