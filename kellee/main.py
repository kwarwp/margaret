# margaret.kellee.main.py
__author__ = "Bárbara Juliana C.Soares barbara_ju07@hotmail.com"
from _spy.vitollino.main import Cena
from random import shuffle
IMAGENS = ["CENA", "TESOURO", "MONSTRO", "FOGO", "PEDRAS", "MUMIA"]*8
shuffle(IMAGENS)
PERIGOS = {}

DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/F0pWLRM.png"
DI["TESOURO"] = "https://i.imgur.com/Z2CD83L.jpg"
DI["MONSTRO"] = "https://i.imgur.com/4cBiZ6n.jpg"
DI["FOGO"] = "https://i.imgur.com/qLYrtR0.jpg"
DI["PEDRAS"] = "https://i.imgur.com/qPfDat7.jpg"
DI["MUMIA"] = "https://i.imgur.com/4xWmf5O.jpg"
ACAMPAMENTO = Cena(" https://i.imgur.com/59m6gMz.jpg")
class Perigo:
    def __init__(self, imagem, tipo):
       self.cena = Cena(imagem)
       self.tipo = tipo
       self.cena_vai = self.cena.vai
       self.cena.vai = self.vai
       self.acampamento = ACAMPAMENTO
     
    def set_direita(self, direita):
        self.cena.direita = direita
        
    def set_esquerda(self, esquerda)
        self.cena.esquerda = esquerda
    def vai(self):
        if self.tipo in PERIGOS:
           # deu ruim, já tinha aparecido um perigp
           self.cena.direita = self.acampamento
        else:
            PERIGOS[self.tipo] = 1
        self.cena_vai()
        
        
class Carta:
    def __init__(self):
        self.cartas = [Perigo(DI[uma_imagem], uma_imagem) 
        for uma_imagem in IMAGENS] 
        for ordem, carta in enumerate(self.cartas):
            if ordem < len(self.cartas)-1:
                carta.direita = self.cartas[ordem+1]
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