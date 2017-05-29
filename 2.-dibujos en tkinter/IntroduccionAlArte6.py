'''
Created on 27/08/2014
Copa de vino, guitarra y musico
@author: A01221672
'''
from Tkinter import*

ancho=284
alto=320
ventana = Tk()
lienzo =Canvas(ventana, width= ancho, height=alto)
lienzo.pack()


lienzo.create_rectangle(0,0,ancho,alto, fill ="#faf2e9", width=0)
lienzo.create_rectangle(3,3,ancho,alto, fill="#79b2e8", width=0)
lienzo.create_rectangle(21,79,260,279,width= 3, outline ="#3b4876")
lienzo.create_polygon(23,61,
                      26,271,
                      254,274,
                      261,71,
                      198,65,
                      195,171,
                      219,171,
                      215,284,
                      155,288,
                      153,48,
                      108,51,
                      107,253,
                      139,255,
                      138,168,
                      166,168,
                      168,62,
                      41,49,
                      39,291,
                      86,288,
                      91,168,
                      64,164,
                      65,56,
                      width= 2, outline = "white", fill = "")

mainloop()