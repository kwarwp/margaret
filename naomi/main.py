# margaret.naomi.main.py
from _spy.vitollino.main import Cena
IMAGENS = ["CENA", "ARTEFATO" , "FOGO" , "DESMORONAMENTO" , "COBRA"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/inzdUaq.jpg"
DI["ARTEFATO"] = "https://i.imgur.com/DJNXWXY.jpg"
DI["FOGO"] = " https://i.imgur.com/yufZlvN.jpg"
DI["DESMORONAMENTO"] = "https://i.imgur.com/uMSX7Ka.jpg"
DI["COBRA"] = "https://i.imgur.com/UcWZh28.jpg"
class Inca:
    def inicia(self):
        templo = Cena(DI["CENA"])
        artefato = Cena(DI["ARTEFATO"])
        fogo = Cena(DI["FOGO"])
        desmoronamento = Cena(DI["DESMORONAMENTO"])
        cobra = Cena(DI["COBRA"])
        templo.direita = artefato
        artefato.esquerda = templo
        artefato.direita = fogo
        fogo.esquerda = artefato
        fogo.direita = desmoronamento
        desmoronamento.esquerda = fogo
        desmonoramento.direita = cobra
        cobra.esquerda = desmonoramento
        templo.vai()
        
class Carta:
    def __init__(self):
        self.cartas = [Cena(RDI[uma_imagem]) for uma_imagem in IMAGENS]
    def baralho(self):
        return self.cartas
        
class Jogo:
    def __init__(self):
        self.baralho = Carta().baralho()
        self.templo = Cena(DI["CENA"])
        self.templo.direita = self.baralho[0]
    def inicia(self):
        self.templo.vai()
        pass
    
inca = Jogo()  # Inca()

if __name__ == "__main__":
    inca.inicia() 
    
    

   