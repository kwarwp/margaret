# margaret.roxanne.main.py
from _spy.vitollino.main import Cena 
CENA = "https://i.imgur.com/XY8get8.jpg"
MONSTRO = "https://i.imgur.com/ZOoZ2aQ.jpg"
TESOURO = "https://i.imgur.com/4L5y1To.jpg"
caverna = Cena(CENA)
monstro = Cena(MONSTRO)
tesouro = Cena(TESOURO)
caverna.direita = monstro
monstro.esquerda = caverna
caverna.vai()
monstro.direira = tesouro
tesouro.esquerda = monstro
monstro.vai()
