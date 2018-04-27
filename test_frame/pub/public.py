# -*- coding:utf-8 -*-

#登录
def login(driver,name,pasd):
    frame = driver.find_element_by_xpath("//*[@id='x-URS-iframe']")
    driver.switch_to.frame(frame)
    driver.find_element_by_xpath("//*[@name='email']").clear()
    driver.find_element_by_xpath("//*[@name='email']").send_keys(name)
    driver.find_element_by_css_selector("[name='password']").send_keys(pasd)
    driver.find_element_by_css_selector("#dologin").click()
#退出
def logout(driver):
    driver.find_element_by_link_text("退出")