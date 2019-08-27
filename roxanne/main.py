# margaret.roxanne.main.py
from _spy.vitollino.main import Cena 
CENA = "https://i.imgur.com/XY8get8.jpg"
MONSTRO = "https://i.imgur.com/ZOoZ2aQ.jpg"
OURO = "https://i.imgur.com/4L5y1To.jpg"
caverna = Cena(CENA)
monstro = Cena(MONSTRO)
ouro = Cena(OURO)
caverna.direita = monstro
monstro.esquerda = caverna
caverna.vai()
monstro.direita = ouro
ouro.esquerda = monstro
monstro.vai()