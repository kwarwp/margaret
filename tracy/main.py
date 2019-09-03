# margaret.tracy.main.py
from _spy.vitollino.main import Cena 
imagens = ["CENA", "TESOURO"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/IdXGTYa.jpg"
DI["TESOURO"] = "https://i.imgur.com/78iHROq.jpg"
DI["COBRA"] = "https://i.imgur.com/7G66ctJ.png"
DI["FOGO"] = "https://i.imgur.com/76RAEGh.jpg"

class Inca:
    def inicia(self):
        cena = Cena(DI["CENA"])
        tesouro = Cena(DI["TESOURO"])
        cobra = Cena(DI["COBRA"])
        fogo = Cena(DI["fogo"])
        templo.direita = tesouro
        templo.vai()
        tesouro.esquerda = templo
        tesouro.direita = cobra
        cobra.esquerda = tesouro
        cobra.direita = fogo
        fogo.esquerda = cobra 

inca = Inca()
inca.inicia()