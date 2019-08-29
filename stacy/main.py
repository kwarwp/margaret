# margaret.stacy.main.py
from _spy.vitollino.main import Cena
from random import shuffle
TEMPLO = "https://i.imgur.com/dQqwYul.jpg"
TESOURO = "https://i.imgur.com/Nq1hCeU.jpg"
FOGO = "https://i.imgur.com/A6Z2zqB.jpg"
ARTEFATO1 = "https://i.imgur.com/1QHNdyI.jpg"
COBRA = "https://i.imgur.com/MydpgBT.jpg"
DESABAMENTO = "https://i.imgur.com/jnxWklS.jpg"
MUMIA = "https://i.imgur.com/3215w01.jpg" 
ARANHA = "http://varg.wdfiles.com/local--files/sr-annals-1/Spiders.jpg"

templo = Cena(TEMPLO)
templo.vai()
tesouro = Cena(TESOURO)
tesouro.vai()
fogo = Cena(FOGO)
fogo.vai()
artefato1 = Cena(ARTEFATO1)
artefato1.vai()
cobra = Cena(COBRA)
cobra.vai()
desabamento = Cena(DESABAMENTO)
desabamento.vai()
mumia = Cena(MUMIA)
mumia.vai()
aranha = Cena(ARANHA)
aranha.vai()

def decisao (anterior,carta):
    resposta = input ("Você descobriu uma câmara do templo. Você entra nela ou sai?")
    if resposta == "entro": 
        carta.vai() 
    elif resposta == "saio":
        anterior.vai()

cartas = [(TESOURO), (FOGO), (ARTEFATO1), (DESABAMENTO), (MUMIA), (ARANHA), (COBRA)]
baralho = cartas[:] # Copy cartas
shuffle(baralho) # Shuffle baralho
for elemento in cartas
elemento.vai


# decisao(tesouro, fogo)