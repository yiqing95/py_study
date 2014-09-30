__author__ = 'yiqing'

import sys

sum = 0

while True:
    try:
        line = input()
    except EOFError:
        break
    else:
        sum += input(line)

print(sum)

'''
python sorter.py < data.txt
'''