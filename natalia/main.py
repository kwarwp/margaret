# margaret.natalia.main.py
from _spy.vitollino.main import Cena
from parisa.main import sereiamonstro
CENA = "http://i.imgur.com/loO50ff.jpg"
ARTEFATO = "https://i.imgur.com/rGbY5XC.jpg"
PEDRAS = "https://i.imgur.com/4ftVqRs.jpg"
templo = Cena(CENA)
artefato = Cena(ARTEFATO)
pedras = Cena(PEDRAS)
templo.direita = artefato
artefato.esquerda = templo
templo.vai()
artefato.direita = pedras
pedras.esquerda = artefato 
artefato.vai()
pedras.direita = sereiamonstro 
sereiamonstro.esquerda = pedras
pedras.vai()