# margaret.soraya.main.py
__author__ "Vitória da Costa Lima vitcardinnot@gmail.com
from spy.vitollino.main import Cena
DI = DICIONARIO_DE_IMAGENS = {} 
"CENA" = ""
"TESOURO" = "https://i.imgur.com/tI5hg9u.jpg"
TEMPLO = "https://i.imgur.com/jnxWklS.jpg"
COBRA = "
DESABAMENTO =
MUMIA =
ARANHA =
FOGO =

templo = Cena(CENA)
tesouro = Cena(TESOURO)
templo.direta = tesouro
tesouro.esquerda = templo
tesouro.direita = aranha
aranha.esquerda = tesouro
templo.vai()
