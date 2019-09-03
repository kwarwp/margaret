# margaret.angie.main.py
from _spy.vitollino.main import Cena
IMAGENS = ["CENA", "TESOURO", "COBRA", "FOGO"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/6NNu6ps.jpg"
DI["TESOURO"] = "https://i.imgur.com/nBbQxbD.jpg"
DI["COBRA"] = "https://i.imgur.com/0paGPPh.jpg"
DI["FOGO"] = "https://i.imgur.com/ScR01C1.png"
DI["MONSTRO"] = "https://i.imgur.com/C487QGN.jpg"

class Inca:
    def inicia(self):
        templo = Cena (DI["CENA"])
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

inca = Inca()

if __name__ == "__main__":
    inca.inicia()