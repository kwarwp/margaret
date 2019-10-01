# margaret.courtney.main.py
__author__ = "Adailton dos S. Junior junior_shoot4@hotmail.com"
from _spy.vitollino.main import Cena, STYLE
STYLE["width"] = 600
STYLE["height"] = 600
from random import shuffle
IMAGENS = ["FOGO", "COBRA", "DESABAMENTO", "MUMIA", "ARANHA"]*5
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

class Acampamento:
    def __init__(self):
        """ o que tem que ter no acampamento? """
        self.cena = Cena("https://i.imgur.com/wgcVh9M.jpg")
        pass
                
    def vai(self):
        self.cena.vai()
        
class Jogador:
    def __init__(self):
        """ o que tem que ter no jogador? """
        """ o jogador ganha uma turquesa para cada camara """ 
        pass
class Inca:
def continua(self):
        """ entra em nova camara e acumula turquesa """
        pass
                
    def desiste(self):
        " segue para o acampamento """
        pass Image

            
class Perigo:
    def __init__(self, imagem, tipo):
        self.cena = Cena(imagem)
        self.tipo = tipo
        self.cena_vai = self.cena.vai
        self.cena.vai = self.vai
        self.acampamento = Acampamento()
    def inicia(self):
        templo = Cena(DI["CENA"])
        tesouro = Cena(DI["TESOURO"])
        cobra = Cena(DI["COBRA"])
        fogo = Cena(DI["FOGO"])
        templo.direita = tesouro
        templo.vai()
        tesouro.esquerda = templo
        tesouro.direita = cobra
        cobra.esquerda = tesouro
        cobra.direita = fogo
        fogo.esquerda = cobra 

inca = Inca()

if __name__ == "__main__":
    inca.inicia()