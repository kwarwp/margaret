# margaret.anastasia.main.py
from _spy.vitollino.main import Cena
from random import shuffle
TEMPLO = "https://i.imgur.com/Z3XxeMC.jpg"
TESOURO = "https://i.imgur.com/eH41cff.jpg"
PERIGOS = {
    "MUMIA": "https://i.imgur.com/YfLqYCa.jpg",
    "COBRA":"https://i.imgur.com/Adp8zfm.jpg",
    "FOGO" : "https://i.imgur.com/9341Lk9.jpg",
    "DESMORONAMENTO" : "https://i.imgur.com/Qm6d1sd.jpg"
}
#ARTEFATOS = {
 #   "ARTEFATO1": "",
 #  "ARTEFATO2": "",
 #  "ARTEFATO3": "",
 #  "ARTEFATO4": "",
#}

class Cartas:
    def __init__(self):
        self.baralho = [Cena(perigo) for perigo in PERIGOS.values()] * 5
        shuffle(self.baralho)
        baralho_amanha = self.baralho[1:]
        baralho_zip = zip(self.baralho, baralho_amanha)
        for carta_hoje, carta_amanha in baralho_zip:
            carta_hoje.direita = carta_amanha
            carta_amanha.esquerda = carta_hoje
        
    def primeira_carta(self):
        return self.baralho[0]
        
class Jogo:
    def inicia(self):
        templo = Cena(TEMPLO)
        tesouro = Cena (TESOURO)
        templo.direita = tesouro
        tesouro.esquerda = templo
        perigos = Cartas()
        umperigo = perigos.primeira_carta()
        tesouro.direita = umperigo
        umperigo.esquerda = tesouro
        templo.vai()
        

jogo = Jogo()
jogo.inicia()
