# margaret.parisa.main.py
from _spy.vitollino.main import Cena
CENA = "https://i.imgur.com/gjHwE6J.jpg"
SEREIAMONSTRO = "https://i.imgur.com/7Hfx7Vd.jpg"
FLORESTA = "https://i.imgur.com/Jfr1Ww9.jpg"
templo = Cena (CENA)
sereiamonstro = Cena(SEREIAMONSTRO)
floresta = Cena(FLORESTA)
templo.direita = sereiamonstro
sereiamonstro.esquerda = templo
sereiamonstro.direita = floresta
floresta.esquerda = templo
templo.vai()