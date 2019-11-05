# margaret.stacy.main.py
""" Tesouro Inca - versão texto uma aventura de exploração """

__author__ = "Victória Regina Caruzo victorialourencocaruzo@gmail.com"
__version__ = "19.11.05a"

class CamaraSecreta:
    """ Uma camara contendo um conteúdo misterioso. O jogador entra nela quando se invoca o método vai """
    def __init__(self):
        self.camara = "Você entrou numa câmara vazia."
        
    def vai(self):
        continua = "Segue para outra câmara? (S/N)"
        if input(self.camara+continua) == "S"
            self.vai()
        else:
            input("Você volta para a entrada do templo")
            return

class JogoDoTesouroInca:
    """ O jogo do tesouro inca. O jogo começa quando se invoca o método vai """
    def __init__(self):
        self.templo = "Você está diante de um templo Inca"
        self.camara = CamaraSecreta()
        
    def vai(self):
        continua = "Você vai entrar? (S/N)"
        if input(self.templo+continua) == "S":
            input("Você se embrenha no templo, e explora")
            self.camara.vai()
        else:
            input("Você sabiamente desiste desta loucura")
        
if __name__ == "__main__":
    tesouro = JogoDoTesouroInca()
    tesouro.vai()