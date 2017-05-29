'''
Created on 15/08/2014

@author: A01221672
'''
from Tkinter import*

ventana = Tk()
lienzo =Canvas(ventana, width=400, height=400)
lienzo.pack()


#lienzo.create_arc(10,10,40,30,style = "arc")
for x in range(50):
    lienzo.create_line(20,x,40,49)

mainloop()