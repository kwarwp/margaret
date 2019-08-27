# margaret.angie.main.py
from _spy.vitollino.main import Cena
CENA = "https://i.imgur.com/6NNu6ps.jpg"
TESOURO = "https://i.imgur.com/nBbQxbD.jpg"
COBRA = "https://i.imgur.com/ow7s2gK.jpg"
templo = Cena (CENA).vai()
tesouro = Cena(TESOURO).vai()
cobra = Cena (COBRA).vai()
templo.direita = tesouro
templo.vai()
tesouro.esquerda = templo
templo.vai()
tesouro.direita = cobra
templo.vai()
cobra.esquerda = tesouro
templo.vai()