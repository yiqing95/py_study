__author__ = 'yiqing'

print('this is a mod in %s ' % __package__)

print('------------------------------\n ')
print('相对导入string mod ')
from . import string
print(string.__name__)

from .string import name1,name2
print('here are two module variables defined in string mod : ',name1,name2)

print('------------------------------\n ')

print('relative import example 2 : ')
from  .. import my_util
print(my_util.__name__)
print('import the util mod from a sibling of parent dir of this file  ')
