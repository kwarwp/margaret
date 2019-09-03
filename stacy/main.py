# margaret.stacy.main.py
from _spy.vitollino.main import Cena
IMAGENS = ["TEMPLO", "TESOURO", "FOGO", "ARTEFATO1", "COBRA", "DESABAMENTO", "MUMIA", "ARANHA"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/LXptu0U.jpg"
DI["TESOURO"] = "https://i.imgur.com/Nq1hCeU.jpg"
DI["FOGO"] = "https://i.imgur.com/KRK66bR.jpg"
DI["ARTEFATO1"] = "https://i.imgur.com/1QHNdyI.jpg"
DI["COBRA"] = "https://i.imgur.com/MydpgBT.jpg"
DI["DESABAMENTO"] = "https://i.imgur.com/jnxWklS.jpg"
DI["MUMIA"] = "https://i.imgur.com/HPp1k5T.jpg" 
DI["ARANHA"] = "https://i.imgur.com/w90m1jf.jpg"

class Inca:
    def inicia(self):
        templo = Cena(DI["TEMPLO"])
        tesouro = Cena(DI["TEMPLO"])
        fogo = Cena(FOGO)
        artefato1 = Cena(ARTEFATO1)
        cobra = Cena(COBRA)
        desabamento = Cena(DESABAMENTO)
        mumia = Cena(MUMIA)
        aranha = Cena(ARANHA)


