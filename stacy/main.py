# margaret.stacy.main.py
__author__ = "Victória Regina Caruzo victorialourencocaruzo@gmail.com"
from _spy.vitollino.main import Cena
IMAGENS = ["TEMPLO", "TESOURO", "FOGO", "ARTEFATO1", "COBRA", "DESABAMENTO", "MUMIA", "ARANHA"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/LXptu0U.jpg"
DI["TESOURO"] = "https://i.imgur.com/Nq1hCeU.jpg"
DI["FOGO"] = "https://i.imgur.com/KRK66bR.jpg"
DI["ARTEFATO1"] = "https://i.imgur.com/1QHNdyI.jpg"
DI["COBRA"] = "https://i.imgur.com/MydpgBT.jpg"
DI["DESABAMENTO"] = "https://i.imgur.com/jnxWklS.jpg"
DI["MUMIA"] = "https://i.imgur.com/HPp1k5T.jpg" 
DI["ARANHA"] = "https://i.imgur.com/w90m1jf.jpg"

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
        
inca = Inca()

if __name__ == "__main__":
    inca.inicia()
    
class Cartas:
    def baralho(self):
        return []
    pass
    
class Jogo:
    def __init__(self):
    self.baralho = Cartas().baralho()
    pass 
    

