'''
Created on 23/10/2014
circulos que se mueven
Proven and tested on python 3.3.3
@author: A01221672
'''

from tkinter import*
direction =1
x=1
ancho=400
alto=375
ventana = Tk()
lienzo =Canvas(ventana, width= ancho, height=alto)
lienzo.pack()

while True:
    lienzo.delete('all')
    lienzo.create_oval(x+10,40,x+100,100,fill = 'blue')
    if (x>300 or x <0):
        direction =direction*(-1)
    x+=10*direction
    lienzo.after(200)
    lienzo.update()


mainloop()