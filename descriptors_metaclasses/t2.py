__author__ = 'yiqing'
'''
Properties with decorators
'''

class Square(object):
    """
    A square using properties with decorators.
    """

    def __init__(self,side):
        self.side = side

    @property
    def area(self):
        """
        Calculate the area of the square
        """
        return self.side * self.side

    @area.setter
    def area(self,val):
        print("Can't set the area ")

    @area.deleter
    def area(self):
        """
        Don't allow deleting
        """
        print("Can't delete the area ")

if __name__ == '__main__':
    s = Square(5)
    # read the area property
    print(s.area)
    # set the area property
    s.area = 2
    # delete the area property
    del s.area