__author__ = 'yiqing'

class  Square(object):
    def __init__(self,side):
        self.side = side

    def aget(self):
        return self.side * self.side

    def aset(self,val):
        print('Can not change the area.')

    def adel(self):
        print('can not delete the area.')

    area = property(aget,aset,adel,doc='Area of the square .')

if __name__ == '__main__':
    s = Square(3)
    print(s.area)
    try:
        del s.area
    except Exception as e:
        print(e)

    try:
        s.area = 2
    except Exception as e:
        print(e)

    print(Square.area.__doc__)