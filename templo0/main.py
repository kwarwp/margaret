# margaret.templo0.main.py
"""
Tesouro Inca - O Templo
"""
__author__ = "Carlo"

class Camara:
    def __init__(self):
        print("criou camara")
        
    def entra(self, explorador):
        print("explorador entrou na camara")
        explorador.pilhagem()

class Explorador:
    def __init__(self, camara):
        self.camara = camara
        print("criou explorador")
        
    def pilhagem(self):
        """ saqueia a camara e fica com o tesouro"""
        print("saqueia a camara")
        if input("continua?") == "s":
            self.camara.entra(self)

class Templo:
    """ O Templo Inca com camaras secretas """
    def __init__(self):
        """ Cria o templo com suas camaras e também o explorador """
        self.camara = Camara()  # importa a Camara de outro módulo
        self.explorador = Explorador(self.camara)  # cria um explorador
        
    def inicia(self):
        """ dá início ao jogo, fazendo o explorador entrar
            na primeira câmara
        """
        self.camara.entra(self.explorador)

if __name__ == "__main__":
    templo = Templo()
    templo.inicia()
    