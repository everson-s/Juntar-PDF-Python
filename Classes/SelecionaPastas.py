from tkinter import *
import os

app = Tk()

window_width = 600
window_height = 300

app.title("Selecionar pasta")
app.configure(background="#dde")

def center_screen():
    global screen_height, screen_width, x_cordinate, y_cordinate

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    app.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

center_screen()


app.mainloop()