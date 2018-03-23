# -*- coding:utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://mail.163.com")
time.sleep(3)
frame = driver.find_element_by_xpath("//*[@id='x-URS-iframe']")
driver.switch_to.frame(frame)
driver.find_element_by_xpath("//*[@name='email']").clear()
driver.find_element_by_xpath("//*[@name='email']").send_keys("15309215554")
