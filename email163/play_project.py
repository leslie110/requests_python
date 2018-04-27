# -*- coding:utf-8 -*-

import os,time

k = 1
while k < 2:
    now = time.strftime("%H_%M")
    if now == "10_56":
        print ("执行任务")
        os.chdir(r"F:\download\Pythontest\eig _test_case\126email")
        os.system("python test_login.py")
        print ("执行完毕")
        break
    else:
        time.sleep(10)
        print (now)
