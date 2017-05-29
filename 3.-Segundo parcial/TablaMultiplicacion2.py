'''
Created on 04/10/2014
Otra forma de hacer la tabla de multiplicacion
@author: A01221672
'''

def multiplica(n):
    for i in range (1,n+1):
        for e in range (1,n+1):
            print( e *i, end ="\t")
        print()
multiplica(2)
