# margaret.stacy.main.py
""" Tesouro Inca - versão texto uma aventura de exploração """

__author__ = "Victória Regina Caruzo victorialourencocaruzo@gmail.com"
__version__ = "19.11.05"
from random import randint

class CamaraPerigosa:
    """ Uma camara contendo um perigos mortais. O jogador entra nela quando se invoca o método vai """
    def __init__(self, outra):
        self.tipos = ["aranha", "fogo", "mumia", "cobra", "desabammento"]
        self.camara = "Você entrou numa câmara com {}."
        self.perigos = {tipo :0 for tipo in self.tipos}
        self.perigo_mortal = None
        self.outra = outra
        
    def sai(self):
        per_m = self.perigo_mortal
        quantos = self.perigos[per_m]
        input(f"Você sai do templo, mas encontrou {quantos} {per-m}")

    def vai(self):
        continua = " Segue para outra câmara? (s/N)"
        tipo_do_perigo = self.tipos[randint(0,5)]
        if input(self.camara.format(tipo_do_perigo)+continua) == "s":
            self.perigos[tipo_do_perigo] = self.perigos[tipo_do_perigo] + 1
            if self.perigos[tipo_do_perigo] > 1 :
                self.perigo_mortal = tipo_do_perigo
                input("Você foge assustado para a entrada do templo")
                self.sai()
                self.outra.perde()
                return self.perigos
            
            if randint(0,9) > 3:
                return self.outra.vai()
            else:
                return self.vai()
        else:
            input("Você volta para a entrada do templo")
            self.sai()
            self.outra.sai()
            return self.perigos
           

class CamaraSecreta:
    """ Uma camara contendo um conteúdo misterioso. O jogador entra nela quando se invoca o método vai """
    def __init__(self, outra):
        self.camara = "Você entrou numa câmara com tesouros."
        self.tesouros = 0
        self.outra = outra
        
    def perde(self):
        input(f"Você fugiu do templo e perdeu {self.tesouros} tesouros:")
        
    def sai(self):
        input(f"Você sai do templo com {self.tesouros} tesouros:")
        
    def vai(self):
        continua = "Segue para outra câmara? (s/N)"
        if input(self.camara+continua) == "s":
            self.tesouros = self.tesouros + 1
            if randint(0,9) > 6:
                return self.outra.vai()
            else:
                return self.vai()
        else:
            input("Você volta para a entrada do templo")
            self.sai()
            self.outra.sai()
            return self.tesouros

class JogoDoTesouroInca:
    """ O jogo do tesouro inca. O jogo começa quando se invoca o método vai """
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