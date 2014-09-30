__author__ = 'yiqing'
"""
Shell variables, sometimes known as environment variables, are made available to Python
scripts as os.environ, a Python dictionary-like object with one entry per variable
setting in the shell. Shell variables live outside the Python system; they are often set at
your system prompt or within startup files or control-panel GUIs and typically serve
as system-wide configuration inputs to programs.
系统级的程序配置

Shell variables can also be set by programs to serve as inputs to other programs in an
application;

也可以作为程序间通信的通道！

because their values are normally inherited by spawned programs, they
can be used as a simple form of interprocess communication.

"""

"""
Indexing os.environ by the desired shell variable’s name string (e.g.,
os.environ['USER']) is the moral equivalent of adding a dollar sign before a variable
name in most Unix shells (e.g., $USER), using surrounding percent signs on DOS
(%USER%), and calling getenv("USER") in a C program.
"""

import os
print(
    os.environ.keys()
)
'''
打印所有的系统变量key
'''
print(
    list(os.environ.keys())
)

# 某个系统变量
print(os.environ['PATH'])
print(os.environ['TEMP'])

print(os.environ['PYTHONPATH'])

for srcdir in os.environ['PYTHONPATH'].split(os.pathsep):
    print(srcdir)

    import sys
    print(sys.path[:3])
    '''
    As usual, sys.path is the actual search path at runtime, and reflects the
result of merging in the PYTHONPATH setting after the current directory.
'''

### 写环境变量
## key assignments to os.environ call os.putenv
os.environ['TEMP2'] = r'c:\temp'
print(
    os.environ['TEMP2']
)
del os.environ['TEMP2']