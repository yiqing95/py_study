__author__ = 'yiqing'

from functools import wraps

def debug(prefix=''):
    def decorate(func):
        msg = prefix + func.__qualname__
        # func is function to be wrapped
        @wraps(func)
        def wrapper(*args,**kwargs):
            #  print(func.__qualname__)
            print(msg)
            return func(*args,**kwargs)
        return wrapper
    return decorate

