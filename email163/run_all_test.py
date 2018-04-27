# -*- coding:utf-8 -*-
import HTMLTestRunner
import unittest,time
from email163.public import send_email_fujian,new_file

def all_case():
    this_dir = r"F:\download\requests_python\email163"
    discover = unittest.defaultTestLoader.discover(this_dir,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    return discover

def run_case(report_dir):
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = report_dir + '\\'+"测试报告" + now + ".html"
    print (filename)
    fp = open(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="126邮箱测试报告",
                                           description="用例执行情况")
    runner.run(all_case())
    fp.close()
if __name__ == '__main__':
    report_dir = r"F:\download\requests_python\email163\report"
    run_case(report_dir)
    send = send_email_fujian
    dir = send.send_report(report_dir)
    send.send_email_acc(dir)
