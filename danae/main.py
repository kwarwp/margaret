# margaret.danae.main.py
""" Tesouro Inca - versão texto
Uma aventura de exploração

v 19.11.26b - cria uma classe baralho com perigos e tesouros
v 19.11.26a - encontra mais de um tesouro e avisa quantos tem
v 19.11.05h - o jogador foge se encontra dois perigos do mesmo tipo
v 19.11.05g - o jogador foge se encontra dois perigos quaisquer
v 19.11.05f - alterna aleatoriamente entre tesouros e perigos
"""
__author__ = "Carlo Oliveira <carlo at ufrj br>"
__version__ = "19.11.05h"
from random import randint, shuffle


class Baralho:
    """
    """
    def __init__(self):
        self.baralho = []
        self.tesouros = 0
        perigos = ["aranha", "fogo", "mumia",
                   "cobra", "desabamento"]*5
        tesouros = list(range(1,17))
        self.perigos = {tipo :0 for tipo in perigos}

        # cria os perigos
        for perigo in perigos:
            self.baralho.append(
                 CamaraPerigosa(baralho=self,tipo=perigo))
        # cria os perigos
        for tesouro in tesouros:
            self.baralho.append(
                 CamaraSecreta(baralho=self,tipo=tesouro))
                 
        shuffle(self.baralho)
    def quantos_perigos(self, tipo):
        """ verifica quantos perigos deste tipo já saiu
        """
        self.perigos[tipo] += 1
        return self.perigos[tipo]
        
    def perde(self):
        input(f"Você fugiu do templo e perdeu {self.tesouros} tesouros:")
        
    def sai(self):
        input(f"Você sai do templo com {self.tesouros} tesouros:")
    def vai(self):
        self.baralho.pop().vai()
    def acumula_tesouros(self, quantos):
        self.tesouros += quantos

class CamaraPerigosa:
    """ Uma camara contendo um perigos mortais. 
    O jogador entra nela quando se invoca o método vai
    """
    def __init__(self, baralho, tipo):
        self.baralho, self.tipo = baralho, tipo
        self.camara = f"Você entrou numa câmara com {self.tipo}."
        
    def foge(self):
        input(f"Você foge do templo porque encontrou dois {self.tipo}s")

    def vai(self):
        continua = " Segue para outra câmara? (s/N)"
        if input(self.camara+continua) == "s":
            if self.baralho.quantos_perigos(self.tipo) > 1 :
                self.foge()
                self.baralho.perde()
            else:
                return self.baralho.vai()
        else:
            input("Você volta para a entrada do templo")
            self.baralho.sai()

class CamaraSecreta:
    """ Uma camara contendo um conteúdo misterioso. 
    O jogador entra nela quando se invoca o método vai.
    O jogador pode encontrar um total entre 1 e 17 tesouros
    """
    def __init__(self, baralho, tipo):
        self.baralho, self.tipo = baralho, tipo
        self.camara = f"Você entrou numa câmara com {self.tipo} tesouros."
        
    def vai(self):
        continua = " Segue para outra câmara? (s/N)"
        if input(self.camara+continua) == "s":
            self.baralho.acumula_tesouros(self.tipo)
            
            return self.baralho.vai()
        else:
            input("Você volta para a entrada do templo")
            self.baralho.sai()

class JogoDoTesouroInca:
    """ O jogo do tesouro inca. 
    O jogo começa quando se invoca o método vai
    """
    def __init__(self):
        self.templo = "Você está diante de um templo Inca."
        self.baralho = Baralho()
        
    def vai(self):
        continua = " Você vai entrar? (s/N)"
        if input(self.templo+continua) == "s":
            input("Você se embrenha no templo, e explora")
            self.baralho.vai()
        else:
            input("Você sabiamente desiste desta loucura")


if __name__ == "__main__":
    tesouro = JogoDoTesouroInca()
    tesouro.vai()