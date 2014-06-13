__author__ = 'yiqing'

from functools import wraps

def debug(func):
    # func is function to be wrapped
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(func.__name__)
        return func(*args,**kwargs)
    return wrapper

