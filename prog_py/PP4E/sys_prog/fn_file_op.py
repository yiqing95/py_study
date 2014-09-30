__author__ = 'yiqing'

# print(open('ch1.1.py').read())
# print(open('ch1.1.py').readlines())
file = open('spam.txt','w')
file.write(('spam'*5)+'\n')

file.close()

file = open('spam.txt')
text = file.read()
print(text)