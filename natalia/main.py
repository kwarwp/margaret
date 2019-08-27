# margaret.natalia.main.py
from _spy.vitollino.main import Cena
from _parisa.main import sereiamonstro
CENA = "http://i.imgur.com/loO50ff.jpg"
ARTEFATO = "https://i.imgur.com/rGbY5XC.jpg"
PEDRAS = "https://i.imgur.com/4ftVqRs.jpg"
templo = Cena(CENA)
artefato = Cena(ARTEFATO)
templo.direita = artefato
artefato.esquerda = templo
templo.vai()

templo = Cena(CENA)