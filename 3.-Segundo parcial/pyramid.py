'''
Created on 04/10/2014
funcion para una piramide con x escalones
@author: A01221672
'''
from Tkinter import *
import math
def pyramid(stairs):
    ventana = Tk()
    width =400
    height = 400
    lienzo =Canvas(ventana, width= width, height=height)
    lienzo.pack()

    for y in range(0,height,int((height/stairs))):
        lienzo.create_line(0+y/2,height-y,
                           width-y/2,height-y)


pyramid(100)

