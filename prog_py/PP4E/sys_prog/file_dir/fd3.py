__author__ = 'yiqing'
import os

fdfile = os.open('spam.txt',(os.O_RDWR|os.O_BINARY))
print(
    fdfile
)

objfile = os.fdopen(fdfile,'rb')
print(
    objfile.read()
)