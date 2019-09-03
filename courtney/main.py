# margaret.courtney.main.py
__author__ = "Adailton dos S. Junior junior_shoot4@hotmail.com"
from _spy.vitollino.main import Cena 
imagens = ["CENA", "TESOURO"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/IdXGTYa.jpg"
DI["TESOURO"] = "https://i.imgur.com/78iHROq.jpg"
DI["COBRA"] = "https://i.imgur.com/7G66ctJ.png"
DI["FOGO"] = "https://i.imgur.com/76RAEGh.jpg"

class Inca:
    def inicia(self):
        templo = Cena(DI["CENA"])
        tesouro = Cena(DI["TESOURO"])
        cobra = Cena(DI["COBRA"])
        fogo = Cena(DI["FOGO"])
        templo.direita = tesouro
        templo.vai()
        tesouro.esquerda = templo
        tesouro.direita = cobra
        cobra.esquerda = tesouro
        cobra.direita = fogo
        fogo.esquerda = cobra 

inca = Inca()

if __name__ == "__main__":
    inca.inicia()