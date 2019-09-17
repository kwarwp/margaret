# margaret.ruzwana.main.py
__author__ = "G.L.L Almeida gabriellaleni@gmail.com"
from _spy.vitollino.main import Cena, STYLE
STYLE["width"] = 600
STYLE["height"] = 600

from random import shuffle
IMAGENS = ["FOGO", "PEDRAS", "ARANHA", "MUMIA", "DESMORONAMENTO","ARTEFATO"]*5
shuffle(IMAGENS)
PERIGOS = {}

DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/BTTqaBa.jpg"
DI["MUMIA"] = "https://i.imgur.com/T6ONIKS.jpg"
DI["PEDRAS"] = "https://i.imgur.com/fbNGz9L.jpg"
DI["DESMORONAMENTO"] = "https://i.imgur.com/WNgmQjQ.jpg"
DI["ARTEFATO"] = "https://i.imgur.com/vN9MDwx.jpg"
DI["FOGO"] = "https://i.imgur.com/Mbek5ie.jpg"
DI["ARANHA"] = "https://i.imgur.com/k2RoQqf.jpg"
DI["COBRA"] = "https://i.imgur.com/k2RoQqf.jpg"
ACAMPAMENTO = Cena("https://i.imgur.com/Cbt8tRd.jpg")
        
class Perigo:
    def __init__(self, imagem, tipo):
        self.cena = Cena(imagem)
        self.tipo = tipo
        self.cena_vai = self.cena.vai
        self.cena.vai = self.vai
        self.acampamento = ACAMPAMENTO
        
    def set_direita(self, direita):
        self.cena.direita = direita
        
    def set_esquerda(self, esquerda):
        self.cena.esquerda = esquerda
        
    def vai(self):
        if self.tipo in PERIGOS:
            # deu ruim, já tinha aparecido um perigo
            self.cena.direita = self.acampamento
        else:
            PERIGOS[self.tipo] = 1
        self.cena_vai()

class Cartas:
    def __init__(self):
        self.cartas = [Perigo(DI[uma_imagem], uma_imagem)
            for uma_imagem in IMAGENS]
        for ordem, cartas in enumerate(self.cartas):
            if ordem < len(self.cartas)-1:
                cartas.set_direita = (self.cartas[ordem+1])
    def baralho(self):
        return self.cartas

class Jogo:
    def __init__(self):
        global PERIGOS
        PERIGOS = {}
        self.baralho = Cartas().baralho()
        self.templo = Cena(DI["TEMPLO"])
        self.templo.direita = self.baralho[1]        
    def inicia(self):
        self.templo.vai()
        
inca = Jogo()

if __name__ == "__main__":
    inca.inicia()