'''
Created on 05/11/2014
Trivia con 10 preguntas y 3 respuestas para cada pregunta
Proven and tested on python 3.3.3
@author: A01221672
'''
def answearsAtRandom(qu2):
    re2 = []
    for r in range(1,20,2):
        re2.append(r)
    piv0 = qu2+1
    re2.remove(piv0)
    piv1 = random.choice(re2)
    re2.remove(piv1)
    piv2 = random.choice(re2)
    re2.remove(piv2)
    pivA = [piv0,piv1,piv2]
    Art1 =random.sample(pivA,3)
    for co1 in range(len(Art1)):
        print(foo[Art1[co1]])
    return piv0
import random


foo = ["How many pairs of ribs would the normal human have?","12","Who wrote the classic novel Les Miserables??","Victor Hugo","What was the name of Sherlock Holmes Housekeeper?","Mrs Hudson","Which actress played the part of Sybil Fawlty in Television?s Fawlty Towers?","Prunella Scale","What was the title of Beethoven?s only opera?","Fidelio","Which river flows through the city of Dublin?","Liffey","Who appeared with David McCallum in the title role of the TV series ?Sapphire and Steel??","Joanna Lumley","Which Irishman won the Tour de France in 1987?","Stephen Roche","In which European country is Cro-Magnon, famous for the discovery of four Palaeolithic skeletons in 1868?","France","Which town is the administrative centre for the Open University? ","Milton Keynes"]
qu1 = []
h0  = []
re1 = []
h3  = 0

for j in range(0,20,2):
    qu1.append(j)

for x in range(0,20,2):
    h0.append(x)

for q in range(1,20,2):
    re1.append(q)


for question in qu1:
    h1 = random.choice((h0))
    print(foo[h1])
    answearsAtRandom(h1)
    h0.remove(h1)
    h2 = input()
    if h2 == foo[h1+1]:
        h3 = h3 + 10
    print("")

print("Your total score is " + str(h3) + " points")
if h3 > 90:
    print ("You are the best")
elif h3 >50:
    print("You did a good job")
else:
    print("Congratulations")