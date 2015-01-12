__author__ = 'yiqing'
import sys

for stream in (sys.stdin,sys.stdout,sys.stderr):
    print(stream.fileno())

sys.stdout.write('hello stdio world\n')

import os
os.write(1,b'hello descriptor world\n')