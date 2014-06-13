__author__ = 'yiqing'

from functools import wraps
import  logging

def debug(func):
    log = logging.getLogger(func.__module__)
    msg = func.__qualname__
    # func is function to be wrapped
    @wraps(func)
    def wrapper(*args,**kwargs):
        #  print(func.__qualname__)
        # print(func.__name__)
        log.debug(msg)
        return func(*args,**kwargs)
    return wrapper

