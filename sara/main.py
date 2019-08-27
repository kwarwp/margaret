# margaret.sara.main.py
from _spy.vitollino.main import Cena
CENA = "https://i.imgur.com/ZzWag8V.jpg"
ARTEFATO = "https://i.imgur.com/0t0j5Ne.jpg"
MONSTRO = "https://i.imgur.com/zwbxMeu.jpg"
PEDRAS = "https://i.imgur.com/fvnFDJl.jpg"

class Inca:
    def inicia(self):
        templo = Cena(CENA).vai()
        artefato = Cena(ARTEFATO).vai()
        templo.direita = artefato
        artefato.esquerda = templo
        monstro = Cena(MONSTRO).vai()
        artefato.direita = monstro
        monstro.esquerda = artefato
        pedras = Cena(PEDRAS).vai()
        monstro.direita = pedras
        pedras.esquerda = monstro
        templo.vai()
