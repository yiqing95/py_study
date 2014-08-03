__author__ = 'yiqing'

'''
Example for descriptor that checks conditions on attr
'''
import  uuid

class Checked(object):

    def __init__(self,checker = None,default=None):
        if checker:
            if(callable(checker)):
                checker(default)
            else:
                raise TypeError('must be a callable ')
        self.hidden_name = '__'+ uuid.uuid4().hex
        self.checker = checker
        self.default = default

    def __get__(self, instance, owner):
        return getattr(instance,self.hidden_name,self.default)

    def __set__(self, instance, value):
        if self.checker:
            self.checker(value)

        setattr(instance,self.hidden_name,value)

if __name__ == '__main__':

    def is_int(val):
       """
       check if value is an integer
       """
       if not isinstance(val,int):
           raise  ValueError('Int required {} found'.format(type(val)))

    class Restricted(object):
        """
        Use checked attributes
        """
        attr1 = Checked(checker=is_int,default=10)
        attr2 = Checked(default=12.5)

        # setting the default to float ,cause raise a ValueError
        try:
            attr3 = Checked(checker=is_int,default=22.5)

        except ValueError:
            print("Can't set default value to float ,must be int  ")
            attr3 = Checked(checker=is_int,default=12)
    r1 = Restricted()
    print('attr1',r1.attr1)
    r1.attr1 = 100
    print('attr1',r1.attr1)
    try:
        r1.attr1 = 200.12
    except ValueError:
        print('Cannot set attr1 to float ,must be int. ')
        r1.attr1 = 200