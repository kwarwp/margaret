# margaret.templo.main.py
from _spy.vitollino.main import Cena
TEMPLO = "https://i.imgur.com/IKMbeR2.jpg"
TURQUESA = "https://i.imgur.com/tS8YRxw.jpg"
ARANHA = "https://i.imgur.com/0BUoL0u.jpg"

class Carta:
    def __init__(self):
        self.carta = Cena(ARANHA)
        
    def vai(self):
        self.carta.vai()
        
    def anterior(self, anterior):
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