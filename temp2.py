# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 06:23:16 2019

@author: Oni Remi John
"""
#REVERSE STATEMENTS-----------------------------------
#def rev(f):
#    b = f.split()
#    a = b[::-1]
#    return ' '.join(a)
#
#x = str(input('Enter a statement: '))
#print(rev(x))
#REVERSE STATEMENTS-----------------------------------


##DATASETS TESTS-----------------------------------
foo = ['good', 'bad', 'bad', 'nil', 'good', 'bad']
blee = dict()
cos = []
v = 0
for i in foo:
    if i not in blee:
        blee.update({i: v})
        v += 1
for i in foo:
     cos.append(blee[i])

print(cos)
#DATASETS TESTS----------------------------------


#BRICKS CALC.------------------------------------
#n = int(input('How many bricks do you have?: '))
#op = 'Your pyramid is'
#tl = 'cm tall'
#i, d = 1, [1, 2]
#for x in range(1, (n - 1)):
#    d.append(d[i] + d[0])
#    if sum(d) < n:
#        i += 1
#    if sum(d) > n:
#        d.pop()
#print(op + ' ' + str(len(d)) + tl)
#BRICKS CALC.------------------------------------

#x = str(input('Please input p if you need to get the price or input a if you need to  get the amount of unit?: '))
#if x == 'p':
#    y = float(input('How much unit do you need? '))
#    z = (y)*200
#    print('You will need #' + str(z) + ' ' + 'to get' + ' '+ str(y) + ' ' + 'units')
#elif x == 'a':
#    y = float(input('How much do you have? '))
#    z = (y)/200
#    print(str(y) + ' ' + 'can only get you' + ' ' + str(z) + ' ' + 'units')
