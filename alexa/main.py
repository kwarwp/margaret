# margaret.alexa.main.py
from _spy.vitollino.main import Cena
TEMPLO = "https://i.imgur.com/SN72LsK.jpg"
TURQUESA = "https://i.imgur.com/nTK6oYD.png"
ARANHA = "https://i.imgur.com/5nKC0ns.png"
ARTEFATO = "https://i.imgur.com/IITJkP0.png"
DESMORONAMENTO = "https://i.imgur.com/HRBlc8Q.jpg"
COBRA = "https://i.imgur.com/NEPd9FH.jpg"
FOGO = "https://i.imgur.com/qK0szTH.jpg"

DESASTRES = [ARTEFATO, DESMORONAMENTO, COBRA, ARANHA, FOGO]*5

class Carta:    
    def __init__(self, cena=ARANHA):
        self.carta = Cena(cena)
        anterior = self
        for carta in DESASTRE: 
        umacarta = Carta(carta)
        umacarta.anterior(anterior.carta)
        anterior = umacarta
    
    def vai(self):
        self.carta.vai()
    
    def anterior(self,anterior):
        anterior.direita  =self.carta
        self.carta.esquerda = anterior   
        
class Jogo: 
    def __init__(self):
        self.templo = Cena(TEMPLO)
        self.carta = Carta()
        self.carta.anterior(self.templo)
        self.templo.vai()
        
if __name__=="__main__":
    Jogo()
    
    
    
    
    
    
    