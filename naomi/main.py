# margaret.naomi.main.py
from _spy.vitollino.main import Cena
IMAGENS = ["CENA", "TESOURO"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["CENA"] = "https://i.imgur.com/inzdUaq.jpg"
DI["TESOURO"] = "https://i.imgur.com/DJNXWXY.jpg"

class Inca:
    def inicia(self):
        templo = Cena(DI["CENA"])
        tesouro = Cena(DI["TESOURO"])
        templo.dieita = tesouro
        tesouro.esquerda = templo
        templo.vai()
    
inca = Inca()

if __name__ == "__main__":
    inca.inicia() 

   