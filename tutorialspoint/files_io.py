__author__ = 'yiqing'

str = input('Enter your input:')
print('Received input is :',str)

'''
===============================================
'''

# fo = open('foo.txt','wb')
fo = open('foo.txt','w')
print(fo.__dict__)
print(fo)
print('Name of the file:',fo.name)
print('Closed or not :',fo.closed)
print('Opening mode:',fo.mode)
# print('Softspace flag :',fo.softspace)

# Write string to the file object
fo.write('Python is a great language \nYeah its great !!\n ')

fo.close()

'''
-----------------------------------------------------------
'''
fo = open('foo.txt','r+')
str = fo.read()
print('Reading string is :\n',str)

fo.close()

'''
-----------------------------------------------------------
'''
fo = open('foo.txt','r+')
str = fo.read(2)
print('Reading string is :\n',str)
# Check current position
pos = fo.tell()
print('Current file position:',pos)
# Reposition pointer at the beginning once again
pos = fo.seek(0,0)
str = fo.read(10)
print('Again read string is :',str)
fo.close()