from tkinter import *
import os
from SelectPath import SelecionarPastaArquivos as sp

pastaApp = os.path.dirname(__file__)

def Importar():
    print("Importando arquivos...")

def SelecionaPastas():
    exec(open(pastaApp+"\\SelecionaPastas.py").read())


#Cria a janela
app = Tk()

app.title("Alfa PDF")
app.geometry("500x300")
app.configure(background="#dde")

#Criando a barra de menus
barraDeMenus = Menu(app)

menuArquivo = Menu(barraDeMenus, tearoff=0)
menuArquivo.add_command(label="Selecionar pasta", command= SelecionaPastas)
menuArquivo.add_command(label="Agrupar", command= Importar)
menuArquivo.add_command(label="Separar", command= Importar)
menuArquivo.add_separator()
menuArquivo.add_command(label="Fechar", command= app.quit)

menuOpcoes = Menu(barraDeMenus, tearoff=0)
menuOpcoes.add_command(label="Abrir local", command= sp)
menuOpcoes.add_command(label="Enviar para...", command= sp)

menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="Alfa PDF", command=sp)

barraDeMenus.add_cascade(label="Arquivo", menu=menuArquivo)
barraDeMenus.add_cascade(label="Opções", menu=menuOpcoes)
barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)

app.config(menu=barraDeMenus)
app.mainloop()