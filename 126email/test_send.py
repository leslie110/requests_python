# -*- coding:utf-8 -*-
from selenium import webdriver
from public import login
import unittest,time
'''126邮箱发送邮件测试'''
class TestSendEmail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://www.126.com"
        self.driver.implicitly_wait(30)
        self.verificationErrors = []

    def test_send_email(self):
        '''发送邮件测试'''
        driver = self.driver
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(2)
        driver.switch_to.frame(0)
        login.login(self,"test616387","a123456")
        login.trylogin(self)
        driver.find_element_by_xpath('''//*[@id="_mail_component_70_70"]/span[2]''').click()
        time.sleep(1)
        driver.find_element_by_class_name("nui-editableAddr-ipt").send_keys("wangshaobo@ttg.cn")
        time.sleep(2)
        name = driver.find_element_by_class_name("APP-editor-iframe")
        driver.switch_to.frame(name)
        driver.find_element_by_xpath("/html/body").send_keys(u"小明你好！")
        driver.switch_to.default_content()
        driver.find_element_by_class_name("nui-btn-text").click()
        time.sleep(1)
        text = driver.find_element_by_xpath('''//*[@id="1508469869086_succInfo"]''').text
        self.assertEqual(text,u"发送成功")
        login.logout()
    def tearDown(self):
        driver = self.driver
        driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
