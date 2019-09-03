# margaret.courtney.main.py
from _spy.vitollino.main import Cena 
CENA = "https://i.imgur.com/IdXGTYa.jpg"
TESOURO = "https://i.imgur.com/78iHROq.jpg"
COBRA = "https://i.imgur.com/7G66ctJ.png"
FOGO = "https://i.imgur.com/76RAEGh.jpg"

class Inca:
    def inicia(self):
        templo = Cena (CENA).vai()
        tesouro = Cena(TESOURO).vai()
        cobra = Cena (COBRA).vai()
        fogo = Cena (FOGO).vai()
        templo.direita = tesouro
        templo.vai()
        tesouro.esquerda = templo
        tesouro.direita = cobra
        cobra.esquerda = tesouro
        cobra.direita = fogo
        fogo.esquerda = cobra 

inca = Inca()
inca.inicia()