# margaret.stacy.main.py
__author__ = "Victória Regina Caruzo victorialourencocaruzo@gmail.com"

from _spy.vitollino.main import Cena, STYLE
STYLE["width"] = 600
STYLE["height"] = 600
from random import shuffle
IMAGENS = ["TESOURO", "FOGO", "ARTEFATO1", "COBRA", "DESABAMENTO", "MUMIA", "ARANHA"]*5
shuffle(IMAGENS)
PERIGOS = {}
DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/LXptu0U.jpg"
DI["TESOURO"] = "https://i.imgur.com/Nq1hCeU.jpg"
DI["FOGO"] = "https://i.imgur.com/KRK66bR.jpg"
DI["ARTEFATO1"] = "https://i.imgur.com/1QHNdyI.jpg"
DI["COBRA"] = "https://i.imgur.com/MydpgBT.jpg"
DI["DESABAMENTO"] = "https://i.imgur.com/jnxWklS.jpg"
DI["MUMIA"] = "https://i.imgur.com/HPp1k5T.jpg" 
DI["ARANHA"] = "https://i.imgur.com/w90m1jf.jpg"
DI["SALADOTESOURO"] = "https://i.imgur.com/83xewyg.jpg"
DI["PEPITADEOURO"] = "https://i.imgur.com/tsP6aby.jpg"
DI["OBSIDIANA"] = "https://i.imgur.com/1Pqs1JN.jpg"
DI["TURQUESA"] = "https://i.imgur.com/yIhLHaK.jpg"
DI["ACAMPAMENTO"] = "https://i.imgur.com/yIhLHaK.jpg"

class Inca:
    def inicia(self):
        templo = Cena(DI["TEMPLO"])
        tesouro = Cena(DI["TESOURO"])
        fogo = Cena(DI["FOGO"])
        artefato1 = Cena(DI["ARTEFATO1"])
        cobra = Cena(DI["COBRA"])
        desabamento = Cena(DI["DESABAMENTO"])
        mumia = Cena(DI["MUMIA"])
        aranha = Cena(DI["ARANHA"])
        sala_do_tesouro = Cena(DI["SALADOTESOURO"])
        pepita_de_ouro = Cena(DI["PEPITADEOURO"])
        obsidiana = Cena(DI["OBSIDIANA"])
        turquesa = Cena(DI["TURQUESA"])
        acampamento = Cena(DI["ACAMPAMENTO"])
        templo.direita = tesouro
        tesouro.esquerda = templo
        tesouro.direita = fogo
        fogo.esquerda = tesouro
        fogo.direita = artefato1
        artefato1.esquerda = fogo
        artefato1.direita = cobra
        cobra.esquerda = artefato1
        cobra.direita = desabamento
        desabamento.esquerda = cobra
        desabamento.direita = mumia
        mumia.esquerda = desabamento
        mumia.direita = aranha
        aranha.esquerda = mumia
        templo.vai()
        
#inca = Inca()

#if __name__ == "__main__":
    #jogo.inicia()
    
class Perigo:
    def _init__(self, imagem, tipo):
        self.cena = Cena(imagem)
        self.tipo = tipo
        self.cena_vai = self.cena.vai
        self.cena.vai = self.vai
        
    def vai(self):
        if self.tipo in PERIGO:
            # deu ruim, já tinha aparecido um perigo
        else:
            PERIGOS[self.tipo] = 1
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