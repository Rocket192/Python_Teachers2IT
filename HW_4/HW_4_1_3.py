# -*- coding: cp1251 -*-
print ('������ �������� �4')
print ('����� �������� �3 (��������):')
print ('�������� ��������, ��� �������� ���� ����.')
print ('#'*60)
import sys, string
filename = sys.argv[0] # ��� ��������� ���� ��� ������� (����� 'r')
f = open(filename, 'r') # � ���� ����� file descriptor
for line in f: # ��� ������� ����� � ����
    print("".join(reversed(str(line))), end='')
f.close() # �������� �����