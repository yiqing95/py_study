__author__ = 'yiqing'

from io import StringIO

import sys

buff = StringIO()

temp = sys.stdout
sys.stdout = buff
print(42,'spam',3.141)
sys.stdout = temp
print(
    buff.getvalue()
)