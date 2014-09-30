__author__ = 'yiqing'
"""
@see github.com/hprose/hprose-python3
"""
import hprose

def main():
    client  = hprose.HttpClient('http://localhost/my/cxtx-web/web/test/api/hprose')
    print(client.hello('world'))

if __name__ ==  '__main__':
    main()