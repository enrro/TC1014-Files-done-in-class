'''
Created on 22/08/2014

@author: A01221672
'''
from Tkinter import*

ventana = Tk()
lienzo =Canvas(ventana, width=310, height=310)
lienzo.pack()


lienzo.create_rectangle(1,35,310,310, fill = "#f5ead7", width = 0)
lienzo.create_rectangle(30,45,270,300, fill = "#f4d87b", width = 0)
lienzo.create_rectangle(60,100,240,280, fill = "#646464", width = 0)
lienzo.create_rectangle(80,135,220,265, fill = "#269199", width = 0)
lienzo.create_rectangle(100,165,200,255, fill = "#f5f1ea", width = 0)

mainloop()