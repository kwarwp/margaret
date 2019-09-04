# margaret.adda.main.py
from _spy.vitollino.main import Cena
TEMPLO = "https://i.imgur.com/LxT7pkN.jpg"
TESOURO = "https://i.imgur.com/SAGZEN0.jpg"
PERIGOS = {
    "MUMIA": "https://i.imgur.com/W2lH0Qh.png",
    "COBRA": "https://i.imgur.com/5XkbrsE.png",
    "DESLIZAMENTO": "",
    "FOGO": "",
    "ARANHA": ""
}

class Jogo:
	def inicia(self):
            templo = Cena(TEMPLO)
            tesouro = Cena(TESOURO)
            templo.direita = tesouro
            tesouro.esquerda = templo
            mumia = Cena(PERIGOS["MUMIA"])
            templo.vai()

jogo = Jogo()
jogo.inicia()