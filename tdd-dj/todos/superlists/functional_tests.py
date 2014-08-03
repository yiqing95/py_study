__author__ = 'yiqing'

import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        self.browser.implicitly_wait(3)

    def test_starting_a_todo_list(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do',self.browser.title)

        self.fail('finish the test ')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
