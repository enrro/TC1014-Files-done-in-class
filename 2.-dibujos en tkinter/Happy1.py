'''
Created on 15/08/2014

@author: A01221672
'''
from tkinter import*

ventana = Tk()
lienzo =Canvas(ventana, width=400, height=400)
lienzo.pack()

'''lienzo.create_line(0, 0, 200, 100)
lienzo.create_line(0, 100, 200, 0, fill= "#205031074")
lienzo.create_rectangle(50, 25, 150, 75, fill= "#205031074")
lienzo.create_oval(50,25,150,75, fill= "red")
'''
'''for x in range(50,100):
    lienzo.create_line(1, 75, x, 1, fill= "black")
'''
lienzo.create_rectangle(1,1,300,300, fill = "#b11d4f", width = 0)
lienzo.create_rectangle(60,100,240,280, fill = "#541105", width = 0)
lienzo.create_rectangle(80,135,220,265, fill = "#292b2c", width = 0)

mainloop()
