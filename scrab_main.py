__author__ = 'yiqing'

'''
注意安装 bs4：
    pip install beautifulsoup4
'''
from bs4 import BeautifulSoup
import urllib3

import selenium.webdriver as sl_webdriver
from selenium.webdriver.common.keys import Keys

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

def selenium_search():
    url = 'http://www.baidu.com'
    # pass
    browser = sl_webdriver.Firefox()
    browser.get(url)
    # browser.execute_script('alert("hi 我要搜索了 ");')
    # browser.implicitly_wait(20)
    # search_input = browser.find_element_by_id('kw1')
    search_input = browser.find_elements_by_tag_name('input')[0]
    # search_input.send_keys('python',Keys.RETURN)
    # search_input.send_keys('python')
    # search_input.text = 'python'
    print(search_input)
    search_input.send_keys('hi')

def selenium_search2():
    url = 'http://itjuzi.com/'
    # pass
    browser = sl_webdriver.Firefox()
    browser.get(url)

    person_list_div = browser.find_element_by_class_name('person-list')
    for div in person_list_div.find_elements_by_tag_name('div'):
        print(div.text)

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

    # selenium_test(url)
    #    selenium_search()
    selenium_search2()
