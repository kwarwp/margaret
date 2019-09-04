# margaret.grace.main.py
from _spy.vitollino.main import Cena
TEMPLO = "https://i.imgur.com/g3Vskr9.png"
TESOURO = "https://i.imgur.com/MnqQYCC.png"

class Jogo:
    def inicia(self):
        templo = Cena(TEMPLO)
        tesouro = Cena(TESOURO)
        templo.direita = tesouro
        tesouro.esquerda = templo
        templo.vai()
        
jogo = Jogo()
jogo.inicia()