# margaret.ruzwana.main.py
__author__ = "G.L.L Almeida gabriellaleni@gmail.com"
from _spy.vitollino.main import Cena, STYLE
STYLE["width"] = 600

DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/BTTqaBa.jpg"
DI["MUMIA"] = "https://i.imgur.com/T6ONIKS.jpg"
DI["PEDRAS"] = "https://i.imgur.com/fbNGz9L.jpg"
DI["DESMORONAMENTO"] = "https://i.imgur.com/WNgmQjQ.jpg"
DI["ARTEFATO"] = "https://i.imgur.com/vN9MDwx.jpg"
DI["FOGO"] = "https://i.imgur.com/Mbek5ie.jpg"
DI["ARANHA"] = "https://i.imgur.com/k2RoQqf.jpg"
DI["COBRA"] = "https://i.imgur.com/k2RoQqf.jpg"

class Inca:
    def inicia(self):
        templo = Cena(DI["TEMPLO"])
        pedras = Cena(DI["PEDRAS"])
        mumia = Cena(DI["MUMIA"])
        desmoronamento = Cena(DI["DESMORONAMENTO"])
        artefato = Cena(DI["ARTEFATO"])
        fogo = Cena(DI["FOGO"])
        aranha = Cena(DI["ARANHA"])
        cobra = Cena(DI["COBRA"])        
        templo.direita = pedras
        pedras.esquerda = templo
        pedras.direita = desmoronamento
        desmoronamento.esquerda = pedras
        desmoronamento.direita = pedras
        pedras.esquerda = desmoronamento
        pedras.direita = fogo
        fogo.esquerda = pedras
        templo.vai()
    
class Carta:
    pass
    def baralho(self):
        return []

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