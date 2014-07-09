__author__ = 'yiqing'

import  shelve
fieldnames = ('name','age','job','pay')
maxfield = max(len(f) for f in fieldnames)
db = shelve.open('class-shelve')

while True:
    key = input('\nkey? => ')
    if not key: break
    try :
        recode = db[key]
    except:
        print('No such key "%s"! '% key)

    else:
        for field in fieldnames:
            print(field.ljust(maxfield),'=>',getattr(recode,field))
