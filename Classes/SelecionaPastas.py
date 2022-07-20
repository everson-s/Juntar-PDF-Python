from tkinter import *
import os
from windows import *


app = Tk()

window_width = 300
window_height = 300

app.title("Selecionar pasta")
app.configure(background="#dde")

CentralizarJanela(window_width, window_height, app)


app.mainloop()