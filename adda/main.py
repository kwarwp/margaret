# margaret.adda.main.py
from _spy.vitollino.main import Cena
from random import shuffle

TEMPLO = "https://i.imgur.com/LxT7pkN.jpg"
TESOURO = "https://i.imgur.com/SAGZEN0.jpg"
PERIGOS = {
    "MUMIA": "https://i.imgur.com/W2lH0Qh.png",
    "COBRA": "https://i.imgur.com/5XkbrsE.png",
    "DESLIZAMENTO": "https://i.imgur.com/AcZQZBp.jpg",
    "FOGO": "https://i.imgur.com/Djo0gGm.png",
    "ARANHA": "https://i.imgur.com/giPXuH7.png"
}

class Cartas:
    def __init__(self):
        self.baralho = [Cena(perigo) for perigo in PERIGOS.values()] * 5
        baralho_amanha = self.baralho[1:]
        shuffle(self.baralho)
        baralho_zip = zip(self.baralho, baralho_amanha)
        for c_hoje, c_ama in baralho_zip:
            c_hoje.direita = c_ama
            c_ama.esquerda = c_hoje
            
    def primeira_carta(self):
        return self.baralho[0]

class Jogo:
    def inicia(self):
            templo = Cena(TEMPLO)
            tesouro = Cena(TESOURO)
            templo.direita = tesouro
            tesouro.esquerda = templo
            perigos = Cartas()
            umperigo = perigos.primeira_carta()
            tesouro.direita = umperigo
            umperigo.esquerda = tesouro            
            templo.vai()
            

jogo = Jogo()
jogo.inicia()