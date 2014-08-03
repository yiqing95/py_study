__author__ = 'yiqing'


class A(object):
    pass

print(A)
print(type(A))

class B:
    pass
print(type(B))

class C:
    # this is python2 syntax!
    __metaclass__ = type

print(type(C))

class C4py3(metaclass=type):
    pass

print(type(C4py3))

class  MyType(type):
    pass

class D(metaclass=MyType):
    pass
print(type(D))

print(dir(globals()))

# 重置全局变量中的元类型
__metaclass__ = MyType
__class__ = MyType
#  然后创建一个类
class D2:
    pass
# 不是预期那样哦 nnd
print(type(D2))

import types
print(types.ClassType)
