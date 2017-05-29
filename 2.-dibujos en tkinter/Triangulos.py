'''
Created on 15/08/2014

@author: A01221672
'''
from Tkinter import*

ventana = Tk()
lienzo =Canvas(ventana, width=400, height=400)
lienzo.pack()
''''Triangulo isosceles'''
lienzo.create_line(101, 100, 1, 100, fill= "black")
lienzo.create_line(101, 101, 51, 1, fill= "black")
lienzo.create_line(1, 101, 51, 1, fill= "black")
''''Triangulo equilatero'''
lienzo.create_line(150, 100, 250, 100, fill= "black")
lienzo.create_line(150, 100, 200, 186, fill= "black")
lienzo.create_line(250, 100, 200, 186, fill= "black")

mainloop()