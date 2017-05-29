'''
Created on 04/10/2014
Rotacion de una figura alrededor de un circulo
@author: A01221672
'''

from tkinter import *
import math


def animateCircle(cx,cy,r):
    ventana = Tk()
    lienzo =Canvas(ventana, width= 400, height=300, bg = "#83AF9B")
    lienzo.pack()
    angle = 0
    x = math.cos(angle)
    y = math.sin(angle)

    while True:
        lienzo.delete('all') #limpia el circulo anterior
        lienzo.create_oval(cx-r,cy+r,
                           cx+r,cy-r,
                           fill ="#FC9D9A",
                           outline ="#FC9D9A")
        lienzo.create_oval ((cx+5)+((r+10)*x),(cy+5)+((r+10)*y),
                            (cx-5)+((r+10)*x),(cy-5)+((r+10)*y),
                            fill = "#FE4365",
                           outline ="#FE4365")
        lienzo.update() 
        lienzo.after(80) 
        angle += .2
        x = math.cos(angle)
        y = math.sin(angle)
        

animateCircle(200,150,50)

'''
La parte mas interesante de este ejercicio fue descubrir la formula para la
rotacion. Si tenemos que un ecuacion parametrica para un circulo es igual a
radio * cos(angulo) entonces podemos determinar la trallectoria del ciruculo
exterior. las siguientes son algunas de las bases que me llevaron a inferior
la formula de arriba.
1)hacer un pequeño circulo (cx+5),(cy+5),(cx-5),(cy-5)
2) identificar que el circulo va a tener un desplazamiento con respecto a el
circulo interior "+(r*x)" "+(r*y)"
3)hacer una distancia entre el circulo interior y el exterior "(r+10)*x)"
4) la razon por la que se mueve al rededor del circulo es porque el cos y sin
en este caso x y se desplazan de manera muy pequeña en movimientos ondulados
al combinar estos movimientos ondulados se crea una circunferencia. pero esa
circunferencia es muy pequeña para ser apreciada. al multiplicar la circunfer
encia por el radio puedes alcanzar el redio total del circulo. pero si no le
sumas nada entonces estas en la orilla del circulo y no en la parte exterior
de este. es por eso que le sumo 10 unidades para que puedas desplazarte por
fuera del circulo.

'''
