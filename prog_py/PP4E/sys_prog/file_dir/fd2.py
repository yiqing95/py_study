__author__ = 'yiqing'

import os

fdfile = os.open(r'spam.txt',(os.O_RDWR|os.O_BINARY))
os.read(fdfile,20)

os.lseek(fdfile,0,0)
os.read(fdfile,100)

os.lseek(fdfile,0,0)
os.write(fdfile,b'HELLO')