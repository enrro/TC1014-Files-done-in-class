'''
Created on 23/10/2014
Teorema de Fermat
Proven and tested on python 3.3.3
@author: A01221672
'''

def check_fermat(a,b,c,n):
    sumatoria = ((a**n)+(b**c))
    print(sumatoria)
    if n > 2 and sumatoria == c**2:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No that doesn’t work")

check_fermat(2,2,2,2)