'''
Created on 04/10/2014
ejercicio de loops preguntar al usuario por 6 calificacion
@author: A01221672
'''
def askGrade(n):
    y = 0
    for x in range(n):
        grade = int(input("Give me one grade"))
        y = y + grade
    return y

def average(suma, elements):
    return float(suma)/float(elements)

def lastFunction():
    r = askGrade(6)
    return average(r,6)

print(lastFunction())
