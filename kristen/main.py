# margaret.kristen.main.py
from _spy.vitollino.main import Cena
TEMPLO = "https://i.imgur.com/hy9jUf5.jpg"
TESOURO = "https://i.imgur.com/pcrB1gm.jpg"
PERIGOS = {
    "MUMIA": "https://i.imgur.com/vaRhKqK.jpg",
    "COBRA": "https://i.imgur.com/oTs2Tf4.jpg",
    "DESMORONAMENTO": "https://i.imgur.com/gNFtoMy.jpg",
    "ARANHA": "https://i.imgur.com/gNFtoMy.jpg",
    "FOGO": "https://i.imgur.com/4XA6XhB.jpg",
} 

class Cartas:
    def __init__(self):
        self.baralho = [Cena(perigo) for perigo in PERIGOS.values()] * 5 
        baralho_amanha = self.baralho[1:]
        baralho_zip = zip(self.baralho, baralho_amanha)
        for carta_hoje, carta_amanha in baralho_zip:
            carta_hoje.direita = carta_amanha
            carta_amanha.esquerda = carta_hoje

    def primeira_carta(self):
        return self.baralho[0]


class Jogo: 
    def inicia(self):
        templo = Cena (TEMPLO)
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