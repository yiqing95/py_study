"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
# 测试下models
from contacts.models import Contact
from contacts.views import ContactListView


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class ContactTest(TestCase):
    def test_str(self):
        c = Contact(first_name= 'joe',last_name= 'Smith')
        # self.assertEqual(str(c),'joe Smith'+'oh no ')
        self.assertEqual(str(c),'joe Smith')


from django.test.client import  RequestFactory
class ContactListViewTests(TestCase):

    def test_no_contacts_in_context(self):

        factory = RequestFactory()
        request = factory.get('/')

        response = ContactListView.as_view()(request)

        self.assertEqual(
            list(response.context_data['object_list']),
            []
        )

    def test_contacts_in_context(self):

        factory = RequestFactory()
        request = factory.get('/')

        # 手动插入一条数据
        c = Contact.objects.create(
            first_name='qing',
            last_name = 'yi',
            email = 'qing@qq.com'
        )
        response = ContactListView.as_view()(request)

        self.assertEqual(
            list(response.context_data['object_list']),
            [c]
        )

'''
下面是安装selenium后的
pip install selenium
        '''

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class CreateContactIntegrationTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(CreateContactIntegrationTest,cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(CreateContactIntegrationTest,cls).tearDownClass()

    def test_add_contact(self):

        self.selenium.get('%snew' % (self.live_server_url,))
        # 填充表单输入
        self.selenium.find_element_by_id('id_first_name').send_keys('qing')
        self.selenium.find_element_by_id('id_last_name').send_keys('yi')
        self.selenium.find_element_by_id('id_email').send_keys('qing@qq.com')
        # 模拟提交按钮
        self.selenium.find_element_by_xpath("//input[@type='submit']").click()
        # 判断模型的第一条数据跟刚上面模拟插入的那条信息相符！
        self.assertEqual(Contact.objects.all()[0].first_name,'qing')