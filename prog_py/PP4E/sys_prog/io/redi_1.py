__author__ = 'yiqing'

from subprocess import Popen ,PIPE ,call

X = call('python hello-out.py')
print(X)

pipe = Popen('hello-out.py',stdout=PIPE)
print(
    pipe.communicate()[0]
)
print(
    pipe.returncode
)