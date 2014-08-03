__author__ = 'yiqing'

class NameException(Exception):
    pass

class NameChecked(type):

    def __init__(cls,name,bases,cls_dict):
        for name ,val in cls_dict.items():

            if(hasattr(val,'__call__')):
                print('方法内部结构',val)
                if(callable(val)):
                    print('这是个方法哦！')
                name_len = len(name)
                if name_len> 10:
                    msg = 'method name {} is too long!!'.format(name)
                    raise NameException(msg)
        super(NameChecked,cls).__init__(name,bases,cls_dict)
class T1(metaclass= NameChecked):
    def foo(self):
        pass

class T(metaclass= NameChecked):
    def foo(self):
        pass

    def this_is_a_very_long_method_of_T(self):
        pass


