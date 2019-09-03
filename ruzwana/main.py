# margaret.ruzwana.main.py
__author__ = "G.L.L Almeida gabriellaleni@gmail.com"
from _spy.vitollino.main import Cena, STYLE
STYLE["width"] = 600

IMAGENS = ["FOGO", "PEDRAS", "ARANHA", "MUMIA", "DESMORONAMENTO"]*5
DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/BTTqaBa.jpg"
DI["MUMIA"] = "https://i.imgur.com/T6ONIKS.jpg"
DI["PEDRAS"] = "https://i.imgur.com/fbNGz9L.jpg"
DI["DESMORONAMENTO"] = "https://i.imgur.com/WNgmQjQ.jpg"
DI["ARTEFATO"] = "https://i.imgur.com/vN9MDwx.jpg"
DI["FOGO"] = "https://i.imgur.com/Mbek5ie.jpg"
DI["ARANHA"] = "https://i.imgur.com/k2RoQqf.jpg"
DI["COBRA"] = "https://i.imgur.com/k2RoQqf.jpg"
    
class Carta:
    def __init__(self):
        self.cartas = [Cena(DI[uma_imagem]) for uma_imagem in IMAGENS]
        for ordem, carta in enumerate(self.cartas):
            if ordem < len(self.cartas)-1:
                carta.direita = self.cartas[ordem+1]
        
    def baralho(self):
        return self.cartas

class Jogo:
    def __init__(self):
        self.baralho = Carta().baralho()
        self.templo = Cena(DI["TEMPLO"])
        self.templo.direita  = self.baralho[0]
    def inicia(self):
        self.templo.vai()

inca = Jogo()

if __name__ == "__main__":
    inca.inicia()