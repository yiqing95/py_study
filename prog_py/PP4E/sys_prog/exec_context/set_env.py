__author__ = 'yiqing'

import os

print('setenv...',end='')
if 'USER' in os.environ:
    print(os.environ['USER'])

os.environ['USER'] = 'Brian'
os.system('python echoenv.py')


os.environ['USER'] = 'Arthur'
os.system('python echoenv.py')

os.environ['USER'] = input('?')
print(
    os.popen('python echoevn.py').read()
)