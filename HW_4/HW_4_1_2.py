# -*- coding: cp1251 -*-
print ('������ �������� �4')
print ('����� �������� �2 (��������):')
print ('�������� ��������, ��� �������� ���� ����.')
print ('#'*60)
import sys
filename = sys.argv[0] # ��� ��������� ���� ��� ������� (����� 'r')
f = open(filename, 'r') # � ���� ����� file descriptor
for line in f: # ��� ������� ����� � ����
    print(line, end='')
f.close() # �������� �����