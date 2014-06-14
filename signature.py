from helper import errorCall

__author__ = 'yiqing'

from inspect import Parameter,Signature

fields = ['name','shares','price']
params = [  Parameter(fname,    Parameter.POSITIONAL_OR_KEYWORD)   for fname in fields ]

sig = Signature(params)

def foo(*args,**kwargs):
    bound = sig.bind(*args,**kwargs)
    for name , val in bound.arguments.items():
        print(name,val)

def func(*args,**kwargs):
    bound_args = sig.bind(*args,**kwargs)
    for name ,val in bound_args.arguments.items():
        print(name,'=',val)

print(foo(1,3,4))

# print(3,price=3,4)
print(foo(3,price=3,shares = 4))

try:
    print(foo(3,3))
except:
    print('参数不足哦')

errorCall(foo,4,5,5,56)

print(func('ACME',4,4,4))
print(func('ACme',price=33,shares=33))