__author__ = 'yiqing'

def debug(func):
    # func is function to be wrapped
    def wrapper(*args,**kwargs):
        print(func.__name__)
        return func(*args,**kwargs)
    return wrapper

