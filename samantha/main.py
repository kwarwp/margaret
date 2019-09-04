# margaret.samantha.main.py
from _spy.vitollino.main import Cena
TEMPLO = "https://i.imgur.com/Gr3jyiF.jpg"
TESOURO = "https://i.imgur.com/ykncQGm.jpg"
PERIGOS = {
       "MUMIA": "",
       "COBRA": ""

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
         
jogo = Jogo()
jogo.inicia()




