# margaret.heather.main.py
from _spy.vitollino.main import Cena
from random import shuffle
TEMPLO = "https://i.imgur.com/7GZetDn.jpg"
TESOURO = "https://i.imgur.com/h8MfuRD.jpg"
PERIGOS = {
    "MUMIA": "https://i.imgur.com/YfLqYCa.jpg",
    "COBRA":"https://i.imgur.com/Adp8zfm.jpg",
    "FOGO" : "https://i.imgur.com/9341Lk9.jpg",
    "DESMORONAMENTO" : "https://i.imgur.com/Qm6d1sd.jpg"
}
class Cartas:
    def __init__(self):
        self.baralho = [Cena(perigo) 
            for perigo in PERIGOS.values()] * 5
        shuffle(self.baralho)
        baralho_amanha = self.baralho[1:]
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
        templo.direta = tesouro
        tesouro.esquerda = templo
        perigos = Cartas()
        umperigo = perigos.primeira_carta()
        tesouro.direita = umperigo
        umperigo.esquerda = tesouro
        templo.vai()
        
            
jogo = Jogo()
jogo.inicia()