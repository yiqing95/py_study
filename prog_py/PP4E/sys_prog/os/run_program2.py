__author__ = 'yiqing'

import os
##  类似 dos下的 start 命令！是并行执行的！不阻塞调用者进程
os.startfile('README.md')
os.startfile('os_path.py')

'''
the Unix
os.fork/exec and Windows os.spawnv calls can also be used to run parallel programs
without blocking.



module’s other weapons are these:
os.environ
Fetches and sets shell environment variables
os.fork
Spawns a new child process on Unix-like systems
os.pipe
Communicates between programs
os.execlp
Starts new programs
os.spawnv
Starts new programs with lower-level control
os.open
Opens a low-level descriptor-based file
os.mkdir
Creates a new directory
100 | Chapter 2: System Tools
www.it-ebooks.info
os.mkfifo
Creates a new named pipe
os.stat
Fetches low-level file information
os.remove
Deletes a file by its pathname
os.walk
Applies a function or loop body to all parts of an entire directory tree
'''