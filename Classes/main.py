import PySimpleGUI as sg

#Criando o layout

layout = [[sg.Text("Digite o endereço da pasta:")],
          [sg.InputText()],
          [sg.OK("Juntar"), sg.Cancel()],
          ]

Window = sg.Window("Juntando PDF", layout)

while True:
    evento, valores = Window.read()
    if evento in (sg.WIN_CLOSED, "Cancelar"):
        break

Window.close()