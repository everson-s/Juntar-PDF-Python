from tkinter import *
import os
from SelectPath import *

pastaApp = os.path.dirname(__file__)

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

def center_screen():
    global screen_height, screen_width, x_cordinate, y_cordinate

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    app.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

center_screen()

#Criando a barra de menus
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