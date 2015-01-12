__author__ = 'yiqing'

# file = open(r'C:\temp\spam.txt','w')
file = open(r'spam.txt','w')
file.write('hello stdio file\n')
file.flush()
fd = file.fileno()
print(
    fd
)

import os
os.write(fd,b'hello descriptor file\n')
file.close()
