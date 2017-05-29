'''
Created on 04/10/2014
Rotacion de una linea
@author: A01221672
'''

from Tkinter import *
import math
def animateCircle(cx,cy,r):
    ventana = Tk()
    lienzo =Canvas(ventana, width= 400, height=300, bg = "#83AF9B")
    lienzo.pack()
    angle = 0
    x = math.cos(angle)
    y = math.sin(angle)
    while True:

        lienzo.delete('all')
        lienzo.create_line (cx,cy,
                            cx+(x*r),cy+(y*r),
                            width = 5, fill = "#FE4365")
        lienzo.create_rectangle(0,300,400,250, fill = "#C8C8A9", outline ="#C8C8A9")
        lienzo.update() 
        lienzo.after(100) 
        angle += .2
        x = math.cos(angle)
        y = math.sin(angle)



animateCircle(200,150,60)
