'''
Created on 04/10/2014
funcion para una gradilla
@author: A01221672
'''
from tkinter import *
import math
def grid():
    for y in range(0,height,int((height/50))):
        lienzo.create_line(0,y,width,y)
    for x in range (0,width,int((width/50))):
        lienzo.create_line(x,0,x,width)
ventana = Tk()
width =400
height = 300
lienzo =Canvas(ventana, width= width, height=height)
lienzo.pack()
grid()
mainloop()
