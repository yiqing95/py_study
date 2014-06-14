from debugly4 import debugattr

__author__ = 'yiqing'

# from debugly2 import debug
from debugly3 import debug, debugmethods


@debug(prefix='yi-')
def add(x,y):
    return x + y

@debug
def sub(x,y):
    return x - y

@debug
def mul(x,y):
    return x * y

@debug
def div(x,y):
    return x / y

# 装饰器用来修饰某个类
# 类方法跟静态方法 不被wrap哦！
@debugmethods
class Spam:
    @classmethod
    def grok(cls):
        pass

    @staticmethod
    def bar():
        pass

    def a(self):
        pass

    def b(self):
        pass

@debugattr
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
