# margaret.angie.main.py
from _spy.vitollino.main import Cena
IMAGENS = ["CENA", "TESOURO", "COBRA", "FOGO"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/6NNu6ps.jpg"
DI["TESOURO"] = "https://i.imgur.com/nBbQxbD.jpg"
DI["COBRA"] = "https://i.imgur.com/Lh1O87Q.jpg"
DI["FOGO"] = "https://i.imgur.com/ScR01C1"
DI["MONSTRO"] = "https://i.imgur.com/nvWMlWx.jpg"

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