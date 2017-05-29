'''
Created on 08/11/2014
Hangman
Proven and tested on python 3.3.3
@author: A01221672
'''

#Create a conviniant way to extract columns
def column(i):
    return [row[i] for row in board]

import random

board = [["e","e","e"],["e","e","e"],["e","e","e"]]
con1 = 0
print("Tic tac toe")
for row in board:
    print(row)


while True:
    re1 = int(input("row input: "))
    re2 = int(input("column input: "))

    if board[re1][re2] != "o":
        board[re1][re2] = "x"

    #identify rows
    for row in board:
        #conditionening rows non losing
        if (row[0] == "e" and row[1]== "x" and row[2] == "x") or (row [2] == "e" and row[1]== "x" and row[0] == "x") or ((row[2]== "x" and row[1] == "o" and row[0] == "x")):
            for col in range(len(row)):
                #identify columns as part of rows identify empty space to avoid losing
                if row[col] == "e":
                    row[col] = "o"
                    con1 = con1 + 1
        #elif column(len(row)-1)[0] == "x" and column(1)[1] == "x":
            #print("hello world"*20)
    if con1 == 0:
        for k in range(len(board)):
            #conditionening columns non losing
            if (board[0][k] == "x" and board[1][k] == "x" and board[2][k] == "e") or (board[0][k] == "x" and board[1][k] == "e" and board[2][k] == "x") or (board[0][k] == "e" and board[1][k] == "x" and board[2][k] == "x"):
                for r in range(3):
                    if board[r][k] == "e":
                        board[r][k] = "o"
                        con1 = con1 + 1
    if con1 == 0:
        #conditionening diagonals non losing
        if board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "e":
            board[2][2] = "o"
            con1 = con1 + 1
        elif board[0][0] == "x" and board[1][1] == "e" and board[2][2] == "x":
            board[1][1] = "o"
            con1 = con1 + 1
        elif board[0][0] == "e" and board[1][1] == "x" and board[2][2] == "x":
            board[0][0] = "o"
            con1 = con1 + 1

    if con1 == 0:
        if board[2][0] == "x" and board[1][1] == "x" and board[0][2] == "e":
            board[0][2] = "o"
            con1 = con1 + 1
        elif board[2][0] == "x" and board[1][1] == "e" and board[0][2] == "x":
            board[1][1] = "o"
            con1 = con1 + 1
        elif board[2][0] == "e" and board[1][1] == "x" and board[0][2] == "x":
            board[2][0] = "o"
            con1 = con1 + 1


    print(con1)

    con1 = 0
    for row in board:
        print(row)