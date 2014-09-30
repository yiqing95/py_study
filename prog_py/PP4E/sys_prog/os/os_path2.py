__author__ = 'yiqing'

import os

print(
    os.chdir(r'C:\Users'),
os.getcwd()
)

print(
    os.path.abspath(''),
    os.path.abspath('temp'),
    os.path.abspath(r'PP4E\dev'),
)

print(
    os.path.abspath('.'),
    os.path.abspath('..'),
    os.path.abspath(r'..\examples'),
)

## 绝对路径
print(
    os.path.abspath(r'c:\PP4thEd\chapters'),
    os.path.abspath(r'c:\temp\spam.txt')
)