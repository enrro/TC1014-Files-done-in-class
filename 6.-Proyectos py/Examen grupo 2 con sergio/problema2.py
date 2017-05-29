'''
Created on 25/10/2014
preguntas y respuestas de adicion y substraccion
Proven and tested on python 3.3.3
@author: A01221672
'''
import random
cac = 0
for x in range(10):
    rn1 = random.randrange(1,101)
    rn2 = random.randrange(1,101)
    rn3 = random.randrange(2)
    print(rn1,rn2)
    if rn3 == 0:
        addition =input("Add "+ str(rn1) + " to " + str(rn2))
        if addition == str(rn1+rn2):
            print("Correct")
            print(cac)
            cac = cac+10
        else:
            print("Incorrect")
    else:
        substraction = input("substract " + str(rn2) + " to " +  str(rn1))
        if substraction == str(rn1-rn2):
            cac = cac+10
            print("Correct")
            print(cac)
        else:
            print("Incorrect")

print(cac)