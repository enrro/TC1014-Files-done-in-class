'''
Created on 29/08/2014
Obtener informacion de usuarion
@author: A01221672
'''

def ask_Username():
    print("Hi, how are you?. Tell me your name.")
    name = raw_input()
    print("nice to meet you " + name + " :D" )
def ask_Userage():
    print("Hello how old are you?")
    age= input()
    print("What month were you born in numbers")
    month = input()
    print( 12*(age)+month)

ask_Userage()