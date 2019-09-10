# margaret.naomi.main.py
__author__ = "Raquel P. R. Santos raquelp737@gmail.com"
from _spy.vitollino.main import Cena
from random import shuffle
IMAGENS = ["CENA" , "ARTEFATO" , "FOGO" , "DESMORONAMENTO" , "COBRA" , "PEDRINHAS" , "ARANHA" , "MUMIA" , "SALA DO TESOURO" , "PEPITAS DE OURO" , "OBSIDIANA" , "TURQUESA" , "ACAMPAMENTO"]*5 
shuffle(IMAGENS) 
Perigo = {}
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/inzdUaq.jpg"
DI["ARTEFATO"] = "https://i.imgur.com/DJNXWXY.jpg"
DI["FOGO"] = " https://i.imgur.com/yufZlvN.jpg"
DI["DESMORONAMENTO"] = "https://i.imgur.com/uMSX7Ka.jpg"
DI["COBRA"] = "https://i.imgur.com/UcWZh28.jpg"
DI["PEDRINHAS"] = "https://i.imgur.com/ijt1Hbq.jpg"
DI["ARANHA"] = "https://i.imgur.com/opdKFGa.jpg "
DI["MUMIA"] = "https://i.imgur.com/75NssMI.jpg "
DI["SALA DO TESOURO"] = "https://i.imgur.com/w3DPsMb.jpg"
DI["PEPITAS DE OURO"] = "https://i.imgur.com/amIQQ8Z.jpg"
DI["OBSIDIANA"] = "https://i.imgur.com/ShXGOw0.png"
DI["TURQUESA"] = " "
ACAMPAMENTO = Cena("https://i.imgur.com/MEl27uM.png")
class Perigo:
    def __init__(self, imagem, tipo):
        self.cena = Cena(imagem)
        self.tipo =tipo
        self.cena_vai = self.cena.vai
        self.cena.vai = self.vai
        self.acampamento = ACAMPAMENTO
        
    def set_direita(self, direita):   
        self.cena.diereita = direita
        
    def set_esquerda(self, esquerda):   
        self.cena.esquerda = esquerda
        
    def vai(self):
        if self.tipo in PERIGOS:
            #deu ruim, já tinha aparecido um perigo
            self.cena.direita = self.acampamento
        else:
            PERIGOS[self.tipo] = 1
        self.cena_vai()
        
class CARTA:  
    def __init__(self):
        self.cartas = [Perigo(DI[uma_imagem], uma_imagem) 
             for uma_imagem in IMAGEM
        for ordem, carta in enumerate(self.cartas):
            if ordem < len(self.cartas)-1:
                carta.set_direita(self.cartas[ordem+1])
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
    
    

    