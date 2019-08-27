# margaret.libby.main.py
from _spy.vitollino.main import Cena 
from stacy.main import fogo
CENA = "https://i.imgur.com/q4Cznxt.jpg"
TESOURO = "https://i.imgur.com/x2wLF9U.jpg"
templo = Cena(CENA)
tesouro = Cena(TESOURO)
templo.direita = tesouro
tesouro.esquerda = templo
tesouro.direita = fogo
fogo.esquerda = tesouro
tesouro.esquerda = templo
templo.vai()