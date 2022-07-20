from tkinter import *
import os
from SelectPath import *
from windows import *

pastaApp = os.path.dirname(__file__)
SelecionaPas = "SelecionaPastas"
def Importar():  
    print("Importando arquivos...")

#Abre a janela SelecionaPastas.py
def SelecionaPastas():
    exec(open(pastaApp+"\\SelecionaPastas.py").read())
    

#Cria a janela
app = Tk()

window_width = 500
window_height = 300
app.title("Alfa PDF")
app.configure(background="#dde")
CentralizarJanela(window_width,window_height,app)

#==========Criando a barra de menu==================
barraDeMenus = Menu(app)

menuArquivo = Menu(barraDeMenus, tearoff=0)
menuArquivo.add_command(label="Selecionar pasta", command= SelecionaPastas)
menuArquivo.add_command(label="Agrupar", command= Importar)
menuArquivo.add_command(label="Separar", command= Importar)
menuArquivo.add_separator()
menuArquivo.add_command(label="Fechar", command= app.quit)

menuOpcoes = Menu(barraDeMenus, tearoff=0)
menuOpcoes.add_command(label="Abrir local", command= SelecionarPastaArquivos)
menuOpcoes.add_command(label="Enviar para...", command= SelecionarPastaArquivos)

menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="Alfa PDF", command=SelecionarPastaArquivos)

barraDeMenus.add_cascade(label="Arquivo", menu=menuArquivo)
barraDeMenus.add_cascade(label="Opções", menu=menuOpcoes)
barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)

app.config(menu=barraDeMenus)
app.mainloop()