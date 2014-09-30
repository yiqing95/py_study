__author__ = 'yiqing'

import pymysql

try :
    conn = pymysql.connect(host='localhost',user='root',passwd='', db='test',port=3306,charset='utf8')

    cur = conn.cursor()
    cur.execute('show databases')

    rs = cur.fetchall()
    for r in rs:
        print(r)

    cur.close()

    conn.close()

except Exception as ex:
    print(ex)