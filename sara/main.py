# margaret.sara.main.py
from _spy.vitollino.main import Cena
CENA = "https://i.imgur.com/ZzWag8V.jpg"
TESOURO = "https://i.imgur.com/0t0j5Ne.jpg"
templo = Cena(CENA).vai()
tesouro = Cena(TESOURO).vai()
templo.direita = tesouro
tesouro.esquerda = templo
MONSTRO = "https://i.imgur.com/zwbxMeu.jpg"
monstro = Cena(MONSTRO).vai()
tesouro.direita = monstro
monstro.esquerda = tesouro
PEDRAS = "https://i.imgur.com/fvnFDJl.jpg"
pedras = Cena(PEDRAS).vai()
monstro.direita = pedras
pedras.esquerda = monstro
templo.vai()
