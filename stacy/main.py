# margaret.stacy.main.py
""" Tesouro Inca - versão texto uma aventura de exploração """

__author__ = "Victória Regina Caruzo victorialourencocaruzo@gmail.com"
__version__ = "19.11.05a"

class JogoDoTesouroInca:
    """ o jogo do tesouro inca. o jogo começa quando se invoca o método vai """
    def __init__(self):
        self.templo = "Você está diante de um templo Inca"
        
    def vai(self):
        continua = "você vai entrar? (S/N)"
        if input(self.templo+continua) == "S":
            input("você se embrenha no templo, e desaparece")
        else:
            input
        
    def vai(self):
        print(self.templo)
        
if __name__ == "__main__"
    tesouro = JogoDoTesouroInca()
    tesouro.vai()