# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""





##
##def rtp(a, b):
##    if b == 0:
##        return (1)
##    else:
##        x = a
##        for i in range(1, b):
##            x *= a
##        return x

for i in range(1,11):
    print(i)
    if i == 5:
        break



























#def int2words(num):
#    """Given an int32 number, print it in English.
#
#    Parameters
#    ----------
#    num : int
#
#    Returns
#    -------
#    words : str
#    """
#    assert (0 <= num)
#    d = {
#        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
#        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
#        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
#        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
#        19: 'nineteen', 20: 'twenty',
#        30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
#        70: 'seventy', 80: 'eighty', 90: 'ninety'
#    }
#    h = [100, 'hundred', 'hundred and']
#    k = [h[0] * 10, 'thousand', 'thousand,']
#    m = [k[0] * 1000, 'million', 'million,']
#    b = [m[0] * 1000, 'billion', 'billion,']
#    t = [b[0] * 1000, 'trillion', 'trillion,']
#    if num < 20:
#        return d[num]
#    if num < 100:
#        div_, mod_ = divmod(num, 10)
#        return d[num] if mod_ == 0 else d[div_ * 10] + '-' + d[mod_]
#    else:
#        if num < k[0]:
#            divisor, word1, word2 = h
#        elif num < m[0]:
#            divisor, word1, word2 = k
#        elif num < b[0]:
#            divisor, word1, word2 = m
#        elif num < t[0]:
#            divisor, word1, word2 = b
#        else:
#            divisor, word1, word2 = t
#        div_, mod_ = divmod(num, divisor)
#        if mod_ == 0:
#            return '{} {}'.format(int2words(div_), word1)
#        else:
#            return '{} {} {}'.format(int2words(div_), word2, int2words(mod_))
#
#print(int2words(1009474300345))

#RECURSION AND DYNAMIC PROGRAMMING
#def rtp(a, b):
#    if b == 0:
#        return (1)
#    else:
#        x = a
#        for i in range(1, b):
#            x *= a
#        return x
#
##print(rtp(7, 0))
#
#def rtp_recur(a, b):
#    if b == 0:
#        return (1)
#    else:
#        return a * rtp_recur(a, b-1)
#    
#print(rtp_recur(2, 1))
#RECURSION AND DYNAMIC PROGRAMMING


#c = int(input('please enter number of test cases: '))
#for i in range(c):
#    d = str(input('please input test cases in lower cases: '))


bag = [[1, 2, 3, 4, 5],
       [2, 3, 4, 5, 1],
       [3, 4, 5, 1, 2],
       [4, 5, 1, 2, 3],
       [5, 1, 2, 3, 4]]
a = 0
c = []
for i in bag:
    b = i[a]
    c.append(b)
    a += 1
d = sum(c)
print(d)

#z = int(input('Enter the size of list: '))
#def can(a):
#    x = 0
#    for i in a:
#        x += 1
#    return(x)
#jkx = (input('Enter the list numbers seperated by space: ')).strip().split()
#d = can(jkx)
#
#
#
#print(d)
