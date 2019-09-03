# margaret.kellee.main.py
__author__ = "Bárbara Juliana C.Soares barbara_ju07@hotmail.com"
from _spy.vitollino.main import Cena
IMAGENS = ["CENA", "TESOURO", "MONSTRO", "FOGO", "PEDRAS"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/F0pWLRM.png"
DI["TESOURO"] = "https://i.imgur.com/Z2CD83L.jpg"
DI["MONSTRO"] = "https://i.imgur.com/4cBiZ6n.jpg"
DI["FOGO"] = "https://i.imgur.com/qLYrtR0.jpg"
DI["PEDRAS"] = "https://i.imgur.com/rpIsgaD"
    
class Carta:
    def __init__(self):
        self.cartas = [Cena(DI[uma_imagem]) for uma_imagem in IMAGENS] 
    def baralho(self):
        return self.cartas
        

class Jogo:
    def __init__(self):
        self.baralho = Carta().baralho()
        self.templo = Cena(DI["CENA"])
        self.templo.direita = self.baralho[1]
    def inicia(self):
        self.templo.vai()
        
        
inca = Jogo()  # Inca()

if __name__ == "__main__":
    inca.inicia()