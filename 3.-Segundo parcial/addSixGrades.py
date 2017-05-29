'''
Created on 04/10/2014
Create a function to ask the user for six grades that returns the sum
@author: A01221672
'''
def sixGrades():
    y = 0
    for x in range(6):
        i = int(input('Please enter a number: '))
        y = y+i
    return y

print(sixGrades())
