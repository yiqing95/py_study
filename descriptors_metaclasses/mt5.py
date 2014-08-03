__author__ = 'yiqing'

class NoClassAttributes(type):
    def __init__(cls,name,bases,cls_dict):
        allowed = set(['__module__','__metaclass__','__doc__'])
        for key ,val in cls_dict.items():
            print('--'*45)
            print(val)
            if(
                        (key not in allowed)
                    and
                   # (not hasattr(val,'__call__'))
                   (not callable(val))
            ):
                msg = 'Found non-callable class: '+name
                msg += 'Only methods are allowed '
                raise Exception(msg)
            super(NoClassAttributes,cls).__init__(name,bases,cls_dict)


if __name__ == '__main__':
    class AttributeLess(metaclass= NoClassAttributes):
        def meth(self):
            print('hello from attributes')
    try:
        a = AttributeLess()
        a.meth()
    except:
        print('主人出错啦！  ')
    class WithAttribute(metaclass= NoClassAttributes):
        a = 10
        def meth(self):
            print('hello from WithAttribute')

    wa = WithAttribute()
    wa.meth()