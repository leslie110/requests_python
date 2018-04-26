# -*- coding:utf-8 -*-
from email.mime.text import MIMEText
import smtplib
from email.header import Header

#发送邮箱
send_form = '15309215554@163.com'
#接收邮箱
send_to = '616387521@qq.com'
#发送邮件主题
subject = "python email test"
#发送邮箱服务器
smtpserver = 'smtp.163.com'
#发送邮箱账号密码
username = '15309215554@163.com'
password = '616387521'

#编写text类型邮箱正文
body = '<html><h1> 亲爱的hani你好! </h1></html>'
msg = MIMEText(body,'html','utf-8')
msg['Subject'] = Header(subject,'utf-8')
msg['From'] = send_form
msg['To'] = send_to
#发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username,password)
smtp.sendmail(send_form,send_to,msg.as_string())
smtp.quit()
