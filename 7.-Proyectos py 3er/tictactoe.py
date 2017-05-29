'''
Created on 14/12/2014
TIC TAC TOE
Proven and tested on python 3.3.3
@author: A01221672
'''
#**************************functions*********************
def draw():
    for x in board:
        print(x)
def machinePosition():
     x = random.randrange(0,3)
     y = random.randrange(0,3)
     while not board[x][y] == "e":
        x = random.randrange(0,3)
        y = random.randrange(0,3)
     board[x][y] = machine
#********************libraries**********************************
import random
#*****************variables*********************************
board = [["e","e","e"],["e","e","e"],["e","e","e"]]
winCon = []
defCon = []
user = ''
machine = ''
macCoun = 0
win = False
winM = False
turn = 0
#**************Initialise************************************
print("__________________ _______   _________ _______  _______   _________ _______  _______ ")
print("\__   __/\__   __/(  ____ \  \__   __/(  ___  )(  ____ \  \__   __/(  ___  )(  ____ \\")
print("   ) (      ) (   | (    \/     ) (   | (   ) || (    \/     ) (   | (   ) || (    \/")
print("   | |      | |   | |           | |   | (___) || |           | |   | |   | || (__    ")
print("   | |      | |   | |           | |   |  ___  || |           | |   | |   | ||  __)   ")
print("   | |      | |   | |           | |   | (   ) || |           | |   | |   | || (      ")
print("   | |   ___) (___| (____/\     | |   | )   ( || (____/\     | |   | (___) || (____/\\")
print("   )_(   \_______/(_______/     )_(   |/     \|(_______/     )_(   (_______)(_______/")
print()
print("Welcome to Tic tac toe the game")
print(draw())
#Choosing a user input
user = input("Choose your input method: 'x' or 'o': ")
while user not in ('x','o'):
    print("Invalid choice")
    user = input("Choose your input method: 'x' or 'o': ")
if user == 'x':
    print("The x is yours")
    machine = 'o'
    winCon = [["x","x","x"]]
    defCon = [["o","o","o"]]
if user == 'o':
    print("the o is yours")
    machine = 'x'
    winCon = [["o","o","o"]]
    defCon = [["x","x","x"]]


