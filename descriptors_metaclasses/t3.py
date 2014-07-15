__author__ = 'yiqing'

"""
蛋疼的 不能运行 找不到原因
"""
def nested_property(func):
    '''
    Make defining properties simpler
    '''
    names = func()
    names['doc'] = func.__doc__
    return property(**names)

class Square(object):
    '''
    A square using properties with decorators.
    '''

    def __init__(self,side):
        self.side = side


    @nested_property
    def area():
        '''
        why the above method will appear a warning sign
        Property that defines is methods nested
        '''
        def fget(self):
            return self.side * self.side
        def fset(self,val):
            print("Don't allow to set the area")

        def fdel(self):
            print("Can't delete the area.")

        print(locals())
        return locals()

if __name__ == '__main__':
    s = Square(14)

    s.area = 3

    print(s.area)

    del s.area

    # print(s.area.__doc__)