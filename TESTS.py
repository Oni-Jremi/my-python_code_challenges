
##print('Checking')
##def greet(lang):
##    if lang == 'es':
##        return 'Hola'
##    if lang == 'fr':
##        return 'Bonjour'
##    else:
##        return 'Hello'
##
##print(greet('es'), 'John')

##TEMPERATURE CONVERSION
##aa = input("Enter Celsius Temperature: ")
##bb = (float(aa) * 9/5) + 32
##print("Fahrenheit Temperature:", float(bb))
##
##xx = input("Input Score: ")
##yy = 0.9
##cc = 0.8
##vv = 0.7
##bb = [0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]
##
##if xx = float(yy):
##    print("A")
##elif xx = float(cc):
##    print("B")
##elif xx = float(vv):
##    print("C")
##elif xx = float(bb):
##    print("F")

#while True:
#    line = input("> ")
#    if line[0] == '2' :
#        continue
#    if line == 'done' :
#        break
#    print(line)
#print('Done!')
##
##n = int(input())
##if n%2!=0:
##    print('Weird');
##elif n%2==0 and 2<=n<=5:
##    print('Not Weird');
##elif n%2==0 and 6<=n<=20:
##    print('Weird');
##elif n%2==0 and n>20:
##    print('Not Weird');



##n = int(input(""))
##for i in range(1,n+1):
##    print(i, end = "")
##def is_leap(year):
## return year%4==0 and (year%400==0 or year%100!=0)
## 
##
##
##year = int(input())
##--------------------------------------------------------------

##FOR EVEN AND ODD TEST
##odd_even_test = input('Please enter a number: ')
##odd_even_test = int(odd_even_test)
##
##
##if odd_even_test%2 != 0:
##    print('Your number is an odd number')
##    if  odd_even_test == 1 or odd_even_test == 2 or odd_even_test == 3 or odd_even_test == 5 or odd_even_test == 7:
##        print('Your number is a prime number')
##    else:
##        print('Your number is not a prime number')
##elif odd_even_test%2 == 0:
##        print('Your number is an even number')
##        if  odd_even_test == 1 or odd_even_test == 2 or odd_even_test == 3 or odd_even_test == 5 or odd_even_test == 7:
##            print('Your number is a prime number')
##        else:
##            print('Your number is not a prime number')


##num = int(input('Enter a number: '))
##
##if num % 2 == 0:
##    print('number is even')
##else:
##    print('number is odd')
##if num == 1 or num == 2 or num == 3 or num == 5 or num == 7:
##    print('number is prime')
##elif num%2 == 0 or num%3 == 0 or num%5 == 0 or num%7 == 0:
##    print('number is not prime')
##else:
##    print('number is prime')
##----------------------------------------------------------------

##FOR LOWEST COMMON MULTIPLE
##num1 = int(input ('Enter a number betweens 1 and 6: '))
##num2 = int(input ('Enter a number between 1 and 6: '))
##
##if num1 <1 or num1 >6:
##    print('You be goat, you better run the code again and use number between 1-6')
##if num2 <1 or num2 >6:
##    print('Chai! Ewu, go back and do the needful, nonsense')
##
##elif num1 == num2:
##    print(num1 or num2)
##elif num1 >=1 or num1 <= 6:
##    if num1 == 4 and num2 == 6:
##        print('L.C.M = ',(num1*num2)/2)
##    elif num1 == 6 and num2 == 4:
##        print('L.C.M = ',(num1*num2)/2)
##    else:
##        if num1 > num2 and num1%num2 == 0:
##            print(num1)
##        elif num2 > num1 and num2%num1 == 0:
##            print(num2)
##        else:
##            print('L.C.M = ',num1*num2)
##elif num2 >=1 or num2 <= 6:
##    if num1 == 4 and num2 == 6:
##        print('L.C.M = ',(num1*num2)/2)
##    elif num1 == 6 and num2 == 4:
##        print('L.C.M = ',(num1*num2)/2)
##    else:
##        if num1 > num2 and num1%num2 == 0:
##            print(num1)
##        elif num2 > num1 and num2%num1 == 0:
##            print(num2)
##        else:
##            print('L.C.M = ',num1*num2)
##---------------------------------------------------------------

