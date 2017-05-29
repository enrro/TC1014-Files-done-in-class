'''
Created on 06/11/2014
Hangman
Proven and tested on python 3.3.3
@author: A01221672
'''
import random
foo = ["duck","reddit", "dad", "magic", "frog", "sheep", "injured", "undertaker", "potatoe", "king", "north", "princess", "careful", "hammer", "shaman", "gorilla"]
li0 = []
bar = []
hp1 = 7
ho1 = random.choice(foo)
qu1 = ""
ca1 = 0
ca2 = 0

'''
code in case of a list file
with open("words.txt") as file:
    for line in file:
        li0.append(str(line.strip()))
ho2 = random.choice(li0)
'''


#create a list with the amount of elements the word you are looking for has
for x in range(len(ho1)):
    bar.append("_")


print("Welcome to the hangman game. You have 7 lives use them wisely.")
print(bar)
#conditioning for breaking if hp reaches 0 or below
while hp1 > 0:
    qu1 = input("Guess a letter of the word: ")
    #analising if the input data is inside the word
    for i in range(len(ho1)):
        if ho1[i] == qu1:
            bar[i] = qu1
            ca1 = ca1 + 1
    #counter for heal in case the word is not found
    if ca1 == 0:
        hp1 = hp1 - 1
        print("That is not a correct answer.")
        print(str(hp1) + " lives left.")
    print(bar)
    #analising if the list has '_' left for the win condition
    for x in bar:
        if x == "_":
            ca2 = ca2+1
    #win condition achieved
    if ca2  == 0:
        print("Congratulations you have won.")
        break
    ca2 = 0
    ca1 = 0


print("End of the game")