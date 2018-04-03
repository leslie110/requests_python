# -*- coding:utf-8 -*-

#登录
def login(driver):
    frame = driver.find_element_by_xpath("//*[@id='x-URS-iframe']")
    driver.switch_to.frame(frame)
    driver.find_element_by_xpath("//*[@name='email']").clear()
    driver.find_element_by_xpath("//*[@name='email']").send_keys("15309215554")
    driver.find_element_by_css_selector("[name='password']").send_keys("616387521")
    driver.find_element_by_css_selector("#dologin").click()
#退出
def logout(driver):
    driver.find_element_by_link_text("退出")