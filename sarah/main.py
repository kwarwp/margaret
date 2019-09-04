# margaret.sarah.main.py
from _spy.vitollino.main import Cena
#Quando Classe inicia em maiuscula, quando constante não é maiuscula
TEMPLO = "https://i.imgur.com/Tsxuzh2.jpg"
TESOURO = "https://i.imgur.com/tIsfRPD.jpg"

class Jogo:
    def inicia(self):
        templo = Cena(TEMPLO)
        #templo nome de uma instancia de um objeto
        #cena é uma instancia de uma classe
        tesouro = Cena(TESOURO)
        templo.direita = tesouro
        tesouro.esquerda = templo
        templo.vai()
        
