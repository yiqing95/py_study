__author__ = 'yiqing'

'''
注意安装 bs4：
    pip install beautifulsoup4
'''
from bs4 import BeautifulSoup
import urllib3

import selenium.webdriver as sl_webdriver

def get_tree(url):
    conn = urllib3.connection_from_url(url)
    source = conn.urlopen('get',url).data
    tree = BeautifulSoup(source)
    return tree


def selenium_test(url):
    # pass
    browser = sl_webdriver.Firefox()
    resp = browser.get(url)
    print(resp)
    browser.execute_script('alert("hi ");')

'''
lxml:  这个库在windows下安装可能有些问题
也可以用这个库来解析html文本
'''

if __name__ == '__main__':
    url = 'http://itjuzi.com/'
    '''
    tree = get_tree(url)
    print(tree)
    print(tree.findAll('p'))
    '''

    selenium_test(url)