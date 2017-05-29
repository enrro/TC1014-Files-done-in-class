'''
Created on 23/10/2014
Comprobación de la existencia de un triangulo
Proven and tested on python 3.3.3
@author: A01221672
'''

def is_triangle(a,b,c):
    if (a+b)<c or (b+c)<a or(a+c)<b:
        print ("no")

    else:
        print ("yes")

def triangle():
    x=float(input("Input the first side of the triangle"))
    y=float(input("Input the second side of the triangle"))
    z=float(input("Input the third side of the triangle"))
    is_triangle(x,y,z)

triangle()