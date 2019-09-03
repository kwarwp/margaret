# margaret.meredith.main.py
__author__ = "Henrique Bastos <henrique@bastos.net>"
from _spy.vitollino.main import Cena
from collections import OrderedDict

CARTAS = OrderedDict((
    ("TEMPLO", "https://i.imgur.com/LXptu0U.jpg"),
    ("TESOURO", "https://i.imgur.com/Nq1hCeU.jpg"),
    ("FOGO", "https://i.imgur.com/KRK66bR.jpg"),
    ("ARTEFATO1", "https://i.imgur.com/1QHNdyI.jpg"),
    ("COBRA", "https://i.imgur.com/MydpgBT.jpg"),
    ("DESABAMENTO", "https://i.imgur.com/jnxWklS.jpg"),
    ("MUMIA", "https://i.imgur.com/HPp1k5T.jpg"),
    ("ARANHA", "https://i.imgur.com/w90m1jf.jpg")
))

class Inca:
    def inicia(self):
        self.cenas = l = [Cena(img) for img in CARTAS.values()]
        
        for a, b in zip(l[:-1], l[1:]):
            a.direita = b
            b.esquerda = a

        self.cenas[0].vai()

inca = Inca()

if __name__ == "__main__":
    inca.inicia()    