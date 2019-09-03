# margaret.naomi.main.py
from _spy.vitollino.main import Cena
from stacy.main import fogo
IMAGENS = ["CENA", "TESOURO"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/inzdUaq.jpg"
DI["TESOURO"] = "https://i.imgur.com/DJNXWXY.jpg"

class Inca:
    def inicia(self):
        templo = Cena(DI["CENA"])
        tesouro = Cena(DI["TESOURO"])
        templo.dieita = tesouro
        tesouro.esquerda = templo
        tesouro.direita = fogo
        fogo.esquerda = tesouro
        templo.vai()
    
inca = Inca()

if__name__ == "__main__":
   inca.inicia() 
   