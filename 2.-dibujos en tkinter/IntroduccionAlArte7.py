'''
Created on 27/08/2014
Autorrretrato
@author: A01221672
'''
from tkinter import*

ancho=400
alto=400
ventana = Tk()
lienzo =Canvas(ventana, width= ancho, height=alto)
lienzo.pack()

#lienzo.create_rectangle(0,0,ancho,alto, fill = "#B3B3B3", outline = "#B3B3B3", width = 0)
lienzo.create_oval(0,0,ancho,250,outline = "#46F2EF", fill ="#46F2EF")
lienzo.create_polygon(ancho/2-20,0,
                      100,250,
                      300,250,
                      ancho/2+20,0, fil = "#B3B3B3")
lienzo.create_oval(200,200,300,300, fill= "#FCFFAD", outline = "")
lienzo.create_oval(100,200,200,300, fill= "#F72A42", outline = "")

mainloop()
