# margaret.heather.main.py
from _spy.vitollino.main import Cena
TEMPLO = "https://i.imgur.com/7GZetDn.jpg"
TESOURO = "https://i.imgur.com/h8MfuRD.jpg"
PERIGOS = {
    "MUMIA": "",
    "COBRA": ""
}

class Jogo:
    def inicia(self):
        templo = Cena(TEMPLO)
        tesouro = Cena(TESOURO)
        templo.direta = tesouro
        tesouro.esquerda = templo
        mumia = Cena(PERIGOS["MUMIA"])
        tesouro.direita = mumia
        mumia.esquerda = tesouro
        templo.vai()
        
jogo = Jogo()
jogo.inicia()