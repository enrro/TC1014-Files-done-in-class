'''
Created on 03/12/2014
example of final test
Proven and tested on python 2.7
@author: A01221672
'''
#Crea un método en Python que reciba tres argumentos  y que regrese verdadero (booleano true) si terminen con la misma letra. (Ejemplo casa, osa, pera). En caso contrario regresará falso (booleano false).
def threeOfTheSame(foo0,foo1,foo2):
    if foo0[-1]==foo1[-1]==foo2[-1]:
        print("The three words finish with the same letter.")
    else:
        print("False")



'''
SEGUNDA PARTE

PROBLEMA I ROWLING
Realiza un programa en Python que haga lo siguiente:

Tendrás un String palabra que contendrá lo siguiente: “expectopatronumexpelliarmuslumusmáxima”.

Le pedirás al usuario que te escriba un String con dos letras. Por ejemplo el usuario te podrá escribir: “ae”, “si”, “rf”....
Si el usuario escribe un String con una longitud diferente a dos letras le preguntarás de nuevo hasta que te escriba uno con 2 letras exactamente.
Deberás imprimir si el String proporcionado por el usuario se encuentra en “expectopatronumexpelliarmuslumusmáxima”.  Por ejemplo “ex”, “xp”, “on” si están.
Nota: Puedes simplificar el String palabra en el código y poner “expecto…” (Longitud total: 38 letras).
'''

palabra = "expectopatronumexpelliarmuslumusmáxima"

user = input("Enter a string with 2 letters")
while len(user) != 2:
    user = input("Enter a string with 2 letters")
if palabra.find(user) >= 0:
    print("ok")
'''for letter in range(len(palabra)-1):
    if palabra[letter] == user[0] and palabra[letter+1] == user[1]:
        print("La palabra se encuentra")'''