# margaret.lisa.main.py
from _spy.vitollino.main import Cena
CENA = "https://i.imgur.com/ysHJLhg.jpg"
MONSTRO = "https://i.imgur.com/cHd7w24.jpg"

templo = Cena(CENA)
monstro = Cena(MONSTRO)

templo.direita = monstro
monstro.esquerda = templo

templo.vai()