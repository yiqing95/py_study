__author__ = 'yiqing'
"""
The standard streams are simply preopened Python file objects that are automatically
connected to your program’s standard streams when Python starts up.
"""
import sys
for f in (sys.stdin,sys.stdout,sys.stderr):
    print(f)

print('hello stdout world')
'''
上面的方法只是下面方法的简单入口
'''
sys.stdout.write('hello stdout world'+'\n')

### 下面亦等价效果
'''
Because the print and input built-in functions are really nothing more than userfriendly
interfaces to the standard output and input streams, they are similar to using
stdout and stdin in sys directly
'''
input('hello stdin world>')
print('hello stdin wold'); sys.stdin.readline()[:1]