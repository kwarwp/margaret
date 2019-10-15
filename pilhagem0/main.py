# margaret.pilhagem0.main.py
"""
Tesouro Inca - A pilhagem
"""
__author__ = "Victória Regina"

class Camara:
    def __init__(self):
        print("criou camara")
        
    def entra(self, explorador):
        print("explorador entrou na camara")

class Explorador:
    def __init__(self):
        print("criou explorador")


class Pilhagem:
    """ A pilhagem é o lucro retirado do templo """
    def __init__(self):
        """ Cria a pilhagem com os seus valores """
        self.pilhagem = Pilhagem()
        self.explorador = Explorador(self.pilhagem)  # cria um explorador
        
    def inicia(self):
        """ dá início ao jogo, fazendo o explorador entrar
            na primeira câmara
        """
        self.pilhagem.entra(self.explorador)

if __name__ == "__main__":
    pilhagem = Pilhagem()
    pilhagem.inicia()
    