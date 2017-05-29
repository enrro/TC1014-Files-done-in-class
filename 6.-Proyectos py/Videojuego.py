'''
Created on 23/10/2014
Historia interactiva de preguntas y respuestas
Proven and tested on python 3.3.3
@author: A01221672
'''
#! python3
contarPuntos = 0
pregunta0 = pregunta1 = pregunta2 = pregunta3 = pregunta4 = ""
pregunta0 = input("What is the terminal velocity of a unladen swallow.? \nopción a) 2 \nopción b) 3 \nopción 3) African or european?\n")
if pregunta0 == "African or European" or pregunta0 == "african or european":
    contarPuntos = contarPuntos + 50
    print(contarPuntos)
    print("Correct answer. You have " + str(contarPuntos)+ " points")
else:
    print("Wrong answer")



pregunta1 = input("What is this guy power level?\nopción a) 0 \nopción b) not \nmucho c) 9000\n")
if pregunta1 == "9000":
    contarPuntos = contarPuntos +50
    print("Correct answer. You have " + str(contarPuntos)+ " points")
else:
    print("Wrong answer")


pregunta2 = input ("What is the official language in palestine? \nopción a) Spanish \nopción b) Inglish \nopción c) Arabic\n")
if pregunta2 == "Arabic" or pregunta2 == "arabic":
    contarPuntos = contarPuntos +50
    print("Correct answer. You have " + str(contarPuntos)+ " points")
else:
    print("Wrong answer")

pregunta3 = input("What is the name of the yelow rat-like pokemon in the famous cartoon Pokemon? \nopción a) Ivisaur \nopción b) Chuck Norris \nopción c)Pikachu\n")
if pregunta3 == "Pikachu" or pregunta3 == "pikachu":
    contarPuntos = contarPuntos +50
    print("Correct answer. You have " + str(contarPuntos)+ " points")
else:
    print("Wrong answer")

pregunta4 = input("What does the fox says? \nopción a) nobody cares \nopción b) owwwl \nopción c) 42\n")
if pregunta4 == "nobody cares" or pregunta4 == "Nobody cares":
    contarPuntos = contarPuntos +50
    print("Correct answer. You have " + str(contarPuntos)+ " points")
else:
    print("Wrong answer")

print("End of the game you earned " + str(contarPuntos) + " Points")
