# margaret.danae.main.py
""" Tesouro Inca - versão texto
Uma aventura de exploração
"""
__author__ = "Carlo Oliveira <carlo at ufrj br>"
__version__ = "19.11.05e"

class CamaraPerigosa:
    """ Uma camara contendo um perigos mortais. 
    O jogador entra nela quando se invoca o método vai
    """
    def __init__(self, outra):
        self.camara = "Você entrou numa câmara com perigos."
        self.perigos = 0
        self.outra = outra
        
    def vai(self):
        continua = " Segue para outra câmara? (s/N)"
        if input(self.camara+continua) == "s":
            self.perigos = self.perigos + 1
            return self.outra.vai()
        else:
            input("Você volta para a entrada do templo")
            input(f"Você sai do templo mas encontrou {self.perigos} perigos")
            return self.tesouros

class CamaraSecreta:
    """ Uma camara contendo um conteúdo misterioso. 
    O jogador entra nela quando se invoca o método vai
    """
    def __init__(self, outra):
        self.camara = "Você entrou numa câmara com tesouros."
        self.tesouros = 0
        self.outra = outra
        
    def vai(self):
        continua = " Segue para outra câmara? (s/N)"
        if input(self.camara+continua) == "s":
            self.tesouros = self.tesouros + 1
            return self.outra.vai()
        else:
            input("Você volta para a entrada do templo")
            input(f"Você sai do templo com {self.tesouros} tesouros:")
            return self.tesouros

class JogoDoTesouroInca:
    """ O jogo do tesouro inca. 
    O jogo começa quando se invoca o método vai
    """
    def __init__(self):
        self.templo = "Você está diante de um templo Inca."
        tesouro = CamaraSecreta(None)
        self.camara = CamaraPerigosa(tesouro)
        tesouro.outra = self.camara
        
    def vai(self):
        continua = " Você vai entrar? (s/N)"
        if input(self.templo+continua) == "s":
            input("Você se embrenha no templo, e explora")
            muitos = self.camara.vai()
        else:
            input("Você sabiamente desiste desta loucura")


if __name__ == "__main__":
    tesouro = JogoDoTesouroInca()
    tesouro.vai()