# -*- coding:utf-8 -*-
#登录
def login(self,username, password):
    driver = self.driver
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("dologin").click()

#退出
def logout(self):
    driver = self.driver
    driver.find_element_by_xpath('''//*[@id="_mail_component_41_41"]/a''').click()


def trylogin(self):
    driver = self.driver
    try:
        test = driver.find_element_by_id("spnUid").text
        self.assertEqual(test,"test616387@126.com")
        print (test)
        return True
    except:
        return False




