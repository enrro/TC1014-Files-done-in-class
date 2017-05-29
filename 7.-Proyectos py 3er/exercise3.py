'''
Created on 05/11/2014
exercise3
Proven and tested on python 3.3.3
@author: A01221672
'''

foo = [1,2,3,4,5]
bar = []
x = 0
for i in range(len(foo)):
    x = foo[i] + x
    bar.append(x)
print(bar)