__author__ = 'yiqing'
import os
'''
可以借助os模块运行shell命令
os.system
Runs a shell command from a Python script
os.popen
Runs a shell command and connects to its input or output streams

subprocess模块提供了更精细的控制
'''

## block模式
print(os.system('dir /B'))
print(os.system('type hellshell.py'))
"""
The command’s output normally shows up in the Python session’s or program’s
standard output stream
"""

#### 输出输入流跟命令行对接 file-like
text = os.popen('type helloshell.py').read()

listing = os.popen('dir /B').readlines()
print(listing)

### 运行其他py脚本
print(
    os.system('python os_path.py'),
    os.popen('python os_path2.py').read()
)