# margaret.soraya.main.py
__author__ "Vitória da Costa Lima vitcardinnot@gmail.com
from spy.vitollino.main import Cena, STYLE
STYLE:["widht"] = 600
STYLE:["height"] = 600
from random import shuffle 
IMAGENS = ["FOGO" , "COBRA" , "DESABAMENTO" , "MUMIA" , "ARANHA"]*5
shuffle (IMAGENS)
PERIGOS = {}

DI = DICIONARIO_DE_IMAGENS = {} 
DI["TEMPLO"] = "https://i.imgur.com/jnxWklS.jpg"
DI["TESOURO"] = "https://i.imgur.com/tI5hg9u.jpg"
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
ACAMPAMENTO = Cena("https://i.imgur.com/wgcVh9M.jpg")
class Perigo:
    def __init__(self, imagem, tipo):
        self.cena = Cena(imagem)
        self.tipo = tipo
        self.cena_vai = self.cena.vai
        self.cena.vai = self.vai
        self.acampamento = ACAMPAMENTO
        
    def set_direita(self, direita):
        self.cena.direita = direita
        
    def set_esquerda(self, esquerda):
        self.cena.esquerda = esquerda
        
    def vai(self):
        if self.tipo in PERIGOS:
            # deu ruim, já tinha aparecido um perigo
            self.cena.direita = self.acampamento
        else:
            PERIGOS[self.tipo] = 1
        self.cena_vai()




class Acampamento:
     def __init__(self):
        pass
    # o que tem que ter no jogador
    # o jogador ganha uma turquesa para cada camara
     def continua(self):
        pass
      # acumula turquesa
      
     
class Jogador
      def __init__(self):
      "" o que tem que ter no jogador
         o jogador ganha uma turquesa para cada camara
      """
      self.cena_continua 
         
templo = Cena(CENA)
tesouro = Cena(TESOURO)
templo.direta = tesouro
tesouro.esquerda = templo
tesouro.direita = aranha
aranha.esquerda = tesouro
templo.vai()
