# margaret.angie.main.py
from _spy.vitollino.main import Cena
CENA = "https://i.imgur.com/6NNu6ps.jpg"
TESOURO = "https://i.imgur.com/nBbQxbD.jpg"
COBRA = "https://i.imgur.com/0paGPPh.jpg"
FOGO = "https://i.imgur.com/ScR01C1.png"
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