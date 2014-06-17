__author__ = 'yiqing'

import traceback

try:
    raise Exception
except Exception as ex:
        traceback.print_tb(ex.__traceback__)