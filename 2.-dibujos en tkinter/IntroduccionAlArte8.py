'''
Created on 27/08/2014
circulos y cuadrados colores varios
@author: A01221672
'''
from tkinter import*

ancho=325
alto=161
ventana = Tk()
lienzo =Canvas(ventana, width= ancho, height=alto)
lienzo.pack()


lienzo.create_arc(162,67,239,5,style="pieslice", start=0,extent=90, width=5, outline="#254042")
lienzo.create_arc(162+8,67-8,239-4,5+4,style="arc", start=0,extent=90, width=5, outline="#4a5960")
lienzo.create_arc(162+12,67-12,239-8,5+8,style="arc", start=0,extent=90, width=5, outline="#c83f21")
lienzo.create_arc(162+16,67-16,239-12,5+12,style="arc", start=0,extent=90, width=5, outline="#ac8e5d")
lienzo.create_arc(162+20,67-20,239-16,5+16,style="arc", start=0,extent=90, width=5, outline="#2a417b")
lienzo.create_arc(162+24,67-25,239-21,5+21,style="arc", start=0,extent=90, width=5, outline="#94653d")
lienzo.create_arc(162+28,67-30,239-26,5+25,style="arc", start=0,extent=90, width=5, outline="#58894a")
lienzo.create_arc(162+30,67-31,239-28,5+26,style="arc", start=0,extent=90, width=4, outline="#b70f15")
lienzo.create_rectangle(195,38,162,5, width= 5, outline = "#d27e10", fill = "")
lienzo.create_arc(204,38,185,34,style="arc", start=90,extent=90, width=4, outline="#4a7c9c")


mainloop()
