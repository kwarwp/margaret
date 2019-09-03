# margaret.libby.main.py
from _spy.vitollino.main import Cena 
from stacy.main import DIC["FOGO"]
#IMAGENS = ["CENA", "TESOURO"]
DIC = DICIONARIO_DE_IMAGENS = {}
DIC["CENA"] = "https://i.imgur.com/q4Cznxt.jpg"
DIC["TESOURO"] = "https://i.imgur.com/x2wLF9U.jpg"

class Inca:
    def inicia(self):
        templo = Cena(DIC["CENA"])
        tesouro = Cena(DIC["TESOURO"])
        templo.direita = tesouro
        tesouro.esquerda = templo
        tesouro.direita = fogo
        fogo.esquerda = tesouro
        tesouro.esquerda = templo
        templo.vai()
    
inca = Inca()
 
if __name__ == "__main__":
     inicia.inicia()