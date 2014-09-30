__author__ = 'yiqing'

import sys
lines = sys.stdin.readlines()
lines.sort()

for line in lines: print(line ,end='')


'''
python writer2.py | python sorter.py | python adder.py
'''