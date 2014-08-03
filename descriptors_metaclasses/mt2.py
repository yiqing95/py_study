__author__ = 'yiqing'

# 动态创建类
C = type('C',(object,),{})

print(C)

def __init__(self,a):
    self.a = a

def add(self,a,b):
    return a+b

C2 = type('C2',(object,),{
    'x':1,
    '__init__':__init__,
    'add':add,
})
c = C2(2)
print(c.x,c.a)
print(c.add(3,5))

class NewMeta(type):
    def __str__(cls):
        return 'I am a class with name '+cls

class A(metaclass = NewMeta):
    pass

print(type(A),str(type(A)))
print(str(A))
