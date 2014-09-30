__author__ = 'yiqing'
"""
stderr can be similarly reset
to files, pipes, and objects.

no higher-level tools for standard
error do what print and input do for the output and input streams. If you wish to print
to the error stream, you’ll want to call sys.stderr.write() explicitly or read the next
section for a print call trick that makes this easier.

Redirecting standard errors from a shell command line is a bit more complex and less
portable. On most Unix-like systems, we can usually capture stderr output by using
shell-redirection syntax of the form command > output 2>&1. This may not work on some
platforms,
"""

import sys

## 默认file是stdout！
print('spam'*2,file=sys.stderr)

from io import StringIO
buff = StringIO()
print(42,file=buff)
print('spam',file=buff)
print(
    buff.getvalue()
)

"""
## 没有redirect模块呀！
from redirect import Output
>>> buff = Output()
>>> print(43, file=buff)
>>> print('eggs', file=buff)
>>> print(buff.text)
"""