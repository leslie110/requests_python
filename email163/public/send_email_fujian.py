# -*- coding:utf-8 -*-
import smtplib,os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def send_report(result_dir):
#定义文件目录
    # lists = os.listdir(report_dir)
    # lists.sort()
    # file = lists[-1]
    # print (report_dir +'\\'+ file)
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
    file = os.path.join(result_dir,lists[-1])
    print (file)
    return file
def send_email_acc(dir):
    #定义邮箱
    send_from = "15309215554@163.com"
    send_to = '616387521@qq.com'
    send_server = 'smtp.163.com'
    #登录账号密码
    username = '15309215554@163.com'
    passwd = "616387521"
    #定义附件
    msgRoot = MIMEMultipart()
    subject = u'附件发送'
    msgRoot['Subject'] = Header(subject,'utf-8')
    msgRoot['From'] = Header(send_from,'utf-8')
    msgRoot['To'] = Header(send_to,'utf-8')
    #这里是邮件正文
    body = MIMEText(u'163测试完成','plain','utf-8')
    msgRoot.attach(body)
    #这里是附件
    acc = MIMEText(open(dir,'rb').read(),'base64','utf-8')
    acc.add_header('Content-Disposition','attachment',filename='result.html')
    msgRoot.attach(acc)
    #发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(send_server)
    smtp.login(username,passwd)
    smtp.sendmail(send_from,send_to,msgRoot.as_string())
    smtp.quit()
    print ("邮件发送成功")
