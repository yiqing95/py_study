__author__ = 'yiqing'

from debugly5 import *

class Base(metaclass=debugmeta):
    pass

class MyClass(Base):
    def __init__(self,x):
        self.x = x
