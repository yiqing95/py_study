__author__ = 'yiqing'
"""
on Windows,
end-of-file is usually the two-key combination Ctrl-Z; on Unix, type Ctrl-D instead†):
"""
def interact():
    print('hello stream world')
    while True:
        try:
            reply = input('Enter a number')
        except EOFError:
            break
        else:
            num = int(reply)
            print("%d squared is %d" % (num,num*2))

    print('Bye')

'''
python teststreams.py < input.txt

python teststreams.py < input.txt > output.txt
type out.txt

This time, the Python script’s input and output are both mapped to text files, not to
the interactive console session
'''
if __name__ == '__main__':
    interact()


### 管道操作：
'''
python teststreams.py < input.txt | more

One Python script’s output can always be piped into
another Python script’s input
'''