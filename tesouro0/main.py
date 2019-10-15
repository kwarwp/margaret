# margaret.tesouro0.main.py
"""
Tesouro Inca - O Tesouro
"""
__authora__ = "Queila"

class Templo:
    """ O Templo Inca com camaras secretas """
    def __init__(self):
        """ Cria o templo com suas camaras e também o explorador """
        self.camara = Camara()  # importa a Camara de outro módulo
        self.explorador = Explorador()  # cria um explorador
        
class Camara:
    def __init__(self): 
        print("criou camara")
        
    def entra(self, explorador):
        print("explorador entrou na camara")
        explorador.pilhagem()
        
class Explorador:
    def __init__(self):
        print("criou explorador")
        
    def pilhagem(self):
        """ saqueia a camara e fica com o tesouro"""
        print("saqueia a camara")