__author__ = 'yiqing'

import os

fd = os.open('spam.txt',os.O_TEXT|os.O_RDWR)

os.write(fd,b'hi !')

