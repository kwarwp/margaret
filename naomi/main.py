# margaret.naomi.main.py
from _spy.vitollino.main import Cena
IMAGENS = ["CENA", "TESOURO"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/inzdUaq.jpg"
DI["TESOURO"] = "https://i.imgur.com/DJNXWXY.jpg"
DI["FOGO"] = " https://i.imgur.com/yufZlvN.jpg"
DI["DESMORONAMENTO"] = "https://i.imgur.com/uMSX7Ka.jpg"
class Inca:
    def inicia(self):
        templo = Cena(DI["CENA"])
        tesouro = Cena(DI["TESOURO"])
        fogo = Cena(DI["FOGO"])
        desmoronamento = Cena(DI["DESMORONAMENTO"])
        templo.direita = tesouro
        tesouro.esquerda = templo
        tesouro.direita = fogo
        fogo.esquerda = tesouro
        fogo.direita = desmoronamento
        desmoronamento.esquerda = fogo
        templo.vai()
        
class Carta:
    pass
    def baralho(self):
        return []
        
class Jogo:
    def __init__(self):
        self.baralho = Carta().baralho()
        self.templo = Cena(DI["TEMPLO"])
    def inicia(self):
    
    
inca = Jogo()  

if __name__ == "__main__":
    inca.inicia() 
    
    

   