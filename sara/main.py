# margaret.sara.main.py
__author__ = "Luiza Busnardo busnardo.luiza@gmail.com"

from _spy.vitollino.main import Cena, STYLE
STYLE["width"] = 600
STYLE["height"] = 600
from random import shuffle
IMAGENS = ["CENA", "ACAMPAMENTO", "MOCHILA", "ARTEFATO1", "MONSTRO", "PEDRAS", "FOGO", "DESABAMENTO", "COBRA", "ARANHA", "SALADOTESOURO", "OBSIDIANA", "TURQUESA", "PEPITADEOURO"]*5
shuffle(IMAGENS)
PERIGOS = {}

DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/ZzWag8V.jpg"
DI["ACAMPAMENTO"] = "https://i.imgur.com/3QWHNYM.jpg"
DI["MOCHILA"] = "https://i.imgur.com/UCQvviq.jpg"
DI["ARTEFATO1"] = "https://i.imgur.com/0t0j5Ne.jpg"
DI["MONSTRO"] = "https://i.imgur.com/zwbxMeu.jpg"
DI["PEDRAS"] = "https://i.imgur.com/fvnFDJl.jpg"
DI["FOGO"] = "https://i.imgur.com/sIq24MI.jpg"
DI["DESABAMENTO"] = "https://i.imgur.com/iEjnRsA.jpg"
DI["COBRA"] = "https://i.imgur.com/BRCXuz3.jpg"
DI["ARANHA"] = "https://i.imgur.com/VxTxDTj.jpg"
DI["SALADOTESOURO"] = "https://i.imgur.com/PQV7tEW.jpg"
DI["OBSIDIANA"] = "https://i.imgur.com/WAYaUV7.jpg"
DI["PEPITADEOURO"] = "https://i.imgur.com/5MmC1SO.jpg"
DI["TURQUESA"] = "https://i.imgur.com/mh4EZF7.jpg"

class Acampamento:
    def __init__(self):
        """ o que tem que ter no acampamento? """
        self.cena = Cena("https://i.imgur.com/ZzWag8V.jpg")
        
    def vai(self):
        self.cena.vai()
        
class Jogador:
    def __init__(self):
        """ o que tem que ter no jogador? """
        """ o jogador ganha uma turquesa para cada camara """ 
        pass
                
    def continua(self):
        """ entra em nova camara e acumula turquesa """
        pass
                
    def desiste(self):
        " segue para o acampamento """
        pass
            
class Perigo:
    def __init__(self, imagem, tipo):
        self.cena = Cena(imagem)
        self.tipo = tipo
        self.cena_vai = self.cena.vai
        self.cena.vai = self.vai
        self.acampamento = Acampamento()
        
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
        self.cartas = [Perigo(DI[uma_imagem], uma_imagem) for uma_imagem in IMAGENS]
        for ordem, cartas in enumerate(self.cartas):
            if ordem < len(self.cartas)-1:
                cartas.set_direita(self.cartas[ordem+1])
    def baralho(self):
        return self.cartas
    
class Jogo:
    def __init__(self):
        global PERIGOS
        PERIGOS ={}
        self.jogador = Jogador()
        self.baralho = Cartas().baralho()
        self.templo = Cena(DI["CENA"])
        #self.templo = Perigo(tipo="TEMPLO", imagem=DI["TEMPLO"])
        self.templo.direita = self.baralho[1]        
    def inicia(self):
        self.templo.vai()

inca = Jogo()

if __name__ == "__main__":
    inca.inicia()
    



