# margaret.stacy.main.py
""" Tesouro Inca - versão texto uma aventura de exploração """

__author__ = "Victória Regina Caruzo victorialourencocaruzo@gmail.com"
__version__ = "19.11.05a"

class CamaraSecreta:
    """ Uma camara contendo um conteúdo misterioso. O jogador entra nela quando se invoca o método vai """
    def __init__(self):
        self.camara = "Você entrou numa câmara com tesouros."
        self.tesouros = 0
        
    def vai(self):
        continua = "Segue para outra câmara? (s/N)"
        if input(self.camara+continua) == "s":
            self.tesouros = self.tesouros + 1
            return self.vai()
        else:
            input("Você volta para a entrada do templo")
            return self.tesouros

class JogoDoTesouroInca:
    """ O jogo do tesouro inca. O jogo começa quando se invoca o método vai """
    def __init__(self):
        self.templo = "Você está diante de um templo Inca"
        self.camara = CamaraSecreta()
        
    def vai(self):
        continua = " Você vai entrar? (s/N)"
        if input(self.templo+continua) == "s":
            input("Você se embrenha no templo, e explora")
            muitos = self.camara.vai()
            input(F"Você sai do templo com {muitos} tesouros")
        else:
            input("Você sabiamente desiste desta loucura")
        
if __name__ == "__main__":
    tesouro = JogoDoTesouroInca()
    tesouro.vai()