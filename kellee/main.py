# margaret.kellee.main.py
from _spy.vitollino.main import Cena
CENA = "https://i.imgur.com/F0pWLRM.png"
Cena(CENA).vai()
TESOURO = "https://i.imgur.com/Z2CD83L.jpg"
templo = Cena(CENA)
tesouro = Cena(TESOURO)
templo.direita = tesouro
tesouro.esquerda = templo
templo.vai()
MONSTRO = "https://i.imgur.com/4cBiZ6n.jpg"
monstro = Cena(MONSTRO)
monstro.direita = tesouro
monstro.esquerda = templo
monstro.vai()

