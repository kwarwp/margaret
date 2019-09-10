# margaret.kellee.main.py
__author__ = "Bárbara Juliana C.Soares barbara_ju07@hotmail.com"
from _spy.vitollino.main import Cena
from random import shuffle
IMAGENS = ["CENA", "TESOURO", "MONSTRO", "FOGO", "PEDRAS", "MUMIA"]*8
shuffle(IMAGENS)
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/F0pWLRM.png"
DI["TESOURO"] = "https://i.imgur.com/Z2CD83L.jpg"
DI["MONSTRO"] = "https://i.imgur.com/4cBiZ6n.jpg"
DI["FOGO"] = "https://i.imgur.com/qLYrtR0.jpg"
DI["PEDRAS"] = "https://i.imgur.com/qPfDat7.jpg"
DI["MUMIA"] = "https://i.imgur.com/4xWmf5O.jpg"
DI["PEPITA DE OURO"] = "https://i.imgur.com/wtTTD26.png"
DI["PEPITA OBSIDIANA"] = "https://i.imgur.com/DAtKJFX.png"
DI["PEPITA TURQUESA"] = "= https://i.imgur.com/fnpiuCo.jpg" 
 
class Perigo:
    def __init__(self, imagem, tipo):
       self.cena = Cena(imagem)
       self.tipo = tipo
       self.cena_vai = self.cena.vai
       self.cena.vai = self.vai
     
    def vai(self):
        self.cena_vai()
        
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
        self.templo = Cena(DI["CENA"])
        self.templo.direita = self.baralho[1]
    def inicia(self):
        self.templo.vai()
        
        
inca = Jogo()  # Inca()

if __name__ == "__main__":
    inca.inicia()