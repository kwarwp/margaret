# margaret.naomi.main.py
__author__ = "Raquel P. R. Santos raquelp737@gmail.com"
from _spy.vitollino.main import Cena , STYLE
from random import shuffle
STYLE["Width"]=600
STYLE["Width"]=600
IMAGENS = ["CENA", "ARTEFATO" , "FOGO" , "DESMORONAMENTO" , "COBRA" , "PEDRINHAS" , "ARANHAS" , "MUMIA"]*5
shuffle(IMAGENS)
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/inzdUaq.jpg"
DI["ARTEFATO"] = "https://i.imgur.com/DJNXWXY.jpg"
DI["FOGO"] = " https://i.imgur.com/yufZlvN.jpg"
DI["DESMORONAMENTO"] = "https://i.imgur.com/uMSX7Ka.jpg"
DI["COBRA"] = "https://i.imgur.com/UcWZh28.jpg"
DI["PEDRINHAS"] = " https://i.imgur.com/ijt1Hbq.jpg"
DI["ARANHAS"] = " "
DI["MUMIA"] = " "
class Inca:
    def inicia(self):
        templo = Cena(DI["CENA"])
        artefato = Cena(DI["ARTEFATO"])
        fogo = Cena(DI["FOGO"])
        desmoronamento = Cena(DI["DESMORONAMENTO"])
        cobra = Cena(DI["COBRA"])
        pedrinhas = Cena(DI["PEDRINHAS"])
        aranhas = Cena(DI["ARANHAS"])
        mumia = Cena(DI["MUMIA"])
        templo.direita = artefato
        artefato.esquerda = templo
        artefato.direita = fogo
        fogo.esquerda = artefato
        fogo.direita = desmoronamento
        desmoronamento.esquerda = fogo
        desmonoramento.direita = cobra
        cobra.esquerda = desmonoramento
        cobra.direita = pedrinhas
        pedrinhas.esquerda = cobra
        pedrinhas.direita = aranhas
        aranhas.esquerda = pedrinhas
        aranhas.direita = mumia
        mumia.esquerda = aranhas
        templo.vai()
        
class Carta:
    def __init__(self):
        self.cartas = [Cena(DI[uma_imagem]) for uma_imagem in IMAGENS]
        for ordem, carta in enumerate(self.cartas):
            if ordem < len(self.cartas)-2:
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
        pass
    
inca = Jogo()  # Inca()

if __name__ == "__main__":
    inca.inicia() 
    
    

   