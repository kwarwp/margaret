# margaret.amanda.main.py
#Código criado por Acacia Calegari
from _spy.vitollino.main import Cena
TEMPLO = "https://i.imgur.com/S6Ruv7c.jpg"
TURQUESA = "https://i.imgur.com/jR1l6vN.png"
ARANHA = "https://i.imgur.com/1Bz5EVM.png"
ARTEFATO = "https://i.imgur.com/IgwQY1N.png"
DESMORONAMENTO = "https://i.imgur.com/GYLGPyn.jpg"
COBRA = "https://i.imgur.com/1S1LFUE.jpg"

DESASTRES = [ARTEFATO, DESMORONAMENTO, COBRA, ARANHA]*5

class Carta:
    def __init__(self, imagem=ARANHA):
        self.carta = Cena(imagem)
           
    def vai(self):
        self.carta.vai()

    def monta_baralho(self, anterior):
        for imagem_carta in caos:
        carta = Carta(imagem_carta)
        carta.anterior(anterior.carta)
        anterior = carta
        
    def anterior(self, anterior)
        anterior.direita = self.carta
        self.carta.esquerda = anterior
        
class Jogo:
    def __init__(self):
        self.templo = Cena(TEMPLO)
        self.carta = Carta()
        self.carta.anterior(self.templo)
        self.templo.vai()
        
if __name__ == "__main__":
	Jogo()