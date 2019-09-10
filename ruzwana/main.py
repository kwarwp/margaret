# margaret.ruzwana.main.py
__author__ = "G.L.L Almeida gabriellaleni@gmail.com"
from _spy.vitollino.main import Cena, STYLE
STYLE["width"] = 600
STYLE["height"] = 600

from random import shuffle
IMAGENS = ["FOGO", "PEDRAS", "ARANHA", "MUMIA", "DESMORONAMENTO","ARTEFATO"]*5
shuffle(IMAGENS)
DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/BTTqaBa.jpg"
DI["MUMIA"] = "https://i.imgur.com/T6ONIKS.jpg"
DI["PEDRAS"] = "https://i.imgur.com/fbNGz9L.jpg"
DI["DESMORONAMENTO"] = "https://i.imgur.com/WNgmQjQ.jpg"
DI["ARTEFATO"] = "https://i.imgur.com/vN9MDwx.jpg"
DI["FOGO"] = "https://i.imgur.com/Mbek5ie.jpg"
DI["ARANHA"] = "https://i.imgur.com/k2RoQqf.jpg"
DI["COBRA"] = "https://i.imgur.com/k2RoQqf.jpg"
        
class Perigo:
    def _init__(self, imagem, tipo):
        self.cena = Cena(imagem)
        self.tipo = tipo
        self.cena_vai = self.cena.vai
        self.cena.vai = self.vai
        
    def vai(self):
        self.cena_vai()

class Cartas:
    def __init__(self):
        self.cartas = [Cena(DI[uma_imagem]) for uma_imagem in IMAGENS]
        for ordem, carta in enumerate(self.cartas):
            if ordem < len(self.cartas)-1:
                carta.direita = self.cartas[ordem+1]
    def baralho(self):
        return self.cartas
    
class Jogo:
    def __init__(self):
        self.baralho = Cartas().baralho()
        self.templo = Cena(DI["TEMPLO"])
        self.templo.direita = self.baralho[1]        
    def inicia(self):
        self.templo.vai()
        
inca = Jogo()

if __name__ == "__main__":
    inca.inicia()