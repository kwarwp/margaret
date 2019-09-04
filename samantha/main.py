# margaret.samantha.main.py
from _spy.vitollino.main import Cena
TEMPLO = "https://i.imgur.com/Gr3jyiF.jpg"
TESOURO = "https://i.imgur.com/ykncQGm.jpg"
PERIGOS = {
    "MUMIA": "https://i.imgur.com/3Mqa5LE.jpg",
    "COBRA": "",
    "DESMONORAMENTO": "",
    "FOGO": "",
    "ARANHA": "", 
}

class Jogo:
    def inicia(self):
        templo = Cena(TEMPLO)
        tesouro = Cena(TESOURO)
        templo.direita = tesouro
        tesouro.esquerda = templo
        mumia = Cena(PERIGOS["MUMIA"])
        tesouro.direita = mumia
        mumia.esquerda = tesouro 
        templo.vai()
class Cartas:
     def __init__(self):
            self.baralho = []
            self.baralho[0] = Cena(PERIGOS["MUMIA"])
            self.baralho = [Cena(perigos)for perigo in PERIGOS.values()]
            
jogo = Jogo()
jogo.inicia()




