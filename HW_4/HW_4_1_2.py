# -*- coding: cp1251 -*-
print ('Домашнє завдання №4')
print ('Умова завдання №2 (практика):')
print ('Написати програму, яка виводить сама себе.')
print ('#'*60)
import sys
filename = sys.argv[0] # далі відкриваємо файл для читання (опція 'r')
f = open(filename, 'r') # в файлі тепер file descriptor
for line in f: # для кожного рядка у файлі
    print(line, end='')
f.close() # закриття файлу