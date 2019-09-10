# margaret.rachel.main.py
from browser import document, html
HTML = '<img src="https://i.imgur.com/7GZetDn.jpg"></img>'
IMAGEM = "https://i.imgur.com/7GZetDn.jpg"

class Cena:
    def __init__(self, imagem):
        self.dom = document["pydiv"]
        self.cena = html.IMG(src=imagem)
        
    def vai(self):
        self.dom.html=""
        self.dom <= self.cena
        
cena = Cena(IMAGEM)
#cena.vai()
vai_seq = cena.vai
def seq_vai():
    ah = input("peguei!")
    vai_seq()
cena.vai = seq_vai
cena.vai()
