'''
Created on 27/08/2014
Lineas de interseccion roja,azul,amarillo
@author: A01221672
'''
from Tkinter import*

ancho=278
alto=375
ventana = Tk()
lienzo =Canvas(ventana, width= ancho, height=alto)
lienzo.pack()

lienzo.create_rectangle(0,0,ancho,alto, fill ="#826f51", width=0)
lienzo.create_arc(240,358,40,190,start=180,extent=180,fill= "#eeedf2", width=0, style="chord", outline="#eeedf2") #circulo gris
lienzo.create_arc(70,77,205,305,start=270,extent=180,fill= "#1e1e26", width=0, style="chord", outline="#1e1e26") #circulo negro


mainloop()