# margaret.libby.main.py
#__author__ = "Ana Voig frade.giovana13@gmail.com"
from _spy.vitollino.main import Cena 
from random import shuffle 
#from ruzwana.main import DI as RDI
#from stacy.main import fogo
IMAGENS = ["TESOURO" , "ARANHA", "DESMORONAMENTO" , "MUMIA" , "FOGO"]*5
shuffle(IMAGENS)
PERIGOS = {}
DIC = DICIONARIO_DE_IMAGENS = {}
DIC["TEMPLO"] = "https://i.imgur.com/q4Cznxt.jpg"
DIC["DEGRAU"] = "https://i.imgur.com/UxV1LyG.jpg"
DIC["ARTEFATO1"] = "https://i.imgur.com/agqn9Gg.jpg"
DIC["ARTEFATO2"] = "https://i.imgur.com/r3Wkmtv.jpg"
DIC["ARTEFATO3"] = "https://i.imgur.com/QI7eW76.jpg"
DIC["ARTEFATO4"] = "https://i.imgur.com/WOU3fek.png"
DIC["ARTEFATO5"] = "https://i.imgur.com/xe9l1fP.jpg"
DIC["TESOURO"] = "https://i.imgur.com/mZ6E5Qs.jpg"
DIC["ARANHA"] = "https://i.imgur.com/tQLsXB0.jpg"
DIC["MUMIA"] = "https://i.imgur.com/OVSH3Aa.jpg"
DIC["FOGO"] = "https://i.imgur.com/LmoJDRb.jpg"
DIC["DESMORONAMENTO"] = "https://i.imgur.com/Wl29PRv.jpg"
ACAMPAMENTO = Cena("https://i.imgur.com/LYVTX9p.jpg")

class Perigo: 
    def __init__(self, tipo, imagem):
        self.cena = Cena(imagem)
        self.tipo = tipo
        self.cena_vai = self.cena.vai
        self.cena.vai = self.vai
        self.acampamento = ACAMPAMENTO
        
    def set_direita (self, direita):
        self.cena.direta = direita
        
    def set_direita (self, direita):
        self.cena.direta = direita
        
    def vai(self):
        if self.tipo in PERIGOS:
            self.cena.direita = self.acampamento 
        else:
             PERIGOS[self.tipo]*1
        self.cena_vai()   
        
class Cartas: 
    def __init__(self):
        self.cartas = [Perigo(DIC[uma_imagem], uma_imagem) 
            for uma_imagem in IMAGENS]
        for ordem, cartas in enumerate(self.cartas):
            if ordem < len(self.cartas)-1:
               cartas.set_direita = (self.cartas [ordem+1])
    def baralho(self):
        return self.cartas
        
class Jogo:
    def __init__(self):
        global PERIGOS
        PERIGOS = {}
        self.baralho = Cartas().baralho()
        self.templo = Cena(DIC["TEMPLO"])
        self.templo.direita = self.baralho[1]
    def inicia(self):
        self.templo.vai()
    
inca = Jogo() 
 
if __name__ == "__main__":
    inca.inicia()