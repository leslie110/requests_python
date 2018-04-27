# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from test_frame.pub import public

driver = webdriver.Chrome()
driver.get("http://mail.163.com")
time.sleep(3)
name = "15309215554"
pasd = "616387521"
public.login(driver,name,pasd)
time.sleep(3)
public.logout(driver)
driver.quit()