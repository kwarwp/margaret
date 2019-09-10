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
        
        
CENA = "http://i.imgur.com/loO50ff.jpg"
ARTEFATO = "https://i.imgur.com/rGbY5XC.jpg"
PEDRAS = "https://i.imgur.com/4ftVqRs.jpg"
templo = Cena(CENA)
artefato = Cena(ARTEFATO)
pedras = Cena(PEDRAS)
sereiamonstro = Cena(SEREIAMONSTRO)
templo.direita = artefato
artefato.esquerda = templo
templo.vai()
artefato.direita = pedras
pedras.esquerda = artefato 
artefato.vai()
pedras.direita = sereiamonstro 
sereiamonstro.esquerda = pedras
pedras.vai()
sereiamonstro.direita = fogo 
fogo.esquerda = pedras
pedras.vai()
class Jogador:
    def __init__(self):
        self.chance = list(range(30))
        shuffle(self.chance)
        self.perigos, self.artefatos, self.cartas, self.rodada_corrente,\
        self.maior_tesouro, self.maior_joias, = [0]*6
        self.jogadores_jogando, self.tesouros_na_tenda, self.cartas_na_mesa,\
        self.tesouros_na_mesa, self.tesouros_jogadores, self.joias_jogadores = [[]]*6
        
       class Jogo: 
       