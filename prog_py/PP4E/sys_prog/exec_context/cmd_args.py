__author__ = 'yiqing'
"""
测试输入命令
python  cmd_args.py -i data.txt -o results.txt

Much like function arguments,
command-line options are sometimes passed by position and sometimes by
name using a “-name value” word pair.

Command-line arguments play the same role in programs that function arguments do
in functions: they are simply a way to pass information to a program that can vary per
program run. Because they don’t have to be hardcoded, they allow scripts to be more
generally useful. For example, a file-processing script can use a command-line argument
as the name of the file it should process;
"""

import sys

print(sys.argv)