'''
Created on 21/10/2014
arcos de colores que se repiten en una fila y columna
Proven and tested on python 3.3.3
@author: A01221672
'''

from tkinter import *
import random

ventana=Tk()
largo = 800
ancho = 500
lienzo=Canvas(ventana,width=largo,height=ancho)
lienzo.pack()
foo = ["#7D735A","#DBAA6F","#FFCE6F","#FCE190","#1C343E"]
bar = ["#FE4365","#FC9D9A","#F9CDAD","#C8C8A9","#83AF9B"]
neo = ["#5F6D92","#0F3B56","#010005","#CEC5A4","#8199BF"]


def arcos (fila, col,randium):
    color= random.choice(neo)
    if randium ==0:
        lienzo.create_arc(-25+fila,0+col,25+fila,50+col,outline= color,fill =color, style="pieslice", extent = 90, start =0)
    elif randium ==1:
        lienzo.create_arc(0+fila,0+col,50+fila,50+col,outline= color,fill =color, style="pieslice", extent = 90, start =90)
    if randium==2:
        lienzo.create_arc(0+fila,-25+col,50+fila,25+col,outline= color,fill =color, style="pieslice", extent = 90, start =180)
    if randium==3:
        lienzo.create_arc(-25+fila,-25+col,25+fila,25+col,outline= color,fill =color, style="pieslice", extent = 90, start =270)


for fila in range(0,largo,27):
    for col in range(0,ancho,27):
        randiumex = random.randrange(0,4)
        arcos(fila,col,randiumex)
        #print (col)


mainloop()
'''
Este ejercicio es una muestra de un arreglo bidimensional.
posiblemente la parte mas dificil fue encontrar el valor 27
en el incremento de distancia en los rangos de fila y col
porque 27 es 2 puntos mas grande que la figura es que se ve una
separacion pequeña entre una figura y la siguiente.
'''
