# margaret.lisa.main.py
from _spy.vitollino.main import Cena
from stacy.main import fogo
CENA = "https://i.imgur.com/7GZetDn.jpg"
TESOURO = "https://i.imgur.com/h8MfuRD.jpg"
templo = Cena(CENA)
tesouro = Cena(TESOURO)
templo.direita = tesouro
tesouro.esquerda = templo
tesouro.direita = fogo
templo.vai()