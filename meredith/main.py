# margaret.meredith.main.py
from _spy.vitollino.main import Cena
from stacy.main import fogo
CENA = "https://i.imgur.com/7GZetDn.jpg"
TESOURO = "https://i.imgur.com/h8MfuRD.jpg"

class Inca:
    def inicia(self):
        templo = Cena(CENA)
        tesouro = Cena(TESOURO)
        templo.direita = tesouro
        tesouro.esquerda = templo
        tesouro.direita = fogo
        fogo.esquerda = tesouro
        templo.vai()

inca = Inca()
inca.inicia()
    