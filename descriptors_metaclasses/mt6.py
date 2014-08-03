__author__ = 'yiqing'

import  builtins

DEBUG = True
import sys

if DEBUG:
    class DebugMeta(type):
        names = []
        counter = 0

        def __init__(cls,name,bases,cls_dict):
            DebugMeta.names.append('%s.%s'%(cls.__module__,name))
            DebugMeta.counter += 1
            print('Debug metaclass in action %d' % DebugMeta.counter)
            print(DebugMeta.names)
            super(DebugMeta,cls).__init__(name,bases,cls_dict)

    class new_object(metaclass=DebugMeta):
        pass
    # 更换掉系统默认的 最基类 跟元类根
    builtins.object = new_object
    builtins.type = DebugMeta

class C1(object):
    pass
class C2(object):
    pass
class C3(object):
    pass
C4 = type('C4',(object,),{})


