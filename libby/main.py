# margaret.libby.main.py
#__author__ = "Ana Voig frade.giovana13@gmail.com"
from _spy.vitollino.main import Cena 
#from ruzwana.main import DI as RDI
#from stacy.main import fogo
IMAGENS = ["FOGO", "PEDRAS", "ARANHA"]
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
DIC["MÚMIA"] = "https://i.imgur.com/OVSH3Aa.jpg"
DIC["FOGO"] = "https://i.imgur.com/LmoJDRb.jpg"
DIC["DESMORONAMENTO"] = "https://i.imgur.com/Wl29PRv.jpg"

class Cartas: 
    def __init__(self):
        self.cartas = [Cena(RDI[uma_imagem]) for uma_imagem in IMAGENS]
    def baralho(self):
        return self.cartas
        
class Jogo:
    def __init__(self):
        self.baralho = Carta().baralho()
        self.templo = Cena(DIC["TEMPLO"])
        self.templo.direita = self.baralho[0]
    def inicia(self):
        self.templo.vai()
    
inca = Jogo() # Inca()
 
if __name__ == "__main__":
    inca.inicia()