# -*- coding: utf-8 -*-
print ('Домашнє завдання №4')
print ('Умова завдання №1 (практика):')
print ('Кожен пише суму списку за допомогою for та while.')
print ('#'*60)
# створюємо та заповнюємо список
from random import randint
l = [] # створюємо порожній список.
for x in range(1, 11): # заповнюємо список з 10 елементів випадковими числами від -1000 до 1000.
    l.append(randint( -1000, 1000 )) # створення елементу списку (генеруємо випадкове число в діапазоні від -1000 до 1000.
print ('Список', l) # виводимо значення єлементів списку

# обраховуємо суму елементві списку за допомогою циклу for
print ('Обраховуємо суму елементві списку за допомогою циклу for:')
s = 0 # 
for i in l: # 
    s +=i
print ('Сума елементів списку:', s) #

print ('#'*60)
print ('Обраховуємо суму елементві списку за допомогою циклу while:')
# обраховуємо суму елементві списку за допомогою циклу while
print ('Список', l) # виводимо значення єлементів списку
n = 0 # 
b = len (l) # 
s = 0
while n<b:
    s += l[n]
    n += 1
print ('Сума елементів списку:', s) #    