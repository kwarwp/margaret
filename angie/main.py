# margaret.angie.main.py
from _spy.vitollino.main import Cena
CENA = "https://i.imgur.com/6NNu6ps.jpg"
TESOURO = "https://i.imgur.com/nBbQxbD.jpg"
templo = Cena (CENA).vai()
tesouro = Cena(TESOURO).vai()
templo.direita = tesouro
templo.vai()
tesouro.esquerda = templo