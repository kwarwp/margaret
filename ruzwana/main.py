# margaret.ruzwana.main.py
__author__ = "G.L.L Almeida gabriellaleni@gmail.com"
from _spy.vitollino.main import Cena
DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/BTTqaBa.jpg"
DI["MUMIA"] = "https://i.imgur.com/T6ONIKS.jpg"
DI["PEDRAS"] = "https://i.imgur.com/fbNGz9L.jpg"
DI["DESMORONAMENTO"] = "https://i.imgur.com/WNgmQjQ.jpg"
DI["ARTEFATO"] = "https://i.imgur.com/vN9MDwx.jpg"
DI["FOGO"] = "https://i.imgur.com/Mbek5ie.jpg"
DI["ARANHA"] = "https://i.imgur.com/k2RoQqf.jpg"
DI["COBRA"] = "https://i.imgur.com/k2RoQqf.jpg"

class Inca:
    def inicia(self):
        templo = Cena(DI["TEMPLO"])
        pedras = Cena(DI["PEDRAS"])
        mumia = Cena(DI["MUMIA"])
        desmoronamento = Cena(DI["DESMORONAMENTO"])
        artefato = Cena(DI["ARTEFATO"])
        fogo = Cena(DI["FOGO"])
        aranha = Cena(DI["ARANHA"])
        cobra = Cena(DI["COBRA"])        
        templo.direita = pedras
        pedras.esquerda = templo
        pedras.direita = desmoronamento
        desmoronamento.esquerda = pedra
        desmoronamento.direita = tesouro
        tesouro.esquerda = desmoronamento
        tesouro.direita = fogo
        fogo.esquerda = tesouro
        templo.vai()
        
inca = Inca()

if __name__ == "__main__":
    inca.inicia()

        
