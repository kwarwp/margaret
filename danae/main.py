# margaret.danae.main.py
""" Tesouro Inca - versão texto
Uma aventura de exploração
"""
__author__ = "Carlo Oliveira <carlo at ufrj br>"
__version__ = "19.11.05a"


class JogoDoTesouroInca:
    """ O jogo do tesouro inca. 
    O jogo começa quando se invoca o método vai
    """
    def __init__(self):
        self.templo = "Você está diante de um templo Inca"
        
    def vai(self):
        print(self.templo)


if __name__ == "__main__":
    tesouro = JogoDoTesouroInca()
    tesouro.vai()