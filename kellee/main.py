# margaret.kellee.main.py
from _spy.vitollino.main import Cena
IMAGENS = ["CENA", "TESOURO", "MONSTRO", "FOGO", "PEDRAS"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/F0pWLRM.png"
DI["TESOURO"] = "https://i.imgur.com/Z2CD83L.jpg"
DI["MONSTRO"] = "https://i.imgur.com/4cBiZ6n.jpg"
DI["FOGO"] = "https://imgur.com/AVBV4TF"
DI["PEDRAS"] = "https://i.imgur.com/rpIsgaD.png"

class Inca:
    def inicial(self):
        templo = Cena (DI["CENA"])
        tesouro = Cena (DI["TESOURO"])
        monstro = Cena (DI["MONSTRO"])
        fogo = Cena (DI["FOGO"])
        pedras = Cena (DI["PEDRAS"])
        templo.direita = tesouro
        tesouro.esquerda = templo
        tesouro.direita = monstro
        monstro.esquerda = fogo
        fogo.direita = pedras 
        templo.vai()
    
inca = Inca()

if __name__ == "__main__":
    inca.inicia()