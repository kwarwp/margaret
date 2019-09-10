# margaret.natalia.main.py
from _spy.vitollino.main import Cena
from parisa.main import SEREIAMONSTRO
IMAGENS = ["CENA", "PEDRAS", "TEMPLO", "ARTEFATO", "SEREIAMONSTRO"]*5
shuffle(IMAGENS)
DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/7GZetDn.jpg"
DI["TESOURO"] = "https://i.imgur.com/h8MfuRD.jpg"

class Carta:
    def __init__(self):
        self.cartas = [Cena(RDI[uma_imagem]) for uma_imagem in IMAGENS]
        for ordem, carta in enumerate(self.cartas):
            if ordem < len(self.cartas)-1:
                carta.direita = self.cartas[ordem+1]
    def baralho(self):
        return self.cartas
        
class Jogador:
    def __init__(self):
        self.chance = list(range(30))
        shuffle(self.chance)
        self.perigos, self.artefatos, self.cartas, self.rodada_corrente,\
        self.maior_tesouro, self.maior_joias, = [0]*6
        self.jogadores_jogando, self.tesouros_na_tenda, self.cartas_na_mesa,\
        self.tesouros_na_mesa, self.tesouros_jogadores, self.joias_jogadores = [[]]*6
        
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
            # deu ruim, já tinha aperecido um perigo
            self.cena.direita = self.acampamento
        else:
            PERIGOS[self.tipo] = 1
        self.cena_vai()
        
