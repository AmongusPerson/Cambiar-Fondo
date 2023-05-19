from tkinter import *
import random
import numpy as np

pg = Tk()
pg.geometry("500x500")
pg.title("Cambiar Fondo")

array = ["red","blue","pink","black","orange","purple","green"]

def fn1():
    r = random.randint(0,259)
    g = random.randint(0,259)
    b = random.randint(0,259)
    color_rgb = (r, g, b)
    vr = random.randint(0, 6)
    color = array[vr]
    pg.configure(background = color)
    
bt1 = Button(pg, text="Ejecutar", command=fn1)
bt1.place(relx=0.5, rely=0.5, anchor=CENTER,)

pg.mainloop()