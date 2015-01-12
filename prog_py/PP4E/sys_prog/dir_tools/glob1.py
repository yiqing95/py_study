__author__ = 'yiqing'

import glob
lines = glob.glob('*')

print(lines)

print(glob.glob('*.bin'))

for path in glob.glob(r'PP3E\Examples\PP3E\*\s*.py'): print(path)