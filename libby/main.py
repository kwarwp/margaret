# margaret.libby.main.py
from _spy.vitollino.main import Cena 
CENA = "https://i.imgur.com/q4Cznxt.jpg"
TESOURO = "https://i.imgur.com/x2wLF9U.jpg"
templo = Cena(CENA)
tesouro = Cena(TESOURO)
templo.direita = tesouro
tesouro.esquerda = templo
templo.vai()