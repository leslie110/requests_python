# -*- coding:utf-8 -*-
import HTMLTestRunner
import unittest,time
import

def all_case():
    this_dir = r"F:\download\requests_python\126email"
    discover = unittest.defaultTestLoader.discover(this_dir,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    return discover

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = r"F:\download\requests_python\126email\report\\"+"测试报告"+now+".html"
    fp =open(filename,"wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="126邮箱测试报告",
                                           description="用例执行情况")
    runner.run(all_case())
    fp.close()