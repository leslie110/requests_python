# -*- coding:utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://mail.163.com")
time.sleep(3)
def login():
    frame = driver.find_element_by_xpath("//*[@id='x-URS-iframe']")
    driver.switch_to.frame(frame)
    driver.find_element_by_xpath("//*[@name='email']").clear()
    driver.find_element_by_xpath("//*[@name='email']").send_keys("15309215554")
    driver.find_element_by_css_selector("[name=password]").send_keys("616387521")
    driver.find_element_by_css_selector("#dologin").click()