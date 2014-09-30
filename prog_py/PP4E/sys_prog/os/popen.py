__author__ = 'yiqing'

import os

I = os.popen('dir /B *.py ')

print(I.__next__())