'''
Created on 05/11/2014
exercise4
Proven and tested on python 3.3.3
@author: A01221672
'''

foo = [1,2,3,4,5]

def middle(i):
    i.pop(0)
    i.pop(-1)
    return i


print(middle(foo))