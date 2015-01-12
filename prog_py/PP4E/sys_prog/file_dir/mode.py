__author__ = 'yiqing'
"""
the mode string defaults to r for read but can be w for write
and a for append, and you may add a + for update, as well as a b or t for binary or
text mode; order is largely irrelevant.
"""
file = open('data.txt','a')
file.write('The Life of Brian')
file.close()

print(open('data.txt','r').read())