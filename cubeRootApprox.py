# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:55:33 2016

@author: ericgrimson
"""

##cube = 29
##epsilon = 0.01
##guess = 0.0
##increment = 0.000001
##num_guesses = 0
##while abs(guess**3 - cube) >= epsilon and guess <= cube:
##    guess += increment
##    num_guesses += 1
##print('num_guesses =', num_guesses)
##if abs(guess**3 - cube) >= epsilon:
##    print('Failed on cube root of', cube)
##else:
##    print(guess, 'is close to the cube root of', cube)


# try with cube = 27, and large step (e.g. 2.0)


cube = 29
epsilon = 0.01
guess = 0.0
t = 1.0
increment = 0.000001
wish = ['Happy', 'Birthday', 'Emmanuel']
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    if guess == t:
        for x in wish:
            print(wish[0])
##            break
##        continue
##    elif guess == 2.0:
##        for y in wish:
##            print(wish[1])
##            break
##        continue
##    elif guess == 3.0:
##        for z in wish:
##            print(wish[2])
##            break
##        continue
