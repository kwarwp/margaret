# margaret.kathryn.main.py
from _spy.vitollino.main import Cena 
CENA = "http://lorempixel/300/300/city/1"
TESOURO = "https://i.imgur.com/DsncQRP.jpg"
MUMIA = "https://i.imgur.com/ardMlqr.jpg"
templo = Cena(CENA)
tesouro = Cena(TESOURO) 
mumia = Cena(MUMIA)
templo.direita = tesouro 
tesouro.esquerda = templo 
templo.vai()
tesouro.direita = mumia 
mumia.esquerda = tesouro 
mumia.vai()
