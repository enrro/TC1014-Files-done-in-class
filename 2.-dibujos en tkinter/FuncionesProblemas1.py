'''
Created on 03/09/2014
Resolucion de problemas introduccion a las funciones.
@author: A01221672
'''
def ask_peso():
    mercurio = 3.70
    venus =8.87
    Tierra = 9.8
    Marte = 3.71
    Jupiter = 23.12
    Saturno = 8.69
    Urano = 8.69
    Neptuno = 11
    Pluton = .81
    print("hola cual es tu peso en kg \n ")
    x = input()
    print("Tu peso en mercurio es \n " + str(x*mercurio),
          "Tu peso en venues es " +str(x*venus),
          "Tu peos en la tierra es de " + str(x*Tierra),
          "Tu peso en marte es de " + str(x*Marte),
          "Tu peso en Jupiter de " + str(x*Jupiter),
          "Tu peso en Saturno es de " + str(x*Saturno),
          "Tu peso en Urano es de " + str(x * Urano),
          "Tu peso en Neptuno es de " + str(x * Neptuno),
          "Tu peso en Pluto es de " + str(x * Pluton))
    
    
ask_peso()
'''
2. haz un programa que le pregunte al usuario su peso y pueda calcular su masa en los siguientes planetas (considera la gravedad de cada planeta):

Mercurio: 3,70 m/ s2
Venus: 8,87 m/ s2
Tierra: 9,80 m/ s2
Marte: 3,71 m/ s2
Jupiter: 23,12 m/ s2
Saturno: 8,96 m/ s2
Urano: 8,69 m/ s2
Neptuno: 11 m/ s2
Pluton: 0,81 m/ s2
'''