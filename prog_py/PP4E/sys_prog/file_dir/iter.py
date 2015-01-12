__author__ = 'yiqing'

print(
 open('data.txt').readlines()
)

print(
    list(
        open('data.txt')
    )
)

lines = [line.upper() for line in open('data.txt')]

list(
    map(
        str.split,
        open('data.txt'),
    )
)

line = 'hello '
if line in open('data.txt'):
    print('True')