# margaret.templo0.main.py
"""
Tesouro Inca - O Templo
"""
__author__ = "Carlo"

class Cabana:
    """ onde o explorador guarda os tesouros """
    def __init__(self):
        self.tesouro = 0
        print(f"criou cabana contendo {self.tesouro} tesouros")
        
    def entra(self, explorador):
        """ entra e saqueia esta camara """
        print("explorador entrou na cabana")
        self.tesouro += explorador.guarda_butim()
        print(f"explorador guarda na cabana {self.tesouro} tesouros")
        if input("entra na camara de novo?") == "s":
            explorador.retorna()

class Camara:
    def __init__(self):
        print("criou camara")
        self.cabana = Cabana()
        
    def entra(self, explorador):
        """ entra e saqueia esta camara """
        print("explorador entrou na camara")
        explorador.pilhagem()
        
    def sai(self, explorador):
        print("explorador desiste de explorar e sai da camara")
        self.cabana.entra(explorador)

class Explorador:
    def __init__(self, camara):
        self.camara = camara
        self.butim = 0
        print(f"criou explorador com butim {self.butim}")
        
    def retorna(self):
        """ volta a explorar a camara"""
        print("Você decide buscar novos tesouros")
        self.camara.entra(self)
        
    def guarda_butim(self):
        """ coloca o butim que está carregando na segurança da cabana"""
        self.butim, guarda = 0, self.butim
        return guarda
        
    def pilhagem(self):
        """ saqueia a camara e fica com o tesouro"""
        self.butim += 1
        print(f"saqueia a camara e fica com {self.butim} tesouros")
        if input(f"voce já tem {self.butim} tesouros,continua?") == "s":
            self.camara.entra(self)
        else:
            self.camara.sai(self)

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
    