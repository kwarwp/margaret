# margaret.naomi.main.py
__author__ = "Raquel P. R. Santos raquelp737@gmail.com"
from _spy.vitollino.main import Cena
from random import shuffle
IMAGENS = ["CENA", "ARTEFATO" , "FOGO" , "DESMORONAMENTO" , "COBRA" , "TESOURO" , "PEDRAS PRECIOSAS"]*5
shuffle(IMAGENS)
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/inzdUaq.jpg"
DI["ARTEFATO"] = "https://i.imgur.com/DJNXWXY.jpg"
DI["FOGO"] = " https://i.imgur.com/yufZlvN.jpg"
DI["DESMORONAMENTO"] = "https://i.imgur.com/uMSX7Ka.jpg"
DI["COBRA"] = "https://i.imgur.com/UcWZh28.jpg"
DI["PEDRAS PRECIOSAS"] = " https://i.imgur.com/ijt1Hbq.jpg"
class Inca:
    def inicia(self):
        templo = Cena(DI["CENA"])
        artefato = Cena(DI["ARTEFATO"])
        fogo = Cena(DI["FOGO"])
        desmoronamento = Cena(DI["DESMORONAMENTO"])
        cobra = Cena(DI["COBRA"])
        pedras preciosas = Cena(DI["PEDRAS PRECIOSAS"])
        templo.direita = artefato
        artefato.esquerda = templo
        artefato.direita = fogo
        fogo.esquerda = artefato
        fogo.direita = desmoronamento
        desmoronamento.esquerda = fogo
        desmonoramento.direita = cobra
        cobra.esquerda = desmonoramento
        cobra.direita = pedras preciosas
        pedras preciosas.esquerda = cobra
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
    
    

   