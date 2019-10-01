# margaret.stacy.main.py
__author__ = "Victória Regina Caruzo victorialourencocaruzo@gmail.com"
from _spy.vitollino.main import Cena, STYLE, Elemento, INVENTARIO
STYLE["width"] = 800
STYLE["height"] = 800
from random import shuffle
PERIGOS = ["FOGO", "COBRA", "DESABAMENTO", "MUMIA", "ARANHA"]*5
PEDRAS = ["PEPITADEOURO", "OBSIDIANA", "TURQUESA"]*20
shuffle(PERIGOS, PEDRAS)
PERIGOS = {}

DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/LXptu0U.jpg"
DI["TESOURO"] = "https://i.imgur.com/Nq1hCeU.jpg"
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

class Acampamento:
    def __init__(self):
        """ o que tem que ter no acampamento? """
        self.cena = Cena("https://i.imgur.com/wgcVh9M.jpg")
                        
    def vai(self):
        self.cena.vai()
        
class Jogador:
    def __init__(self, acampamento):
        """ o que tem que ter no jogador? 
            o jogador ganha uma turquesa para cada camara """
        self.turquesa = 0
        self.acampamento = acampamento
        self.cena_continua = Cena()
        self.cena_continua.vai = self.continua
        self.cena_desiste = Cena()
        self.cena_desiste.vai = self.desiste
                
    def continua(self):
        """ entra em nova camara e acumula turquesa """
        self.turquesa = self.turquesa + 1
        pass
    def ganha_uma_turquesa(self, onde):
        """
        ouro = turquesa // 10
        sobra_ouro = ouro % 10
        obsidiana = sobra_ouro // 5
        tur = sobra_ouro % 5
        """
        lugar = 50*onde
        tur = Elemento(TURQUESA,  tit=DI["Turquesa"], style=dict(left=f"{lugar}px", top="350px", width="50px", height="30px"), cena=self.acampamento.cena)
    
    def desiste(self):
        " segue para o acampamento """
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
            # deu ruim, já tinha aparecido um perigo
            self.cena.direita = self.acampamento
        else:
            PERIGOS[self.tipo] = 1
        self.jogador.continua()
        self.cena_vai()
        
class Tesouro(Perigo):
    def __init__(self, imagem, tipo, jogador):
        super().__init__(imagem, tipo, jogador)


class Cartas:
    def __init__(self, jogador):
        self.jogador = jogador
        self.cartas = [Perigo(DI[uma_imagem], uma_imagem, jogador) for uma_imagem in IMAGENS]
        for ordem, cartas in enumerate(self.cartas):
            if ordem < len(self.cartas)-1:
                cartas.set_direita(self.cartas[ordem+1])
    def baralho(self):
        return self.cartas
    
class Jogo:
    def __init__(self):
        global PERIGOS
        PERIGOS = {}
        INVENTARIO.inicia()
        self.acampamento = Acampamento()
        self.jogador = Jogador(self.acampamento)
        self.baralho = Cartas(self.jogador).baralho()
        self.templo = Cena(DI["TEMPLO"])
        #self.templo = Perigo(tipo="TEMPLO", imagem=DI["TEMPLO"])
        self.templo.direita = self.baralho[1]
    def inicia(self):
        self.templo.vai()


inca = Jogo()

if __name__ == "__main__":
    inca.inicia()
    