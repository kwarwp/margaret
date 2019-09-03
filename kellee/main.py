# margaret.kellee.main.py
__author__ = "Bárbara Juliana C.Soares barbara_ju07@hotmail.com"
from _spy.vitollino.main import Cena
IMAGENS = ["CENA", "TESOURO", "MONSTRO", "FOGO", "PEDRAS"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/F0pWLRM.png"
DI["TESOURO"] = "https://i.imgur.com/Z2CD83L.jpg"
DI["MONSTRO"] = "https://i.imgur.com/4cBiZ6n.jpg"
DI["FOGO"] = "https://i.imgur.com/qLYrtR0.jpg"
DI["PEDRAS"] = "https://i.imgur.com/rpIsgaD.png"

class Inca:
    def inicia(self):
        templo = Cena(DI["CENA"])
        tesouro = Cena(DI["TESOURO"])
        monstro = Cena(DI["MONSTRO"])
        fogo = Cena(DI["FOGO"])
        pedras = Cena(DI["PEDRAS"])
        templo.direita = tesouro
        tesouro.esquerda = templo
        tesouro.direita = monstro
        monstro.esquerda = fogo
        fogo.direita = pedras 
        pedras.esquerda = templo
        templo.vai()
    
class Carta:
    pass
    def baralho(self):
        return []
        

class Jogos:
    def __init__(self):
        self.baralho = carta().baralho()
        self.templo = Cena(DI["TEMPLO"])
    def inicia(self):
        pass
        
        
inca = Jogo()  # Inca()

if __name__ == "__main__":
    inca.inicia()