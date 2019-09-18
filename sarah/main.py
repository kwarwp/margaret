# margaret.julia.main.py
from _spy.vitollino.main import Cena
TEMPLO = "https://i.imgur.com/eiRyeJf.jpg"
TURQUESA = "https://i.imgur.com/jcJOmVD.png"
ARANHA = "https://i.imgur.com/lt6nVqj.gif"

class Carta:
	def __init__(self):
		self.carta = Cena(ARANHA).vai()  
        
	def vai(self):
     	 self.carta.vai()
         
	def anterior(self, anterior):
		anterior.direita = self.carta
		self.carta.esquerda = anterior
    

class Jogo:
	def __init__(self):
		self.templo = Cena(TEMPLO)
		self.carta = Carta()
		self.carta.proximo(self.templo)
		self.templo.vai()
        
        
if __name__ == "__main__":
	Jogo()