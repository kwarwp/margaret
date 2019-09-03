# margaret.kathryn.main.py
from _spy.vitollino.main import Cena 
CENA = "https://i.imgur.com/IdXGTYa.jpg"
TESOURO = "https://i.imgur.com/78iHROq.jpg"
MUMIA = "https://i.imgur.com/7G66ctJ.png"

class Inca:
def inicia (self):
templo = Cena(CENA)
tesouro = Cena(TESOURO) 
mumia = Cena(MUMIA)
templo.direita = tesouro 
tesouro.esquerda = templo 
templo.vai()
tesouro.direita = mumia 
mumia.esquerda = tesouro 
mumia.vai()

