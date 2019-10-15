# margaret.camara0.main.py
"""
Tesouro Inca - O Templo
"""
__author__ = "Junior"


class camara:
    """ A camara é o lugar do jogo """
    def _init_(self):
        """ as camaras são as divisões do templo """
        self.camara = camara()  # importa a camara de outro módulo
        self.explorador = Explorador()  # cria um explorador
    
    def inicia(self):
        """ dá inicio ao jogo, fazendo o explorador entrar
    na primmeira câmara
    """
        self.camara.entrar(self.explorador)