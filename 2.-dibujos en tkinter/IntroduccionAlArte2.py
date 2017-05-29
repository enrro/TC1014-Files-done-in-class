'''
Created on 26/08/2014
El gran rectangulo gris
@author: A01221672
'''
from Tkinter import*

ventana = Tk()
lienzo =Canvas(ventana, width=310, height=310)
lienzo.pack()


lienzo.create_rectangle(0,0,310,177, fill = "#e3d7cc", width = 0) #color exterior
lienzo.create_rectangle(32,28,270,156, fill = "#ceccc8", width = 0) #color gris interior
lienzo.create_rectangle(50,38,252,144, fill = "#8d8b8c", width = 0) # color gris oscuro
lienzo.create_rectangle(50,65,252,120, fill = "#e7d9cb", width = 0) #color amarillo palido
lienzo.create_polygon(65,65,50,65,50,59, fill = "#e7d9cb", width = 0) # triangulo arriba a la esquirda
lienzo.create_polygon(172,65,101,46,66,65, fill = "#e7d9cb", width = 0) # triangulo arriba a la esquirda
lienzo.create_polygon(172,65,204,46,252,65, fill = "#e7d9cb", width = 0)# triangulo arriba a la derecho
lienzo.create_polygon(252,119,252,124,240,120, fill = "#e7d9cb", width = 0)# triangulo abajo a la derecho
lienzo.create_polygon(240,119,136,119,205,137, fill = "#e7d9cb", width = 0)# triangulo abajo a la derecho
lienzo.create_polygon(50,119,102,137,136,119, fill = "#e7d9cb", width = 0)# triangulo abajo a la izquierda

mainloop()