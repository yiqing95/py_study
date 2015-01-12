__author__ = 'yiqing'
import os

lines = os.popen('dir /B ').readlines()

print(
 lines
)

for line in os.popen('dir /B'):
    print(
        line[:-1]
    )

lines = [line[:-1] for line in os.popen('dir /B')]
print(
    lines
)

lines = os.popen('dir *.py /B').readlines()

print(lines)

print(
    list(os.popen(r'dir parts /B'))
)

print(
    [fname for fname in os.popen(r'c:\cygwin\bin\ls parts')]
)