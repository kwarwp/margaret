# margaret.angie.main.py
from _spy.vitollino.main import Cena
IMAGENS = ["CENA", "TESOURO", "COBRA", "FOGO"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/6NNu6ps.jpg"
DI["TESOURO"] = "https://i.imgur.com/nBbQxbD.jpg"
DI["COBRA"] = "https://i.imgur.com/Lh1O87Q.jpg"
DI["FOGO"] = "https://i.imgur.com/ScR01C1.png"
DI["MONSTRO"] = "https://i.imgur.com/nvWMlWx.jpg"

class Inca:
    def inicia(self):
        templo = Cena (DI["TEMPLO"])
        tesouro = Cena (DI["TESOURO"])
        cobra = Cena (DI["COBRA"])
        fogo = Cena (DI["FOGO"])
        monstro = Cena (DI["MONSTRO"])
        templo.direita = tesouro
        tesouro.esquerda = templo
        tesouro.direita = cobra
        cobra.esquerda = tesouro
        cobra.direita = fogo
        fogo.esquerda = cobra 
        fogo.direita = monstro
        monstro.esquerda = fogo
        templo.vai()

class Carta:
    pass
    def baralho(self)
        return []
    
class Jogo:
    def __init__(self)
        self.baralho = Carta().baralho()
        self.templo = Cena(DI["TEMPLO"])
    pass

inca = Inca()

if __name__ == "__main__":
    inca.inicia()