# margaret.sara.main.py
__author__ = "Luiza Busnardo busnardo.luiza@gmail.com"

from _spy.vitollino.main import Cena, STYLE, INVENTARIO
STYLE["width"] = 600
STYLE["height"] = 600
from random import shuffle
IMAGENS = ["CENA", "ACAMPAMENTO", "MOCHILA", "ARTEFATO1", "MONSTRO", "PEDRAS", "FOGO", "DESABAMENTO", "COBRA", "ARANHA", "SALADOTESOURO", "OBSIDIANA", "TURQUESA", "PEPITADEOURO"]*5
shuffle(IMAGENS)
DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/ZzWag8V.jpg"
DI["CENA"] = "https://i.imgur.com/ZzWag8V.jpg"
DI["ACAMPAMENTO"] = "https://i.imgur.com/3QWHNYM.jpg"
DI["MOCHILA"] = "https://i.imgur.com/UCQvviq.jpg"
DI["ARTEFATO1"] = "https://i.imgur.com/0t0j5Ne.jpg"
DI["MONSTRO"] = "https://i.imgur.com/zwbxMeu.jpg"
DI["PEDRAS"] = "https://i.imgur.com/fvnFDJl.jpg"
DI["FOGO"] = "https://i.imgur.com/sIq24MI.jpg"
DI["DESABAMENTO"] = "https://i.imgur.com/iEjnRsA.jpg"
DI["COBRA"] = "https://i.imgur.com/BRCXuz3.jpg"
DI["ARANHA"] = "https://i.imgur.com/VxTxDTj.jpg"
DI["SALADOTESOURO"] = "https://i.imgur.com/PQV7tEW.jpg"
DI["OBSIDIANA"] = "https://i.imgur.com/WAYaUV7.jpg"
DI["PEPITADEOURO"] = "https://i.imgur.com/5MmC1SO.jpg"
DI["TURQUESA"] = "https://i.imgur.com/KXbOQJv.jpg"

class Acampamento:
    def __init__(self):
        """ o que tem que ter no acampamento?"""
        self.cena = Cena("https://i.imgur.com/dmSDeDF.jpg")
        
    def vai(self):
        self.cena.vai()
    


class Jogador:
    def __init__(self, acampamento):
        """ o que tem que ter no jogador?
            o jogador ganha uma turquesa para cada camara
        """
        self.turquesa = 0
        self.acampamento = acampamento
        # Aparato para capturar a ação clica na direita
        self.cena_continua = Cena() # Chupa-cabras
        self.cena_continua.vai = self.continua
        # Aparato para capturar a ação clica na esquerda
        self.cena_desiste = Cena()
        self.cena_desiste.vai = self.desiste

        
    def continua(self):
        """ entra em nova camara e acumula turquesas """
        self.turquesa = self.turquesa + 1
        pass
    def ganha_uma_turquesa(self, onde):
        """
        ouro = turquesa // 10
        sobra_ouro = ouro % 10
        obsidiana = sobra_ouro // 5
        tur = sobra_ouro % 5
        """
        lugar =  50*onde
        tur = Elemento(TURQUESA,  tit="Turquesa",
            style=dict(left=f"{lugar}px", top="350px", width="50px",
            height="30px"),
                       cena=self.acampamento.cena)

        
    def desiste(self):
        """ segue para o acampamento"""
        self.coleta_tesouro()
        self.acampamento.vai()
        
    def coleta_tesouro(self):
        for tur in range(self.turquesa):
            self.ganha_uma_turquesa(tur)
        

class Perigo:
    def __init__(self, imagem, tipo, jogador):
        self.jogador = jogador
        self.cena = Cena(imagem)
        self.tipo = tipo
        # chupa cabra -- aparato
        self.cena_vai = self.cena.vai
        self.cena.vai = self.vai
        self.acampamento = jogador.acampamento
        self.set_esquerda(jogador.cena_desiste)

    def set_direita(self, direita):
        self.cena.direita = direita

    def set_esquerda(self, esquerda):
        self.cena.esquerda = esquerda
    
        
    def vai(self):
        if self.tipo in PERIGOS:
            # deu ruim, já tinha aperecido um perigo
            self.cena.direita = self.acampamento
        else:
            PERIGOS[self.tipo] = 1
        self.jogador.continua()
        self.cena_vai()


class Tesouro(Perigo):
    def __init__(self, imagem, tipo, jogador):
        super().__init__(imagem, tipo, jogador)
        
class Carta:
    def __init__(self, jogador):
        self.jogador = jogador
        self.cartas = [Perigo(
                              DI[uma_imagem],
                              uma_imagem,
                              jogador) 
            for uma_imagem in IMAGENS]
        for ordem, carta in enumerate(self.cartas):
            if ordem < len(self.cartas)-1:
                carta.set_direita(self.cartas[ordem+1])
    def baralho(self):
        return self.cartas
        
class Jogo:
    def __init__(self):
        global PERIGOS
        PERIGOS ={}
        INVENTARIO.inicia()
        #INVENTARIO.bota(tur)
        self.acampamento = Acampamento()
        self.jogador = Jogador(self.acampamento)
        self.baralho = Carta(self.jogador).baralho()
        self.templo = Cena(DI["TEMPLO"])
        #self.templo = Perigo(tipo="TEMPLO", imagem=DI["TEMPLO"])
        self.templo.direita = self.baralho[1]
    def inicia(self):
        self.templo.vai()
        

inca = Jogo()  # Inca()

if __name__ == "__main__":
    inca.inicia()
    