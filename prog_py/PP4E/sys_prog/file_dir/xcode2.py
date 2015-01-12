__author__ = 'yiqing'

strlen = open('temp.txt','w').write(
    'shrubbery\n'
)
print(strlen)
print(
    open('temp.txt','rb').read()
)
print(
    open('temp.txt','r').read()
)
