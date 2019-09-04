# margaret.sarah.main.py
from _spy.vitollino.main import Cena
#Quando Classe inicia em maiuscula, quando constante não é maiuscula
TEMPLO = "https://i.imgur.com/Tsxuzh2.jpg"
TESOURO = "https://i.imgur.com/W46GoNq.gif"

#DICIONARIO DE PERIGOS
PERIGOS ={
     "MUMIA":"https://i.imgur.com/shYk8Eo.gif",
     "COBRA":"https://i.imgur.com/ndlMANn.png", 
     "DESLIZAMENTO":"https://i.imgur.com/IJG5OKr.png", 
     "FOGO":"https://i.imgur.com/zaHCVGP.png", 
     "ARANHA":"https://i.imgur.com/25KhwPC.png"
}
class Cartas:
    def __init__(self): #dunder
        #nosso baralho é uma lista
        #self.baralho = []
        #self.baralho[0] = Cena(PERIGOS["MUMIA"]) #Para não ter que fazer isso para todos os perigos usamos:
        #self.baralho = [façaalgo for perigo in PERIGOS.VALUES] EU QUERO SABER TODOS OS VALORES EXISTENTES NO PERIGO
        self.baralho = [Cena(perigo) 
        for perigo in PERIGOS.values()] #este for faz parte da linha de cima
        #list compreension crie uma cena com este perigo
        #baralho de hoje (é esse ai em cima)e o baralho de amanha
        baralho_amanha = self.baralho[1:]#conte a partir da 1ª posição e vá até o fim slice
        #self parece com gestalt (eu mesmo) na classe posso trabalhar com coisas minhas e com coisas dos outros
        #trabalha com conjundo de objetos diferentes meu e dos outros.
        baralho_zip = zip(self.baralho,baralho_amanha)
        for c_hoje, c_ama in baralho_zip: 
        #este for e outro comando tem que separar mesmo
        c_hoje.direita = c_ama
        c_ama.esquerda = c_hoje
        #até aqui só definiu mas aind anão usou as cartas
    def primeira_carta(self):
        return self.baralho[0]

class Jogo:
    def inicia(self):
        templo = Cena(TEMPLO)
        #templo nome de uma instancia de um objeto
        #cena é uma instancia de uma classe
        tesouro = Cena(TESOURO)
        templo.direita = tesouro
        tesouro.esquerda = templo
        perigos = Cartas() #serviço oferecido pelas cartas
        #mumia = perigos.baralho[0] #
        umperigo = perigos.primeira_carta()
        
        #mumia = Cena(PERIGOS["MUMIA"])
        tesouro.direita = mumia
        mumia.esquerda = tesouro
        templo.vai()


        
jogo = Jogo()
jogo.inicia()