##PRIME AND EVEN NUMBERS
##num = 10
##nom = 11
##
##print('For Even Numbers between 10 and 30')
##while num >= 10 and num <= 30:
##    print(num)
##    num += 2
##print('')   
##print('For Odd Numbers between 10 and 30')
##while nom >= 11 and nom <= 30:
##    print(nom)
##    nom += 2
##print('')
##print('For Prime Numbers between 10 and 30')
##for i in range(10, 30):
##    if i%2 !=0 and i%3 !=0 and i%5 !=0 and i%7 !=0:
##        print(i)
##--------------------------------------------------------------------

##FACTORS
##num = int(input('Enter a number: '))
##for i in range(1, int(50)+1):
##    if num%i == 0:
##        print(i)

##s = 'ariohjsbobbbobobobbobfjeeiioussfe'
##counts = 0
##vowel = 'aeiou'
##tect1 =  'bob'
##counta = 0
##for letter in s:
##    if letter in vowel:
##        counts += 1
##print('Number of vowels: ' + str(counts))
##for x in range(len (s)):
##  if x != len (s) - 2:
##      if s[x : x+3] == 'bob':
##          counta += 1
##print('Possible number of bob is: ' + str(counta))

##for x in range(len (s)):
##    if x in range('a', 'z') is True:
##        print('Longest substring in alphabetical order is: ' + x)
##-------------------------------------------------------------------

##PALINDROME
##a = str(input("Enter a word: "))
##rvs = a[::-1]
##if rvs == a:
##    print('This word is a Palindrome')
##else:
##    print('This word is not a Palindrome')
##-------------------------------------------------------------------

##a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
##s = [i for i in a if i%2 == 0]
##
##print(s)


##s = open('gatta.txt', 'w+')
##s.write('My name is Oni Remi John.\nI am a student at the Yaba College Of Technology.\n')
##s.close()
##


##varA = int(input('Enter lower number: '))
##varB = int(input('Enter higher number: '))
##while (varA <= varB):
##    if int(varA) <= int(varB):
##        varA += 1
##        if  int(varA)%5 == 0:
##            print(varA)
##while (int(varB) <= int(varA)):
##    if (int(varB) == 5):
##        print(varB)
##    if int(varB) <= int(varA):
##        varB += 1
##        if int(varB)%5 == 0:
##            print(varB)


##for i in range(int(varA), int(varB)+1):
##    if i%5 == 0:
##        print(i)


##varA = int(input('Enter a number: '))
##varB = int(input('Enter a number: '))
##if varA < varB:
##    count =  varA
##    while(count < varB):
##        count = count + 5
##        print(count)
##elif varA > varB:
##    count = varA
##    while(count > varB):
##        count = count - 5
##        print(count)
##else:
##    print('Error in input values')











#while True:
#    a = str(input('Player_1: '))
#    b = str(input('Player_2: '))
#    c = 'Here is another try!'
#    d = 'Player_1 Wins'
#    e = 'Player_2 Wins'
#    if a == b:
#        print('No winner')
#        print(c)
#    else:
#        while a == 'rock':
#            if b == 'scissors':
#                print(d)
#                print(c)
#                break
#            elif b == 'paper':
#                print(e)
#                print(c)
#                break
#        while a == 'paper':
#            if b == 'rock':
#                print(d)
#                print(c)
#                break
#            elif b == 'scissors':
#                print(e)
#                print(c)
#                break
#        while a == 'scissors':
#            if b == 'paper':
#                print(d)
#                print(c)
#                break
#            elif b == 'rock':
#                print(e)
#                print(c)
#                break
#    continue




##a = [1, 2, 7, 9, 'hey', 'goat', 6, 16]
##a.append(4)
##a.extend([2, 2])
##print(a)


