# margaret.julia.main.py
from _spy.vitollino.main import Cena
TEMPLO = "https://i.imgur.com/eiRyeJf.jpg"

""" PEDRAS """
TURQUESA = "https://i.imgur.com/jcJOmVD.png"

""" ARTEFATOS """
ARTa = "https://i.imgur.com/qyzLwer.png"

""" CAOS """
ARANHA = "https://i.imgur.com/lt6nVqj.gif"
DESMORONAMENTO = "https://i.imgur.com/SzTXOyb.png"
COBRA = "https://i.imgur.com/ZGHOKIz.png"
LAVA = "https://i.imgur.com/TadcMw6.jpg"
MUMIA = "https://i.imgur.com/krrhvL6.jpg"


""" Listas """
caos = [ARANHA, DESMORONAMENTO, COBRA, LAVA, MUMIA]*5
pedras = [TURQUESA]
artefatos = [ARTa]

class Carta:
    def __init__(self, cena=ARANHA):
        self.carta = Cena(cena)
        
    def vai(self):
        self.carta.vai()
        
    def anterior(self, anterior):
        anterior.direita = self.carta
        self.carta.esquerda = anterior
        
    def montar_baralho(self, anterior):
        for imagem_carta in caos:
            carta = Carta(imagem_carta)
            carta.anterior(anterior.carta)
            anterior = carta
    

class Jogo:
    def __init__(self):
        self.templo = Cena(TEMPLO)
        self.carta = Carta()
        self.carta.anterior(self.templo)
        self.carta.monta_baralho(self.carta)
        self.templo.vai()
        
        
if __name__ == "__main__":
    Jogo()