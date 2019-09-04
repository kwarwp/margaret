# margaret.grace.main.py
from _spy.vitollino.main import Cena
TEMPLO = "https://i.imgur.com/g3Vskr9.png"
TESOURO = "https://i.imgur.com/MnqQYCC.png"
OBSTACULOS = {
    "MUMIA": "https://i.imgur.com/bxlDc1a.png",
    "COBRA": "https://i.imgur.com/rg2rxco.png",
    "FOGO": "https://i.imgur.com/jn2xy4p.png",
    "ARANHA": "https://i.imgur.com/EQXhklf.png"
    #"DESABAMENTO": ""
}

class Cartas:
    def __init__(self):
        self.baralho = [Cena(obstaculos) 
             for obstaculos in OBSTACULOS.values()] * 5
        shuffle(self.baralho)
        baralho_amanha = self.baralho[1:]
        baralho_zip = zip(self.baralho, baralho_amanha)
        for c_hoje, c_ama in baralho_zip:
            c_hoje.direita = c_ama
            c_ama.esquerda = c_hoje
            
    def primeira_carta(self):
        return self.baralho[0]
        
        
class Jogo:
    def inicia(self):
        templo = Cena(TEMPLO)
        tesouro = Cena(TESOURO)
        templo.direita = tesouro
        tesouro.esquerda = templo
        obstaculos = Cartas ()
        umobstaculo = obstaculos.primeira_carta()
        tesouro.direita = umobstaculo
        umobstaculo.esquerda = tesouro
        templo.vai()
        
            
jogo = Jogo()
jogo.inicia()