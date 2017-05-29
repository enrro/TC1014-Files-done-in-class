'''
Created on 22/08/2014
El gran cuadrado violeta
@author: A01221672
'''
from Tkinter import*

ventana = Tk()
lienzo =Canvas(ventana, width=400, height=400)
lienzo.pack()

lienzo.create_rectangle(1,1,300,300, fill = "#b11d4f", width = 0)
lienzo.create_rectangle(60,100,240,280, fill = "#541105", width = 0)
lienzo.create_rectangle(80,135,220,265, fill = "#292b2c", width = 0)

mainloop()