import os
from tkinter import *

#Centraliza a janela
def CentralizarJanela(largura, altura, app):

    global screen_height, screen_width, x_cordinate, y_cordinate

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (largura/2))
    y_cordinate = int((screen_height/2) - (altura/2))

    app.geometry("{}x{}+{}+{}".format(largura, altura, x_cordinate, y_cordinate))

#Abre uma nova janela
def AbrirJanela(pastaApp, NovaJanela):
    exec(open(pastaApp + "\\" + NovaJanela + ".py").read())