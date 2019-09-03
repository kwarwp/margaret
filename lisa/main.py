# margaret.lisa.main.py
__author__ = "Carlo E. T. Oliveira carlo@ufrj.br"
from _spy.vitollino.main import Cena
#from stacy.main import fogo
#from natalia.main import sereiamonstro
#IMAGENS = ["CENA", "TESOURO"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/7GZetDn.jpg"
DI["TESOURO"] = "https://i.imgur.com/h8MfuRD.jpg"

class Inca:
    def inicia(self):
        templo = Cena(DI["CENA"])
        tesouro = Cena(DI["TESOURO"])
        templo.direita = tesouro
        tesouro.esquerda = templo
        #tesouro.direita = fogo
        #fogo.esquerda = tesouro
        templo.vai()
        
class Jogo:
    pass

inca = Inca()

if __name__ == "__main__":
    inca.inicia()
    