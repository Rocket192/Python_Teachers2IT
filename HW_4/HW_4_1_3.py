# -*- coding: cp1251 -*-
print ('Домашнє завдання №4')
print ('Умова завдання №3 (практика):')
print ('Написати програму, яка виводить сама себе.')
print ('#'*60)
import sys, string
filename = sys.argv[0] # далі відкриваємо файл для читання (опція 'r')
f = open(filename, 'r') # в файлі тепер file descriptor
for line in f: # для кожного рядка у файлі
    print("".join(reversed(str(line))), end='')
f.close() # закриття файлу