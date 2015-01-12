__author__ = 'yiqing'

file = open('data.txt')
lines = file.readlines()
'''
iterators combine the convenience of readlines() with the space efficiency of read
line() and are the preferred way to read text files by lines today.
'''
for line in lines:
    print(line,end='')

'''
In recent Pythons, the file object includes
an iterator which is smart enough to grab just one line per request in all iteration contexts,
including for loops and list comprehensions.
'''

file = open('data.txt')
for line in file:
    print(line,end='')

'''
If you want to see what really happens inside
the for loop, you can use the iterator manually; it’s just a __next__ method (run by the
next built-in function),
    '''
file = open('data.txt')
print(
    file.__next__()
)