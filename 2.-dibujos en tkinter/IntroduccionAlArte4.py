'''
Created on 27/08/2014
Lineas de interseccion roja,azul,amarillo
@author: A01221672
'''
from Tkinter import*

ancho=543
alto=408
ventana = Tk()
lienzo =Canvas(ventana, width= ancho, height=alto)
lienzo.pack()
'''
Forma alterna para resolver
lienzo.create_line(0,77,ancho,77, width= 5) #linea horizontal superior
lienzo.create_line(0,188,ancho,188, width= 5)#linea horizontal media
lienzo.create_line(0,352,ancho,352, width= 5)#linea horizontal baja
lienzo.create_line(92,0,92,alto, width= 5)#linea vertical izquierda
lienzo.create_line(188,0,188,alto, width= 5)#linea vertical izquierda-derecha
lienzo.create_line(317,0,317,alto, width= 5)#linea vertical derecha-izquierda
lienzo.create_line(484,0,484,alto, width= 5)#linea vertical izquierda
'''
CV=[77,188,352]
CH=[92,188,317,484]
for x in range(3):
    lienzo.create_line(0,CV[x],ancho,CV[x], width= 5) #linea horizontal
for x in range(4):
    lienzo.create_line(CH[x],0,CH[x],alto, width= 5)#linea vertical izquierda

lienzo.create_rectangle(CH[0]+3,CV[0]+3,
                        CH[1]-2,CV[1]-2, fill ="red",width=0)
lienzo.create_rectangle(CH[2]+3,CV[0]+3,
                        CH[3]-2,CV[1]-2, fill ="blue",width=0)
lienzo.create_line(CH[0],300,CH[1],300,width=5)
lienzo.create_rectangle(CH[0]+3,300+3,
                        CH[1]-2,CV[2]-2, fill ="yellow",width=0)
mainloop()