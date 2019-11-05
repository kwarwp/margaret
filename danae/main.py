# margaret.danae.main.py
""" Tesouro Inca - versão texto
Uma aventura de exploração
"""
__author__ = "Carlo Oliveira <carlo at ufrj br>"
__version__ = "19.11.05c"

class CamaraSecreta:
    """ Uma camara contendo um conteúdo misterioso. 
    O jogador entra nela quando se invoca o método vai
    """
    def __init__(self):
        self.camara = "Você entrou numa câmara vazia."
        
    def vai(self):
        continua = " Segue para outra câmara? (s/N)"
        if input(self.camara+continua) == "s":
            self.vai()
        else:
            input("Você volta para a entrada do templo")
            return

class JogoDoTesouroInca:
    """ O jogo do tesouro inca. 
    O jogo começa quando se invoca o método vai
    """
    def __init__(self):
        self.templo = "Você está diante de um templo Inca."
        self.camara = CamaraSecreta()
        
    def vai(self):
        continua = " Você vai entrar? (s/N)"
        if input(self.templo+continua) == "s":
            input("Você se embrenha no templo, e explora")
            self.camara.vai()
            input("Você sai do templo de mãos vazias")
        else:
            input("Você sabiamente desiste desta loucura")


if __name__ == "__main__":
    tesouro = JogoDoTesouroInca()
    tesouro.vai()