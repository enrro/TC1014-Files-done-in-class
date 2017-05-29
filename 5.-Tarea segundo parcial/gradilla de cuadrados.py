'''
Created on 14/10/2014
loops dentro de loops
Proven and tested on python 3.3.3
@author: A01221672
'''
from tkinter import*
import math
import random

x=1
y = math.sin(x)
ancho=600
alto=375
ventana = Tk()
lienzo =Canvas(ventana, width= ancho, height=alto, background ="#170A3E")
lienzo.pack()

foo = ["#C5085B","#D2FACE","#62D9CB","#E2FCC2"]

for filas in range(10):
    for columnas in range(13):
        color= random.choice(foo)
        if columnas %2 ==0:
            lienzo.create_rectangle(50*columnas,50*filas,50*columnas+30,50*filas+30,fill = color, width=0, outline=color)
        else:
            lienzo.create_rectangle(50*columnas,50*filas,50*columnas+30,50*filas+30,fill = color, width=0, outline=color)


    

mainloop()
