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
class Jogo: 
    def inicia(self):
        templo = Cena (TEMPLO)
        tesouro = Cena (TESOURO)
        templo.direita = tesouro
        tesouro.esquerda = templo 
        mumia = Cena (PERIGOS["MUMIA"])
        tesouro.direita = mumia
        mumia.esquerda = tesouro 
        templo.vai()
        
jogo = Jogo()
jogo.inicia()