##THIS IS THE FIRST FUNCTION THAT RETURNS A TUPLE
##OF THE X AND Y COORDINATES OF THE DESIRED ELEMENT
##def tupGUY(a, b):
##    for i in a:
##         for x in i:
##             if x == b:
##                 return[a.index(i),i.index(x)]
##
##
##
##
##def pathList(oyo):
##    c = [ tupGUY(oyo, 'r'),tupGUY(oyo, 'p')]
##    mov1 = []
##    while c[0][1] != c[1][1]:
##        if c[0][1] < c[1][1]:
##            mov1.append('right')
##            c[0][1] +=1
##        elif c[0][1] > c[1][1]:
##            mov1.append('left')
##            c[0][1] -=1
##    while c[0][0] != c[1][0]:
##        if c[0][0] < c[1][0]:
##            mov1.append('down')
##            c[0][0] +=1
##        elif c[0][0] > c[1][0]:
##            mov1.append('up')
##            c[0][0] -=1
##    return(mov1)
##    
##def tip(a):
##    u = []
##    x = []
##    for i in a:
##        p = i[0] + i[1]
##        u.append(p)
##    u.sort()
##    for i in u:
##        for k in a:
##            if k[0] + k[1] == i:
##                if k not in x:
##                    x.append(k)
##    return(x)
##    
##def optMOV(grid):
##    d = [tupGUY(grid, 'r')]
##    u = [tupGUY(grid, 'r')]
##    f = []
##    h = []
##    miv1 = []
##    mov1 = []
##    for i in grid:
##        k = enumerate(i[0:])
##        for y, x in k:
##             if x == 'p':
##                 e = [grid.index(i),y]
##                 f.append(e)
##                 h.append(e)
##    r = tip(h)
##    for i in r:
##        u.append(i)
##    for i in f:
##        d.append(i)
##    for i in range(1, len(d)):
##        while d[0][0] != d[i][0]:
##            if d[0][0] < d[i][0]:
##                    miv1.append('down')
##                    d[0][0] +=1
##            elif d[0][0] > d[i][0]:
##                    miv1.append('up')
##                    d[0][0] -=1   
##        while d[0][1] != d[i][1]:
##            if d[0][1] < d[i][1]:
##                miv1.append('right')
##                d[0][1] +=1
##            elif d[0][1] > d[i][1]:
##                miv1.append('left')
##                d[0][1] -=1
##        miv1.append('CLEAN')
##    for i in range(1, len(u)):
##        while u[0][0] != u[i][0]:
##            if u[0][0] < u[i][0]:
##                    mov1.append('down')
##                    u[0][0] +=1
##            elif u[0][0] > u[i][0]:
##                    mov1.append('up')
##                    u[0][0] -=1   
##        while u[0][1] != u[i][1]:
##            if u[0][1] < u[i][1]:
##                mov1.append('right')
##                u[0][1] +=1
##            elif u[0][1] > u[i][1]:
##                mov1.append('left')
##                u[0][1] -=1             
##        mov1.append('CLEAN')
##    if len(miv1) > len(mov1):
##        return(mov1)
##    else:
##        return(miv1)
##
##bag = [['r', '1', '12', '16', '17'],
##       ['9', '5', '11', 'p', '18'],
##       ['47', 'p', '6', '31', '4'],
##       ['p', '8', '13', '50', '20'],
##       ['16', 'p', '40', '23', '85']]
##print(optMOV(bag))
#
#
#
##bag = [['r', '1', '12', '16', '17'],
##       ['9', '5', '11', '22', '18'],
##       ['47', 'p', '6', '31', '4'],
##       ['p', '8', '13', '50', '20'],
##       ['16', 'p', '40', '23', '29']]
##print(optMOV(bag))

#d = [tupGUY(bag, 'r')]
#f = []
#miv1 = []
#for i in bag:
#    k = enumerate(i[0:])
#    for y, x in k:
#             if x == 'p':
#                 e = [bag.index(i),y]
#                 f.append(e)
#k = tip(f)
#print(k)
#r = tip(f)
#for i in r:
#    d.append(i)

#print(f)
#def amTIRED(a):
#    t = 0
#    c = []
#    a[t] = tip(a[t])
#    for r in a:
#        if tip(r) < tip(a[t]):
#            a[t] = r
#            c.append(a[t])
#            t += 1
#    return(c)
#u = amTIRED(f)
#for i in f:
#    v = tip(i)
#    c.append(v)
#c.sort()
#y = min(c)
#for i in range(max(c)):
#    for q in f:
#        z = tip(q)
        

