# -*- coding: utf-8 -*-
print ('Домашнє завдання №3')
print ('Перший рівень')
print ('Умова завдання №4:')
print ('''Ввести число, вивести його розряди та їх множники.''')
print ('#'*40)
x = k = int(input("Введіть ціле число: "))
s=0
print (x, '=', sep='', end='')
while x:
    roz_ch=x%10
    x=x//10
    print (roz_ch, '*10^', s, '+', sep='', end='')
    s=s+1
print('')
print('')

print ('Варріант зі списком:')
print (k, '=', sep='', end='')
l=[]
m=0
while k:
    r=k%10
    k=k//10
    l.append(str(r)+'*10^'+str(m))
    m+=1
print ('+'.join(l[::-1]))


