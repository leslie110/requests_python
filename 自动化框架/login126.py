# -*- coding:utf-8 -*-
from selenium import webdriver
import time,public


driver = webdriver.Chrome()
driver.get("http://mail.163.com")
time.sleep(3)
public.login(driver)
time.sleep(3)
public.logout(driver)
driver.quit()