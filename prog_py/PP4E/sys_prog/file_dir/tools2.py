__author__ = 'yiqing'

import os
'''
os.rename(
    'spam.txt',
    'eggs.txt'
)

os.remove(
    'spam.txt'
)
'''

open(
    'spam.txt'
,'w')

info = os.stat('spam.txt')
print(
    info
)

import stat
print(
    info[stat.ST_MODE],
    info[stat.ST_SIZE],
)