# margaret.templo.main.py
from _spy.vitollino.main import Cena
TEMPLO = "https://i.imgur.com/IKMbeR2.jpg"


class Jogo:
    def __init__(self):
        Cena(TEMPLO).vai()
        
if __name__ == "__main__":
    Jogo()