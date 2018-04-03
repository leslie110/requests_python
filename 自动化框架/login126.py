# -*- coding:utf-8 -*-
from selenium import webdriver
import time
def login():
    frame = driver.find_element_by_xpath("//*[@id='x-URS-iframe']")
    driver.switch_to.frame(frame)
    driver.find_element_by_xpath("//*[@name='email']").clear()
    driver.find_element_by_xpath("//*[@name='email']").send_keys("15309215554")
    driver.find_element_by_css_selector("[name='password']").send_keys("616387521")
    driver.find_element_by_css_selector("#dologin").click()

def logout():
    driver.find_element_by_link_text("退出")

driver = webdriver.Chrome()
driver.get("http://mail.163.com")

login()
time.sleep(3)
logout()
driver.quit()