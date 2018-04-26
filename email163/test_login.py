# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest,time
from public import login
import HTMLTestRunner

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = "http://www.126.com"
        self.driver.implicitly_wait(30)
        self.verificationError = []



    def test_login(self):
        '''登录邮箱成功测试'''
        driver = self.driver
        driver.get(self.url)
        time.sleep(2)
        driver.switch_to.frame(0)
        #登录126邮箱
        login.login(self,"test616387","a123456")
        #获取断言信息进行验证
        test = login.trylogin(self)
        self.assertTrue(test)

        #退出操作
        login.logout(self)

    def test_login2(self):
        '''错误登录测试'''
        driver = self.driver
        driver.get(self.url)
        time.sleep(2)
        driver.switch_to.frame(0)
        #无用户名和密码
        login.login(self,"","")
        # 获取断言信息进行验证
        test = login.trylogin(self)
        self.assertTrue(test)
        # 退出操作
        login.logout(self)

    def test_login3(self):
        '''不输入用户名登录测试'''
        driver = self.driver
        driver.get(self.url)
        time.sleep(2)
        driver.switch_to.frame(0)
        #无用户名和密码
        login.login(self,"test616387","")
        # 获取断言信息进行验证
        test = login.trylogin(self)
        self.assertTrue(test)
        # 退出操作
        login.logout(self)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationError)

if __name__ =="__main__":
    testsuite = unittest.TestSuite()
    testsuite.addTest(TestLogin('test_login'))
    testsuite.addTest(TestLogin('test_login2'))
    testsuite.addTest(TestLogin('test_login3'))
    now = time.strftime("%Y-%m-%d %H_%M_%S")



    filename = "F:\\download\\Pythontest\\eig _test_case\\report\\" + u"测试报告" + now + ".html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'搜索功能测试报告',
        description=u'用例执行情况：')

    runner.run(testsuite)
