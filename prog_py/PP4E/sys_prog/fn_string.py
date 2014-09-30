__author__ = 'yiqing'

mystr = 'xxxSPAMxxx'

pos = mystr.find('SPAM')
print(pos)

mystr = 'xxxaaxxaa'
print(mystr.replace('aa','SPAM'))

'''
in  is similar to find!
'''
if('SPAM'  in mystr):
    print('here you find the SPAM in your string .')

print('Ni' in mystr)

print(mystr.find('Ni'))

## like trim:
mystr = '\t   Ni\n'
print(mystr.strip())
print(mystr.rstrip())

mystr = 'SHRUBBERY'
print(mystr.lower())

print(mystr.isalpha())
print(mystr.isdigit())

##
import  string
print(string.ascii_lowercase)
print(string.whitespace)

mystr =  'aaa,bbb,cccc'
print(mystr.split(','))
mystr = 'a  b\nc\nd'
print(mystr.split())

delim = 'NI'
print(delim.join(['aaa','bbb','ccc']))

print('  '.join(['A','dead','parrot']))

chars = list('Lorreta')
print(chars)

## conversions
print(int('42'),eval('42'))

print(str(42),repr(42))

print('%d'%42,'{:d}'.format(42))

print('42'+str(1),int('42')+1)