__author__ = 'yiqing'
'''
收集命令行选项为字典
测试： parsing_cmd_args.py  myInputFile -out hiOutHere
'''

def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
            argv = argv[2:]
        else:
            argv = argv[1:]

    return opts

if __name__ == '__main__':
    from  sys   import argv
    myargs = getopts(argv)
    if '-i' in myargs:
        print(myargs['-i'])
    print(myargs)

'''
The getopt module, modeled after a Unix/C utility of the same name
• The optparse module, a newer alternative, generally considered to be more
powerful

=====================================
Executable Scripts on Unix
Unix and Linux users: you can also make text files of Python source code directly
executable by adding a special line at the top with the path to the Python interpreter
and giving the file executable permission. For instance, type this code into a text file
called myscript:
#!/usr/bin/python
print('And nice red uniforms')

but it’s worth pointing out
that it can be made a bit less machine dependent by listing the Unix env command at
the top instead of a hardcoded path to the Python executable:
#!/usr/bin/env python
print('Wait for it...')
When coded this way, the operating system will employ your environment variable
settings to locate your Python interpreter (your PATH variable, on most platforms). If
you run the same script on many machines,
    '''