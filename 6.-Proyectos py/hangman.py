'''
Created on 23/10/2014
hangman
Proven and tested on python 3.3.3
@author: A01221672
'''


import random
lives = 7
words = ["alpaca", "turin", "Arma", "portal"]
genWo = random.choice(words)
win = False
print("You have " + str(lives) + " to solve the hangman. Have fun")
print("The word is "+ str(len(genWo)) + " long")


while lives !=0 or win != False:
    g1 = input(str(lives)+ " left")
    for i in range(genWo):

    lives = lives -1
