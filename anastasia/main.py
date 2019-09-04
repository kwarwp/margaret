# margaret.anastasia.main.py
from _spy.vitollino.main import Cena
TEMPLO = "https://i.imgur.com/Z3XxeMC.jpg"
TESOURO = "https://i.imgur.com/eH41cff.jpg"
PERIGOS = {
    "MUMIA": "https://i.imgur.com/YfLqYCa.jpg",
    "COBRA":"https://i.imgur.com/xqLNF3c.jpg",
    "FOGO" : "https://i.imgur.com/9341Lk9.jpg",
    "DESMORONAMENTO" : "https://i.imgur.com/Qm6d1sd.jpg"
}

class Jogo:
    def inicia(self):
        templo = Cena(TEMPLO)
        tesouro = Cena (TESOURO)
        templo.direita = tesouro
        tesouro.esquerda = templo
        mumia = Cena(PERIGOS["MUMIA"])
        tesouro.direita = mumia
        mumia.esquerda = tesouro
        templo.vai()

jogo = Jogo()
jogo.inicia()
