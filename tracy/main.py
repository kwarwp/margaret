# margaret.tracy.main.py
__author__ = "gabrielly de souza silveira dos reis bielly2reis@gmail.com "
from _spy.vitollino.main import Cena
from ruzwana.main import DI as RDI
from random import shuffle
#from stacy.main import fogo
#from natalia.main import sereiamonstro
IMAGENS = ["FOGO", "PEDRAS", "ARANHA", "MUMIA", "DESMORONAMENTO"]*5
shuffle(IMAGENS)
PERIGOS = {}

DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/7GZetDn.jpg"
DI["TESOURO"] = "https://i.imgur.com/h8MfuRD.jpg"
ACAMPAMENTO = Cena("https://i.imgur.com/dmSDeDF.jpg")      
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
            # deu ruim, já tinha aperecido um perigo
            self.cena.direita = self.acampamento
        else:
            PERIGOS[self.tipo] = 1
        self.cena_vai()
        
class Carta:
    def __init__(self):
        self.cartas = [Perigo(RDI[uma_imagem], uma_imagem) 
            for uma_imagem in IMAGENS]
        for ordem, carta in enumerate(self.cartas):
            if ordem < len(self.cartas)-1:
                carta.set_direita(self.cartas[ordem+1])
    def baralho(self):
        return self.cartas
        
class Jogo:
    def __init__(self):
        global PERIGOS
        PERIGOS ={}
        self.baralho = Carta().baralho()
        self.templo = Cena(DI["TEMPLO"])
        #self.templo = Perigo(tipo="TEMPLO", imagem=DI["TEMPLO"])
        self.templo.direita = self.baralho[1]
    def inicia(self):
        self.templo.vai()
        

inca = Jogo()  # Inca()

if __name__ == "__main__":
    inca.inicia()
    