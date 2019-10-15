# margaret.camara0.main.py
"""
Tesouro Inca - O Templo
"""
__author__ = "Junior"
class Templo:
    def Templo(self):
        print("chega no templo")

class Camara:
    """ A camara é o lugar do jogo """
    def __init__(self):
        """ as camaras são as divisões do templo """
        self.camara = camara()  # importa a camara de outro módulo
        self.explorador = explorador()  # cria um explorador
    
    def inicia(self):
        """ dá inicio ao jogo, fazendo o explorador entrar na primmeira câmara """
        self.camara.entrar(self.explorador)

if __name__ == "__main__":
    camara = Camara()
    camara.inicia()