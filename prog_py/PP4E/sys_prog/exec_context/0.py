__author__ = 'yiqing'

'''
操作系统 传递给py脚本的东西

阴阳世界  操作系统是外部环境 py脚本形成内部空间  外部总是会传递东西进来

四类：
Current working directory
os.getcwd gi ves access t o t he direct or y fr om whi ch a scri pt i s st art ed, and many fil e
tools use its value implicitly.
Command-line arguments
sys.argv gives access to words typed on the command line that are used to start
the program and that serve as script inputs.
Shell variables
os.environ provides an interface to names assigned in the enclosing shell (or a
parent program) and passed in to the script.
Standard streams
sys.stdin, stdout, and stderr export t he t hree i nput/ out put strea ms t hat are at t he
heart of command-line shell tools, and can be leveraged by scripts with print options,
the os.popen call and subprocess module introduced in Chapter 2, the
io.StringIO class, and more.

Such tools can serve as inputs to scripts, configuration parameters, and so on. In this
chapter, we will explore all these four context’s tools—both their Python interfaces
and their typical roles.

'''

import os ,sys
print(
    os.getcwd,
    sys.argv,
    os.environ,

)