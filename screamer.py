from tkinter import *
from PIL import Image, ImageTk
import pygame



ssw = Tk()

def six():
    pygame.mixer.init()
    pygame.mixer.music.load("screamer.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    image = Image.open("small.gif")
    zoom = 1.8
    pixels_x, pixels_y = tuple([int(zoom * x) for x in image.size])
    toplvl = Toplevel() #топ левел виджет
    photo = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))
    lbl = Label(toplvl, image=photo)
    lbl.image = photo
    lbl.grid(row = 0, column = 0)

def base():
    la = Button(ssw, text='не нажимай сюды', command = six)
    la.grid(row = 0, column = 0)
base()
ssw.configure(background="black")
ssw.mainloop()

