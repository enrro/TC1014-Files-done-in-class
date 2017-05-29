from tkinter import *
import random

ventana=Tk()
lienzo=Canvas(ventana,width=600,height=600)
lienzo.pack()
x=0
y=0
for j in range(10):
    varx1=random.randint(40,60)
    vary1=random.randint(35,70)
    varx=random.randint(40,60)
    vary=random.randint(35,70)
    
    for i in range(1, 40):
        lienzo.create_line(x, y, x+varx, y+vary, width=5)
        lienzo.create_line(x+varx, y+vary, x+varx+varx1, y, width=5)
        print(y+vary,end ="\t")
        y=y+20+i
    x=varx+varx1+x
    y=0
    print("y"+str(y))
    

mainloop()