#********THE ACTUAL GAME *************************************
while win == False and winM == False: #Big mistake I did the first thousand of times was using a "or" instead or "and"
    #Data validation
    re1 = int(input("height input: "))
    while re1 not in (0,1,2):
        print("Invalid choice")
        re1 = int(input("height input: "))
    re2 = int(input("width input: "))
    while re2 not in (0,1,2):
        print("Invalid choice")
        re2 = int(input("height input: "))
    if board[re1][re2] != machine:
        board[re1][re2] = user
        turn = turn + 1

    piv = len (board)
    if [board[i][i] for i in range(piv)]  == winCon[0]: # Diagonal from top left to botom right
        win = True
    elif [board[len(board[0])-1-i][i] for i in range(len(board[0])-1,-1,-1)] == winCon[0]: #The other diagonal
        win = True
    elif [row[0] for row in board] == winCon[0]: #Victoria vertical 0
        win = True
    elif [row[1] for row in board] == winCon[0]: #Victoria vertical 1
        win = True
    elif [row[2] for row in board] == winCon[0]: #Victoria vertical 2
        win = True
    elif win == False: #print ("Victoria horizontal")
        for x in board:
            if x == winCon[0]:
                win = True
    #***************MACHINE ACTIVITIES ****************************
    #*******************defensive moveset**************************
    #Rows
    for j in board:
        if j[0] == user and j[1] == user and j[2] == 'e':
            j[2] = machine
            macCoun += 1
        elif j[0] == user and j[1] == 'e' and j[2] == user:
            j[1] = machine
            macCoun += 1
        elif j[0] == 'e' and j[1] == user and j[2] == user:
            j[0] = machine
            macCoun += 1
    #Columns
    for q in range(0,3):
        if board[0][q] == user and board[1][q] == user and board[2][q] == 'e':
            board[2][q] = machine
            macCoun += 1
        elif board[0][q] == user and board[1][q] == 'e' and board[2][q] == user:
            board[1][q] = machine
            macCoun += 1
        elif board[0][q] == 'e' and board[1][q] == user and board[2][q] == user:
            board[0][q] = machine
            macCoun += 1
    #Diagonal from top left to bottom right
    if board[0][0] == user and board[1][1] == user and board[2][2] == 'e':
        board[2][2] = machine
        macCoun += 1
    elif board[0][0] == user and board[1][1] == 'e' and board[2][2] == user:
        board[1][1] = machine
        macCoun += 1
    elif board[0][0] == 'e' and board[1][1] == user and board[2][2] == user:
        board[0][0] = machine
        macCoun += 1
    #Diagonal from bottom left to top right
    if board[0][2] == user and board[1][1] == user and board[2][0] == 'e':
        board[2][0] = machine
        macCoun += 1
    elif board[0][2] == user and board[1][1] == 'e' and board[2][0] == user:
        board[1][1] = machine
        macCoun += 1
    elif board[0][2] == 'e' and board[1][1] == user and board[2][0] == user:
        board[0][2] = machine
        macCoun += 1
    #******************Ofenssive moveset*******************************
    if macCoun == 0:
        #Rows
        for j in board:
            if j[0] == machine and j[1] == machine and j[2] == 'e':
                j[2] = machine
                macCoun += 1
            elif j[0] == machine and j[1] == 'e' and j[2] == machine:
                j[1] = machine
                macCoun += 1
            elif j[0] == 'e' and j[1] == machine and j[2] == machine:
                j[0] = machine
                macCoun += 1
        #Columns
        for q in range(0,3):
            if board[0][q] == machine and board[1][q] == machine and board[2][q] == 'e':
                board[2][q] = machine
                macCoun += 1
            elif board[0][q] == machine and board[1][q] == 'e' and board[2][q] == machine:
                board[1][q] = machine
                macCoun += 1
            elif board[0][q] == 'e' and board[1][q] == machine and board[2][q] == machine:
                board[0][q] = machine
                macCoun += 1
        #Diagonal from top left to bottom right
        if board[0][0] == machine and board[1][1] == machine and board[2][2] == 'e':
            board[2][2] = machine
            macCoun += 1
        elif board[0][0] == machine and board[1][1] == 'e' and board[2][2] == machine:
            board[1][1] = machine
            macCoun += 1
        elif board[0][0] == 'e' and board[1][1] == machine and board[2][2] == machine:
            board[0][0] = machine
            macCoun += 1
        #Diagonal from bottom left to top right
        if board[0][2] == machine and board[1][1] == machine and board[2][0] == 'e':
            board[2][0] = machine
            macCoun += 1
        elif board[0][2] == machine and board[1][1] == 'e' and board[2][0] == machine:
            board[1][1] = machine
            macCoun += 1
        elif board[0][2] == 'e' and board[1][1] == machine and board[2][0] == machine:
            board[0][2] = machine
            macCoun += 1
    #Counters for machine moveset
    if macCoun == 0:
        machinePosition()
    macCoun = 0
    #***** Checking if the machine won *********
    if [board[i][i] for i in range(piv)]  == defCon[0]: # Diagonal from top left to botom right
        winM = True
    elif [board[len(board[0])-1-i][i] for i in range(len(board[0])-1,-1,-1)] == defCon[0]: #The other diagonal
        win = True
    elif [row[0] for row in board] == defCon[0]:
        winM = True
    elif [row[1] for row in board] == defCon[0]:
        winM = True
    elif [row[2] for row in board] == defCon[0]:
        winM = True
    elif winM == False:
        for x in board:
            if x == defCon[0]:
                winM = True

    draw()
if (win == True and user == 'x'):
    print("Congratulations have a smiley :)")

if winM == True:
    print("The machine has won")
print("Game over")