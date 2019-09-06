# margaret.soraya.main.py
__author__ "Vitória da Costa Lima vitcardinnot@gmail.com
from spy.vitollino.main import Cena
CENA = ""
TESOURO = ""
templo = Cena(CENA)
tesouro = Cena(TESOURO)
templo.direta = tesouro
tesouro.esquerda = templo
tesouro.direita = aranha
aranha.esquerda = tesouro
templo.vai()