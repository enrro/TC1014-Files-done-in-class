'''
Created on 21/10/2014
Circulos dentro de cuadrados monocromaticos
Proven and tested on python 3.3.3
@author: A01221672
'''

from tkinter import *
import random

ventana=Tk()
largo = 400
ancho = 400

lienzo=Canvas(ventana,width=largo,height=ancho)
lienzo.pack()

def JaredTarbell(filas,columnas,randium):
    if randium == 0:
        lienzo.create_rectangle(0+filas,0+columnas,50+filas,50+columnas, outline = "black", fill = "black")
        lienzo.create_oval(5+filas,5+columnas,45+filas,45+columnas, outline ="white", fill = "white")
    if randium == 1:
        lienzo.create_rectangle(0+filas,0+columnas,50+filas,50+columnas, outline = "white", fill = "white")
        lienzo.create_oval(5+filas,5+columnas,45+filas,45+columnas, outline ="black", fill = "black")
    if randium == 2:
        prueba(filas,columnas,randium)


def prueba(filas,columnas,randium):
    for filas in range(filas,filas+50,12):
        for lol in range(columnas,columnas+50,12):
            randium = random.randrange(0,2)
            print("columna "  + str(filas)+ " fila " + str(columnas))
            if randium == 0:
                lienzo.create_rectangle(0+filas,0+lol,50*.25+filas,50*.25+lol, outline = "black", fill = "black")
                lienzo.create_oval(5*.25+filas,5*.25+lol,45*.25+filas,45*.25+lol, outline ="white", fill = "white")
            if randium == 1:
                lienzo.create_rectangle(0+filas,0+lol,50*.25+filas,50*.25+lol, outline = "white", fill = "white")
                lienzo.create_oval(5*.25+filas,5*.25+lol,45*.25+filas,45*.25+lol, outline ="black", fill = "black")




for fil in range(0,largo,50):
    for col in range(0,ancho,50):
        aleatorios = random.randrange(0,3)
        JaredTarbell(fil,col,aleatorios)

mainloop()
