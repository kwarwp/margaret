# margaret.roxanne.main.py
from _spy.vitollino.main import Cena 
CENA = "https://i.imgur.com/XY8get8.jpg"
MONSTRO = "https://i.imgur.com/ZOoZ2aQ.jpg"
TESOURO = "https://i.imgur.com/4L5y1To.jpg"
guardado = Cena(CENA)
caverna = Cena(CENA)
monstro = Cena(MONSTRO)
caverna.direita = monstro
monstro.esquerda = caverna
monstro.direita = guardado
caerna.vai()