#for i in range(1, len(d)):
#    while d[0][1] != d[i][1]:
#        if d[0][1] < d[i][1]:
#            miv1.append('right')
#            d[0][1] +=1
#        elif d[0][1] > d[i][1]:
#            miv1.append('left')
#            d[0][1] -=1
#print(d)
#bag =[['1', '2', 'u', 'u', 'u', '6', '9', 'u']]
#d = enumerate(bag[0])
#e = []
#for i, x in d:
#    if x == 'u':
#        e.append(i)
#print(e)        
#c = [1, 2, 3, 4, 5]
#mov = []
#miv = []
#for x in c:
#    if x > 3:
#        mov.append(x)
#    elif x < 3:
#        miv.append(x)
#print(mov)
#print(miv)
##import numpy as np
##d = np.array([0, 2, 0])
##for i in d:
##     u = np.argwhere(x == 0)
##     print(u)
##c = [tupGUY(bag, 'r'), []]
##d = ['p', 'q', 's']
##count = 0
##for i in d:
##     h = tupGUY(bag,i)
##     c[1].append(h)
##     count
##for i in c[1]:
##     for x in i:
##          a = i.index(x)
##          print(a)

##b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
##a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
##c = []
##if len(a) >= len(b):
##    for i in a:
##        if i in b:
##            if i not in c:
##                c.append(i)
##    print(c)
##else:
##    for i in b:
##        if i in a:
##            if i not in c:
##                c.append(i)
##    print(c)



##def prime_check(a = int(input('Enter a number: '))):
##    c = []
##    d = []
##    for i in range(1, a+1):
##        if a%i == 0:
##            c.append(i)
##        else:
##            d.append(i)
##    if len(c) <= 2:
##        return('This is a prime number')
##    else:
##        return('This is not a prime number')
##        
##print(prime_check(13))



##def listENDS(a):
##    b = a.pop()
##    c = a.pop(0)
##    d = list([b, c])
##    d.reverse()
##    return(d)
##e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
##print(listENDS(e))



#FIBONACCI-----------------------------------
#def fibo(a):
#    i = 1
#    d = [1,1]
#    if a == 0:
#        d =[]
#    elif a == 1:
#        d = [1]
#    elif a == 2:
#        d = [1,1]
#    elif a > 2:
#        for x in range(1, (a - 1)):
#            d.append(d[i] + d[i-1])
#            i += 1
#    return d
#
#c = int(input('how many fibonacci numbers: '))
#print(fibo(c))
#FIBONACCI-----------------------------------

    
##while True:
##    u = str(input('Enter a word: '))
##    if u == 'chupacabra':
##        print('You have successfully left the loop.')
##        break

#k = open('PRESIDENTIAL VOTE ENTRIES.txt', 'r')
#m = k.readline()
#x = 'buhari'
#y = 'sowore'
#u = 0

##c = []
#for i in range(len(m)):
#    if 'buhari' in m:
#        c.append('buhari')
#    c = m.count('buhari')
#    d = m.count('sowore')
#print(c)
#if c > d:
#    print('Buhari wins by: ' + str(c) + ' votes')
#elif c < d:
#    print('Sowore wins by: ' + str(d) + ' votes')
#elif c == d:
#    while x[u] == y[u]:
#        u += 1
#    while x[u] != y[u]:
#        if x[u] < y[u]:
#            print('Buhari wins!')
#        elif x[u] > y[u]:
#            print('Sowore wins!')
#        break
#k.close()
#print(c)
        
#d = ['buhari', 'buhari', 'sowore', 'buhari', 'sowore', 'buhari', 'sowore', 'buhari', 'sowore', 'buhari', 'sowore', 'buhari', 'sowore', 'buhari', 'sowore']
#b = 1
#f = {}
#d = []
#for i in d:
#    if i not in f:
#        f[i] = b
#    else:
#        f[i] = f[i] + 1
#for k,v in f.__iter__():
#    if v == max(f.values()):
#        print(k)
#SETS
#b = {1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
#c = {9, 10, 11, 12, 3, 5, 8, 14, 15, 16, 17, 18}
#b.intersection_update(c)
#print(b)
target_names = {'target' : 'setosa', 'versicolor', 'virginica'
}
print(type(target_names))

##target_data = ['setosa', 'versicolor', 'virginica',
##               'setosa', 'versicolor', 'virginica',
##               'setosa', 'versicolor', 'virginica',
##               'versicolor', 'virginica',
##               'setosa','versicolor', 'virginica',
##               'setosa','versicolor', 'virginica',
##               'setosa','versicolor', 'virginica',
##               'setosa', 'virginica',
##               'setosa', 'virginica',
##               'setosa', 'setosa','versicolor', 'setosa', 'setosa',
##               'setosa', 'setosa', 'setosa', 'setosa',]
##target_val = {'target':''}
##x = 0
##for value in target_names.values():
##    if i in target_data:
##        target_val['target'].append(x)
##    x += 1
