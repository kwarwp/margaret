# margaret.stacy.main.py
from _spy.vitollino.main import Cena
CENA = "https://i.imgur.com/ucaj8RJ.jpg"
FOGO = "https://i.imgur.com/FaPZtsh.jpg"
templo = Cena(CENA)
fogo = Cena(FOGO)
templo.direita = fogo
fogo.esquerda = templo
templo.vai()
