# margaret.kathryn.main.py
from _spy.vitollino.main import Cena 
CENA = "https://i.imgur.com/yPBlUJc.jpg"
TESOURO = "https://i.imgur.com/DsncQRP.jpg"
MUMIA = "https://i.imgur.com/ardMlqr.jpg"
FOGO = 
templo = Cena(CENA)
tesouro = Cena(TESOURO) 
mumia = Cena(MUMIA)
templo.direita = tesouro 
tesouro.esquerda = templo 
templo.vai()
tesouro.direita = mumia 
mumia.esquerda = tesouro 
mumia.vai()
