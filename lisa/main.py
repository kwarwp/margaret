# margaret.lisa.main.py
__author__ = "Carlo E. T. Oliveira carlo@ufrj.br"
from _spy.vitollino.main import Cena, Elemento, INVENTARIO
from ruzwana.main import DI as RDI
from random import shuffle
#from stacy.main import fogo
#from natalia.main import sereiamonstro
IMAGENS = ["FOGO", "COBRA", "ARANHA", "MUMIA",
"DESMORONAMENTO"]*5
#shuffle(IMAGENS)
PERIGOS = {}
DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/7GZetDn.jpg"
DI["TESOURO"] = "https://i.imgur.com/h8MfuRD.jpg"
TURQUESA = "https://i.imgur.com/8WDBJM3.png" # DI["TURQUESA"]


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
        #self.jogador.continua()
        self.cena_vai()


class Tesouro(Perigo):
    def __init__(self, imagem, tipo, jogador):
        super().__init__(imagem, tipo, jogador)
        for tur in range(tipo+1):
            self.ganha_uma_turquesa(tur)
        
    def vai(self):
        self.jogador.continua()
        self.cena_vai()
        
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
                       cena=self.cena)
        
class Carta:
    def __init__(self, jogador):
        self.jogador = jogador
        self.cartas = [Perigo(
                              RDI[uma_imagem],
                              uma_imagem,
                              jogador) 
            for uma_imagem in IMAGENS]
        tesouros = [Tesouro(
            RDI["PEDRAS"], pedras % 5, jogador)
            for pedras in range(30)]
        self.cartas += tesouros
        shuffle(self.cartas)
        shuffle(self.cartas)
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
    