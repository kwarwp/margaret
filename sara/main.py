# margaret.sara.main.py
__author__ = "Luiza Busnardo busnardo.luiza@gmail.com"

from _spy.vitollino.main import Cena, STYLE
STYLE["width"] = 600
STYLE["height"] = 600
from random import shuffle
IMAGENS = ["CENA", "ACAMPAMENTO", "MOCHILA", "ARTEFATO1", "MONSTRO", "PEDRAS", "FOGO", "DESABAMENTO", "COBRA", "ARANHA", "SALADOTESOURO", "OBSIDIANA", "TURQUESA", "PEPITADEOURO"]*5
shuffle(IMAGENS)
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/ZzWag8V.jpg"
DI["ACAMPAMENTO"] = "https://i.imgur.com/3QWHNYM.jpg"
DI["MOCHILA"] = "https://i.imgur.com/UCQvviq.jpg"
DI["ARTEFATO1"] = "https://i.imgur.com/0t0j5Ne.jpg"
DI["MONSTRO"] = "https://i.imgur.com/zwbxMeu.jpg"
DI["PEDRAS"] = "https://i.imgur.com/fvnFDJl.jpg"
DI["FOGO"] = "https://i.imgur.com/sIq24MI.jpg"
DI["DESABAMENTO"] = "https://i.imgur.com/iEjnRsA.jpg"
DI["COBRA"] = "https://i.imgur.com/BRCXuz3.jpg"
DI["ARANHA"] = "https://i.imgur.com/VxTxDTj.jpg"
DI["SALADOTESOURO"] = "https://i.imgur.com/PQV7tEW.jpg"
DI["OBSIDIANA"] = "https://i.imgur.com/WAYaUV7.jpg"
DI["PEPITADEOURO"] = "https://i.imgur.com/5MmC1SO.jpg"
DI["TURQUESA"] = "https://i.imgur.com/mh4EZF7.jpg"

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
fogo = Cena(FOGO).vai()
pedras.direita = fogo
fogo.esquerda = pedras
templo.vai()
