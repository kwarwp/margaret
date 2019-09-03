# margaret.libby.main.py
#__author__ = "Ana Voig frade.giovana13@gmail.com"
from _spy.vitollino.main import Cena 
#from stacy.main import fogo
#IMAGENS = ["CENA", "TESOURO"]
DIC = DICIONARIO_DE_IMAGENS = {}
DIC["TEMPLO"] = "https://i.imgur.com/q4Cznxt.jpg"
DIC["TESOURO"] = "https://i.imgur.com/x2wLF9U.jpg"
DIC["DEGRAU"] = "https://i.imgur.com/UxV1LyG.jpg"
DIC["ARTEFATO1"] = "https://i.imgur.com/agqn9Gg.jpg"

#class Inca:
    #def inicia(self):
        #templo = Cena(DIC["TEMPLO"])
        #tesouro = Cena(DIC["TESOURO"])
        #degrau = Cena(DIC["DEGRAU"])
        #artefato01 = Cena(DIC["ARTEFATO01"])
        #templo.direita = degrau
        #degrau.direita = artefato01
        #tesouro.esquerda = templo
        #tesouro.direita = fogo
        #fogo.esquerda = tesouro
        #tesouro.esquerda = templo
        #templo.vai()
        
#outro jeito mais sofisticado:
        
class Carta: 
    pass
    def baralho(self):
        return []
        
class Jogo:
    def __init__(self):
        self.baralho = Carta().baralho()
        self.templo = Cena(DIC["TEMPLO"])
    def inicia(self):
        pass
    
inca = Jogo() # Inca()
 
if __name__ == "__main__":
    inca.inicia()