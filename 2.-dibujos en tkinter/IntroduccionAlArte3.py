'''
Created on 26/08/2014
El gran rectangulo con colores calidos rosa, violeta, marron
@author: A01221672
'''
from Tkinter import*

ancho=658
alto=449
ventana = Tk()
lienzo =Canvas(ventana, width= ancho, height=alto)
lienzo.pack()

#dc9a91
lienzo.create_rectangle(0,0,ancho,alto, fill = "#ecd5b6", width = 0) #color palido rosa de fondo
lienzo.create_rectangle(9,9,ancho-9,alto-9, fill = "#c5576c", width = 0) #color rosa mas oscuro segunda capa de fondo
lienzo.create_rectangle(32,107,ancho-32,alto-107, fill = "#96050c", width = 0) #color rojo parte media
lienzo.create_rectangle(9,58,ancho-9,140, fill = "#9d5d11", width = 0) #color marron parte superior
lienzo.create_rectangle(32,108,ancho-32,140, fill = "#77240a", width = 0) #color sobrepuesto marronish
lienzo.create_polygon(ancho-572,alto-107, #punto inferior izquierdo
                      ancho -82,alto-107, #punto inferior derecho
                      ancho -82,alto-291, #punto superior derecho
                      ancho-211,alto-291, #punto superior derecho-izquierdo
                      ancho-211,alto-135, #punto inferior de la columna derecha, lado izquierdo
                      ancho-466,alto-135, #punto inferior de la columna izquierdo, lado derecho
                      ancho-466,alto-291,
                      ancho-572,alto-291,
                      fill="#792206") #poligono irregular central figura marron
lienzo.create_rectangle(ancho-187,alto-135,ancho-159,alto-251, fill ="#d26179", width = 0)
lienzo.create_rectangle(170,alto-135,143,alto-251, fill ="#d26179", width = 0) #rectangulo rosado central derecho
lienzo.create_rectangle(170,alto-135,143,alto-251, fill ="#d26179", width = 0) #rectangulo rosado central izquierdo
lienzo.create_rectangle(ancho-572,alto-107,ancho -82,alto-9,fill= "#93540f", width=0)

mainloop()